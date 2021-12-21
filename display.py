import tkinter as tk
import tkinter.font as font


BUTTON_NAMES = ['AC', 'DEL', '+/-', '/', '7', '8',
                '9', 'x', '4', '5', '6', '-', '1', '2', '3', '+', '%', '0', '.', '=']


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

    def display_text(self, text: str):
        self.output_display.configure(text=text)

    def on_press(self, button_name, callback):
        self.buttons[button_name].bind('<Button-1>', callback)
        for key_name in button_name_to_key_name(button_name):
            self.root.bind(key_name, callback)

    def on_keypress(self, keyname, callback):
        self.root.bind(keyname, callback)

    def copy_to_clipboard(self, text: str):
        self.root.clipboard_clear()
        self.root.clipboard_append(text)


def button_name_to_key_name(name):
    mapping = {
        'AC': ['c'],
        'DEL': ['<BackSpace>', '<Delete>'],
        '+/-': ['!'],
        '=': ['=', '<Return>'],
    }
    if name in mapping.keys():
        return mapping[name]
    else:
        return [name]