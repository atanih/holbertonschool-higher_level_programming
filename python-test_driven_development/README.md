# Python - Test-driven development

Holberton School project about test-driven development (TDD) in Python.

## Description

Each module in this directory implements a small function, documented with
docstrings and validated with tests written before the code itself.
The tests live in the tests/ folder: .txt files holding interactive
doctests and a .py file holding unittests.

## Requirements

* Ubuntu 20.04 LTS with python3 (version 3.8.5)
* All files are executable and start with #!/usr/bin/python3
* The code follows pycodestyle 2.7.*
* Every module and every function is documented

## Running the tests

    python3 -m doctest ./tests/*
    python3 -m unittest tests.6-max_integer_test

## Files

| File | Description |
| --- | --- |
| 0-add_integer.py | add_integer(a, b=98) adds 2 integers |
| 2-matrix_divided.py | matrix_divided(matrix, div) divides a matrix |
| 3-say_my_name.py | say_my_name(first_name, last_name="") prints a name |
| 4-print_square.py | print_square(size) prints a square of # |
| 5-text_indentation.py | text_indentation(text) indents a text |
| 6-max_integer.py | max_integer(list=[]) returns the biggest integer |
| tests/ | .txt doctests and the 6-max_integer_test.py unittest |

## Author

Antonio Torres Alvarado
