# ezcolors

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple, lightweight Python module for adding ANSI color and style codes to terminal output with minimal effort and zero dependencies.

Color your prints and terminal logs in an easy, modular, and straightforward way!

## Why Metaprogramming?

This module uses metaprogramming to dynamically generate the color/style functions from a list of ANSI codes. This was partly an exploration of Python's dynamic features, but it also makes adding new styles very simple – just add the code to the internal list, and the corresponding function becomes available automatically.

## Features

*   **Easy to Use:** Simple function calls like `okblue("text")` or `bold(warning("message"))`.
*   **Zero Dependencies:** Uses only standard Python features.
*   **Dynamic Generation:** Functions are automatically generated from defined ANSI codes, making extension easy.
*   **Comprehensive Codes:** Includes common styles, standard foreground/background colors, and bright foreground/background colors.
*   **Manual Reset:** Provides the `ENDC` constant for manual terminal state resets.

## Installation

There are a couple of ways to use `ezcolors`:

**Option 1: Install from Local Clone (Recommended for Development)**

This method installs the package in "editable" mode, meaning changes you make to the source code are immediately reflected without reinstalling.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/cfrbal/ezcolors.git
    cd ezcolors
    ```
2.  **(Optional but Recommended) Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```
3.  **Install in editable mode:**
    ```bash
    pip install -e .
    ```
    Now you can `import ezcolors` or `from ezcolors import ...` in your Python scripts within this environment.

4. **Run some tests?**

Once installed, run from the root of this repository:
```
pytest
```

**Option 2: Direct Copy**

For very simple use cases, you can simply place the `src/ezcolors.py` file directly into your project directory or another location included in your Python path (`sys.path`). This is less maintainable if the `ezcolors` code is updated.

**Option 3: Install from PyPI**

Not available as of yet.

```bash
# pip install ezcolors # (Command once available on PyPI)
```

## Basic Usage

Import the desired color or style functions and wrap your strings:

```python
from ezcolors import okblue, bold, warning, okgreen, fail

# Basic coloring
print(okblue("This text is blue."))
print(warning("This is a warning message."))

# Nesting styles
print(bold(fail("This is a bold failure message!")))

# Use within f-strings
status = "OK"
record_id = 123
# Assuming 'okgreen' is generated (check your Available Functions list)
print(f"Processing record {bold(record_id)}: Status = {okgreen(status)}")

# Use directly in logging (see Considerations below)
import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.warning(f"Could not process file: {fail('file_not_found.txt')}")
```

## Available Functions and Constants

The module automatically generates functions for the following styles and colors based on standard ANSI codes. You can import any of these directly:

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

*(These point to some of the bright colors above)*

*   `header` _(Bright Magenta)_
*   `okblue` _(Bright Blue)_
*   `okcyan` _(Bright Cyan)_
*   `okgreen` _(Bright Green)_
*   `warning` _(Bright Yellow)_
*   `fail` _(Bright Red)_

**Reset Constant:**

*   `ENDC`: The ANSI code (`\033[0m`) to reset all attributes. The generated functions add this automatically, but it's exposed for manual use.

## Advanced Usage and Considerations
### Debugging & Introspection

When running the `ezcolors.py` script directly from the command line, you can inspect the final generated namespace (functions, constants, etc.) using the `--debug` flag. This uses the `debug_utils.py` helper script.

**Purpose:**

*   Lists all non-internal names available in the module after generation.
*   Shows the type of each item.
*   Safely displays the first line of function docstrings.
*   Sanitizes output by replacing raw ANSI escape codes with `<ESC>` to avoid messing up your terminal.

**How to Use:**

1.  Navigate to this repository's root directory in the terminal.
2.  Ensure your environment is set up (e.g., virtual environment activated, package installed with `pip install -e .`).
3.  Run the ezcolor.py script using `python` with the `--debug` flag:


### Manual Control with `ENDC`

While functions automatically append the reset code, you might need `ENDC` for manual construction or multi-line styling:

```python
from ezcolors import bold, okgreen, ENDC

print(bold("Important section starts...")) # Manually start bold
print(" - Detail 1")
print(f" - Status: {okgreen('All Good')}") # okgreen() resets automatically
print(bold(" - More bold details"))       # Need to re-apply bold
print("Section ends." + ENDC)             # Manually reset at the very end
```

### Non-Terminal Output (Files, Pipes)

`ezcolors` does **not** automatically detect if output is going to a file or pipe (i.e., not an interactive terminal). In such cases, the raw ANSI codes (e.g., `\033[94mblue\033[0m`) will be written to the output.

If you need clean output in files, you must add checks manually:

```python
import sys
from ezcolors import okblue # Use the actual function name

text = "Hello"
if sys.stdout.isatty():
    print(okblue(text))
else:
    print(text)
```

Consider using a more feature-rich library like `colorama` (for cross-platform Windows activation) or `rich` if automatic detection or advanced features are required.

### Terminal Compatibility

ANSI escape codes are well-supported on modern Linux, macOS, and Windows 10/11 terminals. Older Windows command prompts (`cmd.exe`) might require libraries like `colorama` (`colorama.init()`) to enable ANSI interpretation. Some specific styles (like `italic`, `blink`) may not be supported by all terminal emulators.

### No 256-Color or TrueColor Support

This module focuses on the basic 16 ANSI colors and styles. It does not include support for 256-color palettes or TrueColor (RGB) escape codes.

## Contributing

Contributions are welcome, although the core functionality is quite simple. Feel free to submit issues for bugs or suggestions, or pull requests for improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

