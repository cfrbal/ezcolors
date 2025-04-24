# ezcolors

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
<!-- Add other badges if you set up CI, PyPI etc. -->
<!-- e.g., [![Build Status](...)](...) -->
<!-- e.g., [![PyPI version](...)](...) -->

A simple, lightweight Python module for adding ANSI color and style codes to terminal output with minimal effort and zero dependencies.

Color your prints and terminal logs in an easy, modular, and straightforward way!

## Development Approach: Code Generation

This library uses a **build-time code generation** approach. Instead of generating functions dynamically every time the module is imported (runtime metaprogramming), a generator script (`tools/gen_implementation.py`) reads ANSI code definitions from a central file (`tools/_ezcolors_defs.py`) and creates several static files:

1.  **`src/ezcolors.py`:** The main module containing explicitly defined Python functions (like `blue()`, `bold()`, etc.) for each code. This is the file users import.
2.  **`src/ezcolors.pyi`:** A stub file providing type hints for all generated functions, enabling excellent IDE support (autocompletion, type checking) and linting.
3.  **`src/__init__.py`:** Defines the package and its public API via `__all__`.
4.  **`test/functions_to_test_data.py`:** Automatically generates a list of functions to be tested, ensuring the test suite stays synchronized with the generated code.

**Advantages of this approach:**

*   **Static Analysis Friendly:** Linters (like Pylint, Flake8) and type checkers (like MyPy, Pylance/Pyright) can perfectly understand the code, providing accurate feedback and preventing errors.
*   **Excellent IDE Support:** Autocompletion, type hints, and function signature help work reliably in editors like VS Code and PyCharm.
*   **Runtime Performance:** No overhead from runtime function generation during import. The code is plain, efficient Python.
*   **Clarity & Debugging:** The generated `src/ezcolors.py` is standard Python code, making it easier to read, understand, and debug if needed.
*   **Maintainability:** Adding new styles/colors requires editing only one definition file and re-running the generator.
*   **Robust Testing:** Tests verify the behavior of statically defined functions, and the test parametrization is kept up-to-date automatically.

## Features

*   **Easy to Use:** Simple function calls like `blue("text")` or `bold(warning("message"))`.
*   **Zero Dependencies:** Uses only standard Python features (apart from development tools like `pytest`).
*   **Easy Maintenance via Code Generation:** Add new styles/colors easily by editing the definitions and running the generator.
*   **Comprehensive Codes:** Includes common styles, standard foreground/background colors, and bright foreground/background colors.
*   **Type Hinted:** Provides `.pyi` stub files for excellent static analysis and IDE integration.
*   **Manual Reset Constant:** Provides `ENDC` for manual terminal state resets.

## Installation

**Option 1: Install from Local Clone (Recommended for Development/Contribution)**

This method installs the package in "editable" mode.

1.  **Clone the repository:**
    ```bash
    # Replace with your actual repo URL if different
    git clone https://github.com/cfrbal/ezcolors.git
    cd ezcolors
    ```
2.  **(Optional but Recommended) Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```
3.  **Install dependencies (including pytest for testing):**
    ```bash
    # Assuming you add pytest to requirements-dev.txt or similar
    # pip install -r requirements-dev.txt
    # OR just install pytest directly for now:
    pip install pytest
    ```
4.  **Install `ezcolors` in editable mode:**
    ```bash
    pip install -e .
    ```
    Now you can `import ezcolors` or `from ezcolors import ...` in your Python scripts within this environment.

**Option 2: Install from PyPI**

*(Note: This requires packaging and uploading the project to the Python Package Index first.)*

```bash
# pip install ezcolors # (Command once available on PyPI)
```

## Basic Usage

Import the desired color or style functions and wrap your strings:

```python
from ezcolors import blue, bold, warning, green, fail
from ezcolors import blue, bold, warning, green, fail

# Basic coloring
print(blue("This text is blue."))
print(blue("This text is blue."))
print(warning("This is a warning message."))

# Nesting styles
print(bold(fail("This is a bold failure message!")))

# Use within f-strings
status = "OK"
record_id = 123
print(f"Processing record {bold(record_id)}: Status = {green(status)}") # 'green' is an alias

