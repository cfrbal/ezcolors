# ezcolors

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple, lightweight Python module for adding ANSI color and style codes to terminal output with minimal effort and zero dependencies.

Color your prints/terminal logs in the most easy, modular, straightforward way possible!

## Why are there no explicit function declarations?

Honestly? I just wanted to play around with some metaprogramming. Is it the best solution? Maybe not. Was it fun? YES. ç

Either way, I provided a function to generate all of the declarations, in case you want a more "traditional" approach.

## Features

*   **Easy to Use:** Simple function calls like `blue("text")` or `bold(warning("message"))`.
*   **Zero Dependencies:** Uses only standard Python features.
*   **Dynamic Generation:** Functions are automatically generated from defined ANSI codes, making extension easy.
*   **Comprehensive Codes:** Includes common styles, standard foreground/background colors, and bright foreground/background colors.
*   **Manual Reset:** Provides the `ENDC` constant for manual terminal state resets.

## Installation

**Option 1: Direct Copy**

Simply place the `ezcolors.py` file in your project directory or a location included in your Python path (`sys.path`).

**Option 2: Install via pip (NOT YET SUPPORTED)**

## Basic Usage

Import the desired color or style functions and wrap your strings:
`
from ezcolors import okblue, bold, warning, okgreen, fail
`
# Basic coloring
`
print(okblue("This text is blue."))
print(warning("This is a warning message."))
`
# Nesting styles
`
print(bold(fail("This is a bold failure message!")))
`
# Use within f-strings
`
status = "OK"
record_id = 123
print(f"Processing record {bold(record_id)}: Status = {green(status)}")
`
# Use directly in logging (see Considerations below)
`
import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.warning(f"Could not process file: {fail('file_not_found.txt')}")
`
# Code
The module automatically generates functions for the following styles and colors. You can import any of these directly:

Styles:

bold(text)

dim(text)

italic(text) (Terminal support varies)

underline(text)

blink(text) (Terminal support varies)

blink_rapid(text) (Terminal support varies)

inverse(text) (Swaps foreground/background)

hidden(text) (Not generally useful for display)

strikethrough(text) (Terminal support varies)

Foreground Colors (Standard):

fg_black(text)

fg_red(text)

fg_green(text)

fg_yellow(text)

fg_blue(text)

fg_magenta(text)

fg_cyan(text)

fg_white(text)

Background Colors (Standard):

bg_black(text)

bg_red(text)

bg_green(text)

bg_yellow(text)

bg_blue(text)

bg_magenta(text)

bg_cyan(text)

bg_white(text)

Foreground Colors (Bright/High Intensity):

fg_bright_black(text) (often Gray)

fg_bright_red(text)

fg_bright_green(text)

fg_bright_yellow(text)

fg_bright_blue(text)

fg_bright_magenta(text)

fg_bright_cyan(text)

fg_bright_white(text)

Background Colors (Bright/High Intensity):

bg_bright_black(text) (often Gray)

bg_bright_red(text)

bg_bright_green(text)

bg_bright_yellow(text)

bg_bright_blue(text)

bg_bright_magenta(text)

bg_bright_cyan(text)

bg_bright_white(text)

Semantic Aliases (Convenience Functions):

These point to some of the bright colors above:

header(text) (Bright Magenta)

okblue(text) (Bright Blue)

okcyan(text) (Bright Cyan)

okgreen(text) (Bright Green)

warning(text) (Bright Yellow)

fail(text) (Bright Red)

Reset Constant:

