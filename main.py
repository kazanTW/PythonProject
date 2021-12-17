from __future__ import annotations

import tkinter as tk
import tkinter.font as font
from functools import partial


class App():
    def __init__(self, display: Display):
        self.display = display
        self.display.on_press('AC', self.on_ac_pressed)
        self.display.on_press('DEL', self.on_del_pressed)
        self.display.on_press('%', self.on_percent_pressed)
        self.display.on_press('=', self.on_equal_pressed)
        self.display.on_press('.', self.on_dot_pressed)
        self.display.on_press('+', self.on_plus_pressed)
        self.display.on_press('-', self.on_minus_pressed)
        self.display.on_press('x', self.on_multiple_pressed)
        self.display.on_press('/', self.on_divide_pressed)
        self.display.on_press('+/-', self.on_positiveAndNegative_pressed)
        for num in range(10):
            # bind the first argument to `num`
            self.display.on_press(str(num), partial(
                self.on_number_pressed, num))

    def on_number_pressed(self, num, *args, **kwargs):
        print(f'number {num} is pressed')
        print(args, kwargs)

    def on_ac_pressed(self, *args, **kwargs):
        print('ac is pressed')
        print(args, kwargs)

    def on_del_pressed(self, *args, **kwargs):
        print('del is pressed')
        print(args, kwargs)

    def on_percent_pressed(self, *args, **kwargs):
        print('% is pressed')
        print(args, kwargs)

    def on_equal_pressed(self, *args, **kwargs):
        print('= is pressed')
        print(args, kwargs)

    def on_dot_pressed(self, *args, **kwargs):
        print('. is pressed')
        print(args, kwargs)
    
    def on_plus_pressed(self, *args, **kwargs):
        print('+ is pressed')
        print(args, kwargs)

    def on_minus_pressed(self, *args, **kwargs):
        print('- is pressed')
        print(args, kwargs)

    def on_multiple_pressed(self, *args, **kwargs):
        print('x is pressed')
        print(args, kwargs)
    
    def on_divide_pressed(self, *args, **kwargs):
        print('/ is pressed')
        print(args, kwargs)

    def on_positiveAndNegative_pressed(self, *args, **kwargs):
        print('+/- is pressed')
        print(args, kwargs)

    def run(self):
        self.display.run()


class Display():
    def __init__(self):
        OUTPUT_PADDING = 15

        root = tk.Tk()
        root.title('Easy Calculator')
        root.geometry('400x500')

        # make the keypad row expand
        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(0, weight=0)
        root.grid_rowconfigure(1, weight=1)

        # sub-frames
        top_frame = tk.Frame(root)
        top_frame.grid(row=0, column=0)

        keypad_frame = tk.Frame(root)
        keypad_frame.grid(row=1, column=0, sticky=tk.NSEW)

        # top frame children
        output_font = font.Font(size=20)
        output_display = tk.Label(top_frame, text='', font=output_font,
                                  justify='left', relief=tk.SUNKEN, bd=10, bg='white', width=40)
        output_display.pack(padx=OUTPUT_PADDING, pady=OUTPUT_PADDING)

        # keypad frame children
        buttons = self._create_buttons(keypad_frame)

        # make all rows / cols equaly expanded
        for col in range(4):
            keypad_frame.grid_columnconfigure(col, weight=1)
        for row in range(5):
            keypad_frame.grid_rowconfigure(row, weight=1)

        self.root = root
        self.top_frame = top_frame
        self.keypad = keypad_frame
        self.output_display = output_display
        self.buttons = buttons

    def _create_buttons(self, frame: tk.Frame) -> dict[str, tk.Button]:
        BUTTON_NAMES = ['AC', 'DEL', '+/-', '/', '7', '8',
                        '9', 'x', '4', '5', '6', '-', '1', '2', '3', '+', '%', '0', '.', '=']
        BTN_FONT = font.Font(size=20)

        buttons = {}
        for index, name in enumerate(BUTTON_NAMES):
            # for (row, column) in (0, 0), (0, 1), ..., (4, 3)
            row = index // 4
            column = index % 4
            button = tk.Button(frame, text=name, font=BTN_FONT)
            button.grid(row=row, column=column, sticky=tk.NSEW, padx=3, pady=3)
            buttons[name] = button

        return buttons

    def run(self):
        self.root.mainloop()

    def on_press(self, button_name, callback):
        self.buttons[button_name].bind('<Button-1>', callback)


if __name__ == '__main__':
    display = Display()
    app = App(display)
    app.run()
