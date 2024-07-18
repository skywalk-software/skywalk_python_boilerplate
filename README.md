# Skywalk Python Boilerplate

This is a boilerplate project for Python-based projects at Skywalk.

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/skywalk/skywalk_python_boilerplate.git
   cd skywalk_python_boilerplate
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Install the pre-commit hooks:
   ```
   pre-commit install
   ```

5. Copy the `.env.example` file to `.env` and fill in your secret keys and API tokens.

## Running the Project

To run the example script:

```
python scripts/example_script.py
```

## Running Tests

To run the tests:

```
pytest
```

## Environment

This project was developed and tested with:

- Python 3.8
- PyCharm 2021.1

## Code Style

This project follows the PEP 8 style guide. We use Black for code formatting and Flake8 for linting. These are enforced
using pre-commit hooks.

To manually run the style checks:

```
black .
flake8 --config=.flake8
```

## Contributing

Please make sure to run the pre-commit hooks before committing your changes. If you need to bypass the hooks for any
reason, you can use the `--no-verify` flag with your git commit command.
