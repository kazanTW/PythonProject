#!/usr/bin/python

import sys


def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    else:
        raise ValueError('Invalid operator {}'.format(op))


def prompt_and_calculate():
    n1, opt, n2 = input(
        "Enter a two-number operation(Enter 0 and 0 to end): ").split()
    return calculate(float(n1), float(n2), opt)


if __name__ == '__main__':
    print('Easy Calculator v1.0_py3')
    print('Copyright © 2021 Kazan All Rights Reserved.')
    print()

    while True:
        try:
            output = prompt_and_calculate()
            print(output)
        except ValueError as e:
            print(e)
        except ZeroDivisionError as e:
            print('Invalid input. Cannot divide by 0.')
        except EOFError:
            print('\nThanks for using.')
            sys.exit(0)
