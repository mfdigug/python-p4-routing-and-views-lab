#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<string:somewords>')
def print_string(somewords):
    print(f"{somewords}")
    return f"{somewords}"


@app.route('/count/<int:somenumbers>')
def count(somenumbers):
    count = f''
    for num in range(somenumbers):
        count += f"{num}\n"
    return count


@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == "+":
        return str(num1 + num2)
    elif operation == "-":
        return str(num1 - num2)
    elif operation == "*":
        return str(num1 * num2)
    elif operation == "div":
        return str(num1 / num2)
    elif operation == "%":
        return str(num1 % num2)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