# Use directly in logging (see Considerations below)
import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.warning(f"Could not process file: {fail('file_not_found.txt')}")
```

## Adding New Styles/Colors (Development)

To add a new color or style:

1.  **Edit the Definitions:** Open the file `tools/_ezcolors_defs.py`.
2.  **Add the Code:** Inside the `_ezcolors_codes` class, add a new class attribute in the format:
    ```python
    # Example: Adding an ORANGE color (using 256-color code approximation)
    ORANGE = '\033[38;5;208m'
    # Example: Adding double underline (not widely supported)
    DOUBLE_UNDERLINE = '\033[21m'
    ```
    Use uppercase names for the constants. Ensure the ANSI code string is correct.
3.  **Run the Generator:** From the project's root directory, run the generation script:
    ```bash
    python tools/gen_implementation.py
    ```
    This will update `src/ezcolors.py`, `src/ezcolors.pyi`, `src/__init__.py`, and `test/functions_to_test_data.py`.
4.  **Commit Changes:** If contributing to expand the available styles, add the modified `_ezcolors_defs.py` **and all the generated files** (`src/*`, `test/functions_to_test_data.py`) to your Git commit.

## Running Tests

Ensure you have installed the package editably (see Installation) and installed `pytest`.

From the root directory of the repository, run:

```bash
pytest
```
The tests use the automatically generated `test/functions_to_test_data.py` to ensure all generated functions are tested.

## Available Functions and Constants

The module contains explicitly defined functions for the following styles and colors (generated from `tools/_ezcolors_defs.py`). You can import any of these directly:Add the modified `_ezcolors_defs.py` **and all the generated files** (`src/*`, `test/functions_to_test_data.py`) to your Git commit.

**Styles:**

*   `bold`
*   `dim`
*   `italic` _(Terminal support varies)_
*   `underline`
*   `blink` _(Terminal support varies)_
*   `blink_rapid` _(Terminal support varies)_
*   `inverse` _(Swaps foreground/background)_
*   `hidden` _(Not generally useful for display)_
*   `strikethrough` _(Terminal support varies)_

**Foreground Colors (Standard):**

*   `fg_black`
*   `fg_red`
*   `fg_green`
*   `fg_yellow`
*   `fg_blue`
*   `fg_magenta`
*   `fg_cyan`
*   `fg_white`

**Background Colors (Standard):**

*   `bg_black`
*   `bg_red`
*   `bg_green`
*   `bg_yellow`
*   `bg_blue`
*   `bg_magenta`
*   `bg_cyan`
*   `bg_white`

**Foreground Colors (Bright/High Intensity):**

*   `fg_bright_black` _(often Gray)_
*   `fg_bright_red`
*   `fg_bright_green`
*   `fg_bright_yellow`
*   `fg_bright_blue`
*   `fg_bright_magenta`
*   `fg_bright_cyan`
*   `fg_bright_white`

**Background Colors (Bright/High Intensity):**

*   `bg_bright_black` _(often Gray)_
*   `bg_bright_red`
*   `bg_bright_green`
*   `bg_bright_yellow`
*   `bg_bright_blue`
*   `bg_bright_magenta`
*   `bg_bright_cyan`
*   `bg_bright_white`

**Semantic Aliases (Convenience Functions):**

*(These are generated by stripping the `OK` prefix from constants like `OKBLUE` and point to the corresponding bright colors)*

*   `header` _(Bright Magenta)_
*   `blue` _(Bright Blue)_
*   `cyan` _(Bright Cyan)_
*   `green` _(Bright Green)_
*   `blue` _(Bright Blue)_
*   `cyan` _(Bright Cyan)_
*   `green` _(Bright Green)_
*   `warning` _(Bright Yellow)_
*   `fail` _(Bright Red)_

**Reset Constant:**

*   `ENDC`: The ANSI code (`\033[0m`) to reset all attributes. The generated functions add this automatically, but it's exposed for manual use.

## Advanced Usage and Considerations
### Manual Control with `ENDC`

While functions automatically append the reset code, you might need `ENDC` for manual construction or multi-line styling:

```python
from ezcolors import bold, green, ENDC
from ezcolors import bold, green, ENDC

print(bold("Important section starts...")) # Manually start bold
print(" - Detail 1")
print(f" - Status: {green('All Good')}") # green() resets automatically
print(f" - Status: {green('All Good')}") # green() resets automatically
print(bold(" - More bold details"))       # Need to re-apply bold
print("Section ends." + ENDC)             # Manually reset at the very end
```

### Non-Terminal Output (Files, Pipes)

`ezcolors` does **not** automatically detect if output is going to a file or pipe. Raw ANSI codes will be written to non-terminal outputs. Check `sys.stdout.isatty()` manually if needed:

```python
import sys
from ezcolors import blue

text = "Hello"
if sys.stdout.isatty():
    print(blue(text))
    print(blue(text))
else:
    print(text)
```

Consider libraries like `colorama` or `rich` for more advanced handling.

### Terminal Compatibility

ANSI codes work well on modern terminals (Linux, macOS, Win10/11+). Older Windows `cmd.exe` may need `colorama`. Style support (`italic`, `blink`) varies.

### No 256-Color or TrueColor Support (by default)

The default definitions focus on basic 16 colors/styles. While you *could* add 256/TrueColor codes to `_ezcolors_defs.py` and regenerate, the primary focus is simplicity.

## Contributing

Contributions are welcome! Feel free to submit issues for bugs or suggestions, or pull requests for improvements (especially to the generator or tests). Please ensure you run the generator (`python tools/gen_implementation.py`) and tests (`pytest`) before submitting a PR involving code changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```