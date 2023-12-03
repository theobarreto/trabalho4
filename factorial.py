#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 20:00:46 2023

@author: leonardosilva
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

def factorial(n):
    if n < 0:
        return 'Entrada inválida'
    else:
        i, count = 1, 1
        while count <= n:
            i *= count
            count += 1
        return i

@app.route('/factorial', methods=['POST'])
def calculate_factorial():
    try:
        data = request.get_json()
        number = int(data['number'])

        result = factorial(number)

        return jsonify({'result': result})
    except (KeyError, ValueError):
        return jsonify({'error': 'Entrada inválida'}), 400

if __name__ == '__main__':
    app.run(debug=True)
