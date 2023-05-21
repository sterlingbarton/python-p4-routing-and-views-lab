#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<string:string>')
def print_string(string):
    print(string)
    return string


@app.route('/count/<int:int>')
def count(int):
    count = f''
    for i in range(int):
        count += f'{i}\n'
    return count


@app.route('/math/<int:num1>/<string:operator>/<int:num2>')
def math(num1, operator, num2):
    if operator == '+':
        return str(num1 + num2)
    elif operator == '-':
        return str(num1 - num2)
    elif operator == '*':
        return str(num1 * num2)
    elif operator == 'div':
        return str(num1 / num2)
    elif operator == '%':
        return str(num1 % num2)

    return 'Operation not recognized. Please use one of the following: + - * div %'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
