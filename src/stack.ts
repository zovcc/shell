// @ts-ignore
const Me = imports.misc.extensionUtils.getCurrentExtension();

import type { Entity } from './ecs';
import type { Ext } from './extension';

import * as Ecs from 'ecs';
import * as Rect from 'rectangle';

const { St } = imports.gi;

interface Component {
    entity: Entity;
    button: St.Widget;
}

export class Stack {
    private container = new St.BoxLayout({
        style_class: 'pop-shell-stack-bg',
        vertical: true
    });

    private tabs = new St.BoxLayout({
        style_class: 'pop-shell-stack',
        x_expand: true
    });

    active: Entity;

    active_id: number = 0

    windows: Array<Component> = new Array();

    workspace: number;

    private restacker: SignalID = (global.display as GObject.Object).connect('restacked', () => this.restack());

    constructor(active: Entity, workspace: number) {
        this.active = active;
        this.workspace = workspace;

        global.window_group.insert_child_at_index(this.container, 1);
        global.window_group.add_child(this.tabs);
    }

    activate(entity: Entity) {
        this.active = entity;
        let id = 0;

        for (const component of this.windows) {
            let name;

            if (Ecs.entity_eq(entity, component.entity)) {
                this.active_id = id;
                name = 'pop-shell-tab-active';
            } else {
                name = 'pop-shell-tab-inactive';
            }

            component.button.set_style_class_name(name);
            id += 1;
        }

        this.restack();
    }

    clear() {
        for (const window of this.windows.splice(0)) {
            this.tabs.remove_child(window.button);
        }
    }

    destroy() {
        global.window_group.remove_child(this.container);
        global.window_group.remove_child(this.tabs);
        global.display.disconnect(this.restacker);
        this.container.destroy();
        this.tabs.destroy();
    }

    remove_tab(entity: Entity) {
        let idx = 0;
        for (const window of this.windows) {
            if (Ecs.entity_eq(window.entity, entity)) {
                this.tabs.remove_child(window.button);
                this.windows.splice(idx, 1);
                break
            }
        }
    }

    restack() {
        if (this.container.visible) {
            // Check if a fullscreen window is above our stack.
            const focused = global.display.get_focus_window() as (null | Meta.Window);
            if (focused) {
                const r = Rect.Rectangle.from_meta(focused.get_frame_rect());
                if (r.contains(this.container)) return;
            }

            // Place actors if it's found that we're not behind a fullscreen window
            global.window_group.set_child_at_index(this.container, 1);
            global.window_group.set_child_above_sibling(this.tabs, null);
        }
    }

    set_visible(visible: boolean) {
        if (visible) {
            this.container.show();
            this.container.visible = true;
            this.tabs.show();
            this.tabs.visible = true;
        } else {
            this.container.visible = false;
            this.container.hide();
            this.tabs.visible = false;
            this.tabs.hide();
        }
    }

    update_positions(_ext: Ext, dpi: number, rect: Rectangular) {
        const width = 4 * dpi;
        const tabs_height = width * 6;

        this.container.x = rect.x;
        this.container.y = rect.y - tabs_height;
        this.container.width = rect.width;
        this.container.height = tabs_height + rect.height;

        this.tabs.x = rect.x;
        this.tabs.y = this.container.y;
        this.tabs.height = tabs_height;
        this.tabs.width = rect.width;
    }

    update_tabs(ext: Ext, data: Array<[Entity, string]>) {
        this.clear();

        this.windows.splice(0);

        this.tabs.destroy_all_children();

        for (const [entity, label] of data) {
            const button: St.Widget = new St.Button({
                label,
                x_expand: true,
                style_class: Ecs.entity_eq(entity, this.active)
                    ? 'pop-shell-tab-active'
                    : 'pop-shell-tab-inactive'
            });

            // On click, raise the window to the top of the stack, and activate the window's tab
            button.connect('clicked', () => {
                const window = ext.windows.get(entity);
                if (window) {
                    const actor = window.meta.get_compositor_private();
                    if (actor) {
                        window.meta.raise();
                        window.meta.unminimize();
                        window.meta.activate(global.get_current_time());

                        global.window_group.set_child_above_sibling(actor, null);

                        for (const comp of this.windows) {
                            comp.button.set_style_class_name('pop-shell-tab-inactive');
                        }

                        button.set_style_class_name('pop-shell-tab-active');
                    } else {
                        this.remove_tab(entity);
                    }
                }
            });

            this.windows.push({ entity, button });
            this.tabs.add_actor(button);
        }
    }
}