ENDC: The ANSI code (\033[0m) to reset all attributes. The generated functions add this automatically, but it's exposed for manual use.

Advanced Usage and Considerations
Manual Control with ENDC

While functions automatically append the reset code, you might need ENDC for manual construction or multi-line styling:
`
from ezcolors import bold, okgreen, ENDC

print(bold("Important section starts...")) # Manually start bold
print(" - Detail 1")
print(f" - Status: {green('All Good')}") # green() resets automatically
print(bold(" - More bold details"))       # Need to re-apply bold
print("Section ends." + ENDC)             # Manually reset at the very end
`

ezcolors does not automatically detect if output is going to a file or pipe (i.e., not an interactive terminal). In such cases, the raw ANSI codes (e.g., \033[94mblue\033[0m) will be written to the output.

If you need clean output in files, you must add checks manually:
`
import sys
from ezcolors import blue

text = "Hello"
if sys.stdout.isatty():
    print(okblue(text))
else:
    print(text)
`

Consider using a more feature-rich library like colorama (for cross-platform Windows activation) or rich if automatic detection or advanced features are required.

Terminal Compatibility

ANSI escape codes are well-supported on modern Linux, macOS, and Windows 10/11 terminals. Older Windows command prompts (cmd.exe) might require libraries like colorama (colorama.init()) to enable ANSI interpretation. Some specific styles (like italic, blink) may not be supported by all terminal emulators.

No 256-Color or TrueColor Support

This module focuses on the basic 16 ANSI colors and styles. It does not include support for 256-color palettes or TrueColor (RGB) escape codes.

Contributing

Contributions are welcome although I don't think there's much to do. This library is ridiculously simple.

Please feel free to submit issues or pull requests. (Add more specific contribution guidelines if desired).

License

This project is licensed under the MIT License - see the LICENSE file for details (You'll need to create a LICENSE file, typically containing the MIT license text).

# Complete function list:
Name: bold                 | Type: function        | Doc: Wraps the input string with the 'BOLD' ANSI code (<ESC>[1m).
Name: dim                  | Type: function        | Doc: Wraps the input string with the 'DIM' ANSI code (<ESC>[2m).
Name: italic               | Type: function        | Doc: Wraps the input string with the 'ITALIC' ANSI code (<ESC>[3m).
Name: underline            | Type: function        | Doc: Wraps the input string with the 'UNDERLINE' ANSI code (<ESC>[4m).
Name: blink                | Type: function        | Doc: Wraps the input string with the 'BLINK' ANSI code (<ESC>[5m).
Name: blink_rapid          | Type: function        | Doc: Wraps the input string with the 'BLINK_RAPID' ANSI code (<ESC>[6m).
Name: inverse              | Type: function        | Doc: Wraps the input string with the 'INVERSE' ANSI code (<ESC>[7m).
Name: hidden               | Type: function        | Doc: Wraps the input string with the 'HIDDEN' ANSI code (<ESC>[8m).
Name: strikethrough        | Type: function        | Doc: Wraps the input string with the 'STRIKETHROUGH' ANSI code (<ESC>[9m).
Name: fg_black             | Type: function        | Doc: Wraps the input string with the 'FG_BLACK' ANSI code (<ESC>[30m).
Name: fg_red               | Type: function        | Doc: Wraps the input string with the 'FG_RED' ANSI code (<ESC>[31m).
Name: fg_green             | Type: function        | Doc: Wraps the input string with the 'FG_GREEN' ANSI code (<ESC>[32m).
Name: fg_yellow            | Type: function        | Doc: Wraps the input string with the 'FG_YELLOW' ANSI code (<ESC>[33m).
Name: fg_blue              | Type: function        | Doc: Wraps the input string with the 'FG_BLUE' ANSI code (<ESC>[34m).
Name: fg_magenta           | Type: function        | Doc: Wraps the input string with the 'FG_MAGENTA' ANSI code (<ESC>[35m).
Name: fg_cyan              | Type: function        | Doc: Wraps the input string with the 'FG_CYAN' ANSI code (<ESC>[36m).
Name: fg_white             | Type: function        | Doc: Wraps the input string with the 'FG_WHITE' ANSI code (<ESC>[37m).
Name: bg_black             | Type: function        | Doc: Wraps the input string with the 'BG_BLACK' ANSI code (<ESC>[40m).
Name: bg_red               | Type: function        | Doc: Wraps the input string with the 'BG_RED' ANSI code (<ESC>[41m).
Name: bg_green             | Type: function        | Doc: Wraps the input string with the 'BG_GREEN' ANSI code (<ESC>[42m).
Name: bg_yellow            | Type: function        | Doc: Wraps the input string with the 'BG_YELLOW' ANSI code (<ESC>[43m).
Name: bg_blue              | Type: function        | Doc: Wraps the input string with the 'BG_BLUE' ANSI code (<ESC>[44m).
Name: bg_magenta           | Type: function        | Doc: Wraps the input string with the 'BG_MAGENTA' ANSI code (<ESC>[45m).
Name: bg_cyan              | Type: function        | Doc: Wraps the input string with the 'BG_CYAN' ANSI code (<ESC>[46m).
Name: bg_white             | Type: function        | Doc: Wraps the input string with the 'BG_WHITE' ANSI code (<ESC>[47m).
Name: fg_bright_black      | Type: function        | Doc: Wraps the input string with the 'FG_BRIGHT_BLACK' ANSI code (<ESC>[90m).
Name: fg_bright_red        | Type: function        | Doc: Wraps the input string with the 'FG_BRIGHT_RED' ANSI code (<ESC>[91m).
Name: fg_bright_green      | Type: function        | Doc: Wraps the input string with the 'FG_BRIGHT_GREEN' ANSI code (<ESC>[92m).
Name: fg_bright_yellow     | Type: function        | Doc: Wraps the input string with the 'FG_BRIGHT_YELLOW' ANSI code (<ESC>[93m).
Name: fg_bright_blue       | Type: function        | Doc: Wraps the input string with the 'FG_BRIGHT_BLUE' ANSI code (<ESC>[94m).
Name: fg_bright_magenta    | Type: function        | Doc: Wraps the input string with the 'FG_BRIGHT_MAGENTA' ANSI code (<ESC>[95m).
Name: fg_bright_cyan       | Type: function        | Doc: Wraps the input string with the 'FG_BRIGHT_CYAN' ANSI code (<ESC>[96m).
Name: fg_bright_white      | Type: function        | Doc: Wraps the input string with the 'FG_BRIGHT_WHITE' ANSI code (<ESC>[97m).
Name: bg_bright_black      | Type: function        | Doc: Wraps the input string with the 'BG_BRIGHT_BLACK' ANSI code (<ESC>[100m).
Name: bg_bright_red        | Type: function        | Doc: Wraps the input string with the 'BG_BRIGHT_RED' ANSI code (<ESC>[101m).
Name: bg_bright_green      | Type: function        | Doc: Wraps the input string with the 'BG_BRIGHT_GREEN' ANSI code (<ESC>[102m).
Name: bg_bright_yellow     | Type: function        | Doc: Wraps the input string with the 'BG_BRIGHT_YELLOW' ANSI code (<ESC>[103m).
Name: bg_bright_blue       | Type: function        | Doc: Wraps the input string with the 'BG_BRIGHT_BLUE' ANSI code (<ESC>[104m).
Name: bg_bright_magenta    | Type: function        | Doc: Wraps the input string with the 'BG_BRIGHT_MAGENTA' ANSI code (<ESC>[105m).
Name: bg_bright_cyan       | Type: function        | Doc: Wraps the input string with the 'BG_BRIGHT_CYAN' ANSI code (<ESC>[106m).
Name: bg_bright_white      | Type: function        | Doc: Wraps the input string with the 'BG_BRIGHT_WHITE' ANSI code (<ESC>[107m).
Name: header               | Type: function        | Doc: Wraps the input string with the 'HEADER' ANSI code (<ESC>[95m).
Name: okblue               | Type: function        | Doc: Wraps the input string with the 'OKBLUE' ANSI code (<ESC>[94m).
Name: okcyan               | Type: function        | Doc: Wraps the input string with the 'OKCYAN' ANSI code (<ESC>[96m).
Name: okgreen              | Type: function        | Doc: Wraps the input string with the 'OKGREEN' ANSI code (<ESC>[92m).
Name: warning              | Type: function        | Doc: Wraps the input string with the 'WARNING' ANSI code (<ESC>[93m).
Name: fail                 | Type: function        | Doc: Wraps the input string with the 'FAIL' ANSI code (<ESC>[91m).
