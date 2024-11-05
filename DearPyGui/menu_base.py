# clarifey made the frameless dpg window, i modified it to work much better - dementia enjoyer

import dearpygui.dearpygui as dear_imgui;
import os;

dear_imgui.create_context();
dear_imgui.setup_dearpygui();

class ui:
    width = 400;
    height = 250;
    dragging = False;

class library: # feel free to create functions inside of this class which can be used for custom menu styling
    viewport = dear_imgui.create_viewport(title=" ", width = ui.width, height = ui.height, decorated = False, resizable = True);
    window = dear_imgui.window(label="dementiahaxx", width = ui.width, height = ui.height, no_collapse = True, no_move = True, no_resize = False, tag = "dementiahaxx_window", on_close = lambda: os._exit(0));

class ui_callbacks:
    global ui;

    def drag_callback_down(sender, data):
        if dear_imgui.is_mouse_button_down(0):
            if -2 <= (data[1]) <= 13:
                ui.dragging = True
        else:
            ui.dragging = False

    def drag_callback(sender, data):
        if ui.dragging:
            current_position = dear_imgui.get_viewport_pos();
    
            x = data[1];
            y = data[2];
    
            dear_imgui.configure_viewport(library.viewport, x_pos = (current_position[0] + x), y_pos = (current_position[1] + y), width = ui.width, height = ui.height);
    
    def resize_callback(sender, data):
        window_width = dear_imgui.get_item_width("dementiahaxx_window");
        window_height = dear_imgui.get_item_height("dementiahaxx_window");
    
        if (window_height > 1 and window_height > 1):
            dear_imgui.configure_viewport(library.viewport, width = window_width, height = (window_height + 0.9));
 
with library.window as window:
    dear_imgui.add_text("dasdasdas");

with dear_imgui.handler_registry():
    dear_imgui.add_mouse_drag_handler(0, callback = ui_callbacks.drag_callback);
    dear_imgui.add_mouse_move_handler(callback = ui_callbacks.drag_callback_down);
    dear_imgui.add_mouse_down_handler(callback = ui_callbacks.resize_callback);

dear_imgui.show_viewport();
dear_imgui.start_dearpygui();
dear_imgui.destroy_context();
