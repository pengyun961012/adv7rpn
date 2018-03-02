#!/usr/bin/env python3

import operator
import click



operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    '%': operator.mod,
}
def calculate(debug,myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        if debug:
            print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def printer():
    print("This is a calculator!")

@click.command()
@click.option('--debug', '-d', is_flag=True, help='Print internal stack')
def main(debug):
    while True:
        result = calculate(debug,input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()
