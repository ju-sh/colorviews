# Contributing
Pull requests welcome!

If you spot any errors please create an issue :-)

This package uses the following for development:

| Package         | Purpose              |
| -------         | -------              |
| pytest          | Testing              |
| vulture         | Dead code detection  |
| mypy            | Static type checking |
| pylint & flake8 | Linting              |
| coverage        | Test coverage        |
| tox             | Test automation      |

Use the following command to install them.

    pip install -r development/requirements-dev.txt

## Tests
Make sure to add tests for any new piece of code using pytest and run the tests with

    pytest

## Dead code detection
Use vulture to check for dead code.

    tox -e vulture

## Static type checking
Use type annotations for every function definition and apply mypy for static type checking.

    tox -e mypy

## Linting
Use both pylint and flake8 for linting.

    tox -e pylint,flake8

## Test coverage
Ensure proper test coverage with coverage.py

    tox -e coverage

## All checks
Run all checks with

    tox
