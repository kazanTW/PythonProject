from __future__ import annotations
from functools import partial
from typing import Literal

from display import Display


class App():
    def __init__(self, display: Display):
        self.display = display

        self.display.on_press('AC', self.on_ac_pressed)
        self.display.on_press('DEL', self.on_del_pressed)
        self.display.on_press('=', self.on_equal_pressed)
        self.display.on_press('.', self.on_dot_pressed)
        self.display.on_press('+/-', self.on_plusminus_pressed)

        for op in ['%', '+', '-', 'x', '/']:
            self.display.on_press(op, partial(self.on_op_pressed, op))
        for num in range(10):
            # bind the first argument to `num`
            self.display.on_press(str(num), partial(
                self.on_number_pressed, str(num)))

        self.display.on_keypress('<Control-c>', self.on_ctrl_c_pressed)
        
        self.state: Literal['init'] | Literal['input'] = 'init'
        self.input_string = ''
        self.num = 0
        self.op: str | None = None

        # display 0 initially
        self.update_display()

    def update_display(self):
        self.display.display_text(self.get_display_string())

    def get_display_string(self):
        if self.state == 'init':
            return str(self.num)
        else:
            if len(self.input_string) == 0:
                return '0'
            else:
                return self.input_string

    def on_op_pressed(self, op: str, *args, **kwargs):
        print(f'op {op} is pressed')
        print(args, kwargs)
        if self.state == 'init':
            self.op = op
        else:
            # perform last op
            if self.op is None:
                self.num = float(self.input_string)
            else:
                self.num = perform_op(
                    self.op, self.num, float(self.input_string))
            self.input_string = str(self.num)

            self.state = 'init'
            self.op = op
        self.update_display()

    def on_number_pressed(self, num: str, *args, **kwargs):
        print(f'number {num} is pressed')
        print(args, kwargs)
        if is_float(self.input_string + str(num)):
            if self.state == 'init':
                self.input_string = ''
            self.state = 'input'
            self.input_string += num
            self.update_display()
        else:
            print(f'Input {num} not allowed here')

    def on_ac_pressed(self, *args, **kwargs):
        print('ac is pressed')
        print(args, kwargs)
        self.input_string = ''
        self.num = 0
        self.op = None
        self.update_display()

    def on_del_pressed(self, *args, **kwargs):
        print('del is pressed')
        print(args, kwargs)
        if self.state == 'input':
            if len(self.input_string) != 0:
                self.input_string = self.input_string[1:]
            self.update_display()
        else:
            self.input_string = ''
            self.num = 0
            self.op = None
            self.update_display()

    def on_equal_pressed(self, *args, **kwargs):
        print('= is pressed')
        print(args, kwargs)
        # almost identical to on_op_pressed
        # perform last op
        if self.op is None:
            self.num = float(self.input_string)
        else:
            self.num = perform_op(self.op, self.num, float(self.input_string))
        self.input_string = str(self.num)

        self.state = 'init'
        self.op = None
        self.update_display()

    def on_dot_pressed(self, *args, **kwargs):
        print(f'. is pressed')
        print(args, kwargs)
        if is_float(self.input_string + '.'):
            self.state = 'input'
            self.input_string += '.'
            self.update_display()
        else:
            print(f'Input . not allowed here')

    def on_plusminus_pressed(self, *args, **kwargs):
        print('+/- is pressed')
        print(args, kwargs)
        if self.state == 'init':
            self.num = -self.num
            self.input_string = str(self.num)
        else:
            if '-' in self.input_string:
                self.input_string = self.input_string[1:]
            else:
                self.input_string = '-' + self.input_string
        self.update_display()

    def on_ctrl_c_pressed(self, *args, **kwargs):
        print('ctrl_c is pressed')
        print(args, kwargs)
        self.display.copy_to_clipboard(self.get_display_string())
        
    def run(self):
        self.display.run()


def is_float(string: str) -> bool:
    try:
        float(string)
        return True
    except ValueError:
        return False

def perform_op(op: str, num_1: float, num_2: float) -> float:
    if op == '+':
        return num_1 + num_2
    elif op == '-':
        return num_1 - num_2
    elif op == 'x':
        return num_1 * num_2
    elif op == '/':
        return num_1 / num_2
    elif op == '%':
        return num_1 % num_2
    else:
        raise ValueError(f'Unknown operator "{op}"')


if __name__ == '__main__':
    display = Display()
    app = App(display)
    app.run()
