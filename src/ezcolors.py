import sys
import os
import argparse

# --- Global Color Configuration ---

# Check for common environment variables that might suggest disabling color
_NO_COLOR = 'NO_COLOR' in os.environ
_IS_DUMB_TERM = os.environ.get('TERM') == 'dumb'

# Check if stdout is a TTY and we haven't explicitly disabled color
# Default to True only if stdout is a TTY and NO_COLOR/dumb TERM isn't set.
_DEFAULT_ENABLE_STATE = sys.stdout.isatty() and not _NO_COLOR and not _IS_DUMB_TERM

COLORS_ENABLED = _DEFAULT_ENABLE_STATE

def enable_colors(check_stream=None):
    """
    Globally enables color output for ezcolors functions.

    Args:
        check_stream: If provided (e.g., sys.stdout or sys.stderr),
                      colors will only be enabled if check_stream.isatty()
                      is true (and NO_COLOR/TERM=dumb are not set).
                      If None, enables colors unconditionally.
    """
    global COLORS_ENABLED
    if check_stream:
        is_tty = hasattr(check_stream, 'isatty') and check_stream.isatty()
        COLORS_ENABLED = is_tty and not _NO_COLOR and not _IS_DUMB_TERM
    else:
        # # Allow forcing colors on, even if not a TTY or NO_COLOR is set
       COLORS_ENABLED = True

def disable_colors():
    """Globally disables color output for ezcolors functions."""
    global COLORS_ENABLED
    COLORS_ENABLED = False

# --- ANSI Code Definitions ---
class _ezcolors_codes:
    """Internal class to hold the ANSI escape codes."""
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    BLINK_RAPID = '\033[6m'
    INVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    STRIKETHROUGH = '\033[9m'
    FG_BLACK = '\033[30m'
    FG_RED = '\033[31m'
    FG_GREEN = '\033[32m'
    FG_YELLOW = '\033[33m'
    FG_BLUE = '\033[34m'
    FG_MAGENTA = '\033[35m'
    FG_CYAN = '\033[36m'
    FG_WHITE = '\033[37m'
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    FG_BRIGHT_BLACK = '\033[90m'
    FG_BRIGHT_RED = '\033[91m'
    FG_BRIGHT_GREEN = '\033[92m'
    FG_BRIGHT_YELLOW = '\033[93m'
    FG_BRIGHT_BLUE = '\033[94m'
    FG_BRIGHT_MAGENTA = '\033[95m'
    FG_BRIGHT_CYAN = '\033[96m'
    FG_BRIGHT_WHITE = '\033[97m'
    BG_BRIGHT_BLACK = '\033[100m'
    BG_BRIGHT_RED = '\033[101m'
    BG_BRIGHT_GREEN = '\033[102m'
    BG_BRIGHT_YELLOW = '\033[103m'
    BG_BRIGHT_BLUE = '\033[104m'
    BG_BRIGHT_MAGENTA = '\033[105m'
    BG_BRIGHT_CYAN = '\033[106m'
    BG_BRIGHT_WHITE = '\033[107m'
    HEADER = FG_BRIGHT_MAGENTA
    OKBLUE = FG_BRIGHT_BLUE
    OKCYAN = FG_BRIGHT_CYAN
    OKGREEN = FG_BRIGHT_GREEN
    WARNING = FG_BRIGHT_YELLOW
    FAIL = FG_BRIGHT_RED

# --- Function Generation Automation (with TTY Check) ---

def _create_color_func(color_code, end_code=_ezcolors_codes.ENDC):
    """Factory to create a function that wraps a string with ANSI codes."""
    def color_func(data_to_color):
        string_to_color = str(data_to_color)
        return f"{color_code}{string_to_color}{end_code}"
    return color_func

# Get the current module's dictionary (global namespace)
_module_globals = globals()

# Iterate through the code definitions in the internal class
for _name, _code in vars(_ezcolors_codes).items():
    # Filter for valid codes
    if _name.isupper() and isinstance(_code, str) and _code.startswith('\033') and _name != 'ENDC':
        # Determine function name
        _func_name = _name.lower()
        _new_func = _create_color_func(_code, _ezcolors_codes.ENDC)

        # Set metadata
        _new_func.__name__ = _func_name
        _new_func.__doc__ = (
            f"Wraps the input string with the '{_name}' ANSI code ({_code}).\n"
            f"Color codes are only added if ezcolors.COLORS_ENABLED is True."
        )

        _module_globals[_func_name] = _new_func

# # # --- Cleanup and Exports ---
# Expose ENDC directly
ENDC = _ezcolors_codes.ENDC

# Clean up internal variables
del _create_color_func
del _module_globals
del _name
del _code
del _func_name
del _new_func
# del _ezcolors_codes # Required for testing. Can be removed otherwise



if __name__ == "__main__":

    # --- Conditional Import for Debug Utility ---
    # Try importing the utility only when running as main
    _debug_utils_imported = False
    print_sanitized_namespace = None # Define placeholder
    try:
        # Adjust import path as needed based on structure and how you run it
        from debug_utils import print_sanitized_namespace
        _debug_utils_imported = True
    except ImportError:
        pass # Silently ignore if debug util isn't available

    # --- Argument Parsing ---
    parser = argparse.ArgumentParser(
        description="Run ezcolors examples or print sanitized module namespace.",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Print the sanitized module namespace after generation."
    )
    args = parser.parse_args()

    # --- Action Based on Arguments ---
    if args.debug:
        if _debug_utils_imported and print_sanitized_namespace:
            print("\n" + "="*20 + " DEBUGGING NAMESPACE (--debug) " + "="*20)
            # Pass a *copy* of the globals() dictionary
            print_sanitized_namespace(globals().copy(), title="--- ezcolors Module Globals (Post-Generation) ---")
            print("="*70 + "\n")
        else:
            print("Error: --debug specified, but debug_utils could not be imported.", file=sys.stderr)
            print("Ensure debug_utils.py is accessible in the Python path.", file=sys.stderr)
            sys.exit(1)
    else:
        # --- Default Action: Run Examples ---
        print("--- Testing Colors (Main Execution Examples) ---")
        # Use try/except NameError for safety or explicitly check if functions exist
        try:
            # Make sure these generated function names exist in globals()
            print(header("This is a header"))
            print(okblue("This is blue"))
            print(okcyan("This is cyan"))
            print(okgreen("This is green"))
            print(warning("This is a warning"))
            print(fail("This is a failure"))
            print(bold("This is bold"))
            print(underline("This is underlined"))
            print(bold(okblue("This is bold blue")))
            print(f"You can mix: {warning('Warning')} and {okgreen('success')}")
            print(f"Don't forget to end manually if needed: {bold('Bold continues...')} but now normal.")
            # Add other examples...
        except NameError as e:
             print(f"\nError running examples: A required function might be missing ({e})", file=sys.stderr)
             print("Check function generation logic or example names.", file=sys.stderr)