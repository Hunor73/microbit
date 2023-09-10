def on_button_pressed_a():
    basic.clear_screen()
    basic.show_icon(IconNames.HAPPY)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.clear_screen()
    basic.show_icon(IconNames.SAD)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_touched():
    basic.clear_screen()
    basic.show_icon(IconNames.CONFUSED)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

for index in range(4):
    basic.clear_screen()
    basic.pause(500)
    basic.show_icon(IconNames.HEART)