// @ts-ignore
const Me = imports.misc.extensionUtils.getCurrentExtension();

import type { Entity } from './ecs';
import type { Ext } from './extension';
import type { ShellWindow } from "./window";
import type { Stack } from './stack';

import * as Ecs from 'ecs';
import * as Tweener from 'tweener';

const { GLib, St } = imports.gi;

type Tracked = WindowDetails | StackDetails;

interface Details {
    sources: Array<number>;
}

interface WindowDetails extends Details {
    kind: 1
    entity: Entity;
    meta: Meta.Window;
    parent: Clutter.Actor;
}

interface StackDetails extends Details {
    kind: 2
    stack: Stack;
}

export class ActiveHint {
    dpi: number;

    border: [St.Widget, St.Widget, St.Widget, St.Widget] = [
        new St.BoxLayout({
            reactive: false,
            style_class: 'pop-shell-active-hint',
            visible: false
        }),
        new St.BoxLayout({
            reactive: false,
            style_class: 'pop-shell-active-hint',
            visible: false
        }),
        new St.BoxLayout({
            reactive: false,
            style_class: 'pop-shell-active-hint',
            visible: false
        }),
        new St.BoxLayout({
            reactive: false,
            style_class: 'pop-shell-active-hint',
            visible: false
        })
    ];

    private tracking: number | null = null;

    tracked: Tracked | null = null;

    restacker: SignalID = (global.display as GObject.Object).connect('restacked', () => {
        if (this.tracked) {
            let actor: null | Clutter.Actor = null;

            if (this.tracked.kind === 1) {
                actor = this.tracked.meta.get_compositor_private();
            } else if (this.tracked.stack.destroyed) {
                this.untrack();
            } else {
                actor = this.tracked.stack.tabs;
            }

            if (actor) this.restack(actor);
        }
    });

    constructor(dpi: number) {
        this.dpi = dpi;

        for (const box of this.border) {
            global.window_group.add_child(box);
            global.window_group.set_child_above_sibling(box, null);
        }
    }

    animate_with(window: ShellWindow, x: number, y: number) {
        if (this.tracked?.kind === 1 && Ecs.entity_eq(this.tracked.entity, window.entity)) {
            for (const hint_actor of this.border) {
                Tweener.add(hint_actor, { x, y, duration: 149, mode: null });
                Tweener.on_actor_tweened(hint_actor, () => {
                    this.update_overlay(window.meta.get_frame_rect());
                });
            }
        }
    }

    hide() {
        for (const box of this.border) {
            box.hide();
            box.visible = false;
        }
    }

    is_tracking(entity: Entity): boolean {
        if (!this.tracked || this.tracked.kind !== 1) return false;
        return this.tracked ? Ecs.entity_eq(entity, this.tracked.entity) : false;
    }

    position_changed(window: ShellWindow): void {
        if (window.is_maximized()) {
            this.hide();
        } else {
            this.show();
            this.update_overlay(window.meta.get_frame_rect());
        }
    }

    show() {
        for (const box of this.border) {
            box.visible = true;
            box.show();
        }
    }

    restack(actor: Clutter.Actor) {
        for (const box of this.border) {
            global.window_group.set_child_above_sibling(box, actor);
        }
    }

    stack_changed(stack: Stack) {
        if (!stack.destroyed) this.update_overlay(stack.container);
    }

    track_stack(stack: Stack) {
        this.disconnect_signals();

        this.tracked = {
            kind: 2,
            stack,
            sources: [stack.container.connect('allocation-changed', () => this.stack_changed(stack))],
        };

        this.update_overlay(stack.container);
        this.restack(stack.container);
    }

    track_window(ext: Ext, window: ShellWindow) {
        if (ext.auto_tiler && window.stack !== null) {
            const stack = ext.auto_tiler.forest.stacks.get(window.stack);
            if (stack) {
                this.track_stack(stack);
                return;
            }
        }

        this.disconnect_signals();

        if (this.tracked) {
            if (this.tracked.kind === 1 && Ecs.entity_eq(this.tracked.entity, window.entity)) {
                return;
            }

            this.untrack();
        }

        const meta = window.meta;
        if (meta.is_skip_taskbar()) return

        const actor = meta.get_compositor_private();
        if (!actor) return;

        const parent = actor.get_parent();

        if (parent) {
            this.tracked = {
                kind: 1,
                entity: window.entity,
                meta,
                parent: parent,
                sources: [
                    meta.connect('size-changed', () => this.position_changed(window)),
                    meta.connect('position-changed', () => this.position_changed(window))
                ]
            };

            this.tracking = GLib.idle_add(GLib.PRIORITY_LOW, () => {
                this.tracking = null;
                this.update_overlay(window.meta.get_frame_rect());

                this.show();

                return false;
            });
        }

        this.restack(actor);
    }

    untrack() {
        this.disconnect_signals();

        this.hide();

        if (this.tracked) {
            let object = null;
            if (this.tracked.kind === 1) {
                object = this.tracked.meta;
            } else if (!this.tracked.stack.destroyed) {
                object = this.tracked.stack.container;
            }

            if (object) for (const s of this.tracked.sources) object.disconnect(s);

            this.tracked = null;
        }
    }

    update_overlay(rect: Rectangular) {
        const width = 3 * this.dpi;

        const [w, n, e, s] = this.border;

        w.x = rect.x - width;
        w.y = rect.y;
        w.width = width;
        w.height = rect.height;

        e.x = rect.x + rect.width;
        e.y = rect.y;
        e.width = width;
        e.height = rect.height;

        n.x = rect.x - width;
        n.y = rect.y - width;
        n.width = (2 * width) + rect.width;
        n.height = width;

        s.x = rect.x - width;
        s.y = rect.y + rect.height;
        s.width = (2 * width) + rect.width;
        s.height = width;
    }

    destroy() {
        this.untrack();

        for (const box of this.border) {
            global.window_group.remove_child(box);
        }
    }

    disconnect_signals() {
        if (this.tracking) {
            GLib.source_remove(this.tracking);
            this.tracking = null;
        }
    }
}
