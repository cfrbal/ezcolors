ENDC = '\x1b[0m'

def bg_black(text: object) -> str:
    """Wraps the input string with the 'BG_BLACK' ANSI code (<ESC>[40m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[40m{string_to_color}{ENDC}"

def bg_blue(text: object) -> str:
    """Wraps the input string with the 'BG_BLUE' ANSI code (<ESC>[44m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[44m{string_to_color}{ENDC}"

def bg_bright_black(text: object) -> str:
    """Wraps the input string with the 'BG_BRIGHT_BLACK' ANSI code (<ESC>[100m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[100m{string_to_color}{ENDC}"

def bg_bright_blue(text: object) -> str:
    """Wraps the input string with the 'BG_BRIGHT_BLUE' ANSI code (<ESC>[104m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[104m{string_to_color}{ENDC}"

def bg_bright_cyan(text: object) -> str:
    """Wraps the input string with the 'BG_BRIGHT_CYAN' ANSI code (<ESC>[106m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[106m{string_to_color}{ENDC}"

def bg_bright_green(text: object) -> str:
    """Wraps the input string with the 'BG_BRIGHT_GREEN' ANSI code (<ESC>[102m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[102m{string_to_color}{ENDC}"

def bg_bright_magenta(text: object) -> str:
    """Wraps the input string with the 'BG_BRIGHT_MAGENTA' ANSI code (<ESC>[105m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[105m{string_to_color}{ENDC}"

def bg_bright_red(text: object) -> str:
    """Wraps the input string with the 'BG_BRIGHT_RED' ANSI code (<ESC>[101m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[101m{string_to_color}{ENDC}"

def bg_bright_white(text: object) -> str:
    """Wraps the input string with the 'BG_BRIGHT_WHITE' ANSI code (<ESC>[107m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[107m{string_to_color}{ENDC}"

def bg_bright_yellow(text: object) -> str:
    """Wraps the input string with the 'BG_BRIGHT_YELLOW' ANSI code (<ESC>[103m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[103m{string_to_color}{ENDC}"

def bg_cyan(text: object) -> str:
    """Wraps the input string with the 'BG_CYAN' ANSI code (<ESC>[46m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[46m{string_to_color}{ENDC}"

def bg_green(text: object) -> str:
    """Wraps the input string with the 'BG_GREEN' ANSI code (<ESC>[42m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[42m{string_to_color}{ENDC}"

def bg_magenta(text: object) -> str:
    """Wraps the input string with the 'BG_MAGENTA' ANSI code (<ESC>[45m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[45m{string_to_color}{ENDC}"

def bg_red(text: object) -> str:
    """Wraps the input string with the 'BG_RED' ANSI code (<ESC>[41m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[41m{string_to_color}{ENDC}"

def bg_white(text: object) -> str:
    """Wraps the input string with the 'BG_WHITE' ANSI code (<ESC>[47m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[47m{string_to_color}{ENDC}"

def bg_yellow(text: object) -> str:
    """Wraps the input string with the 'BG_YELLOW' ANSI code (<ESC>[43m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[43m{string_to_color}{ENDC}"

def blink(text: object) -> str:
    """Wraps the input string with the 'BLINK' ANSI code (<ESC>[5m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[5m{string_to_color}{ENDC}"

def blink_rapid(text: object) -> str:
    """Wraps the input string with the 'BLINK_RAPID' ANSI code (<ESC>[6m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[6m{string_to_color}{ENDC}"

def blue(text: object) -> str:
    """Wraps the input string with the 'BLUE' ANSI code (<ESC>[94m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[94m{string_to_color}{ENDC}"

def bold(text: object) -> str:
    """Wraps the input string with the 'BOLD' ANSI code (<ESC>[1m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[1m{string_to_color}{ENDC}"

def cyan(text: object) -> str:
    """Wraps the input string with the 'CYAN' ANSI code (<ESC>[96m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[96m{string_to_color}{ENDC}"

def dim(text: object) -> str:
    """Wraps the input string with the 'DIM' ANSI code (<ESC>[2m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[2m{string_to_color}{ENDC}"

def fail(text: object) -> str:
    """Wraps the input string with the 'FAIL' ANSI code (<ESC>[91m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[91m{string_to_color}{ENDC}"

def fg_black(text: object) -> str:
    """Wraps the input string with the 'FG_BLACK' ANSI code (<ESC>[30m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[30m{string_to_color}{ENDC}"

def fg_blue(text: object) -> str:
    """Wraps the input string with the 'FG_BLUE' ANSI code (<ESC>[34m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[34m{string_to_color}{ENDC}"

def fg_bright_black(text: object) -> str:
    """Wraps the input string with the 'FG_BRIGHT_BLACK' ANSI code (<ESC>[90m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[90m{string_to_color}{ENDC}"

def fg_bright_blue(text: object) -> str:
    """Wraps the input string with the 'FG_BRIGHT_BLUE' ANSI code (<ESC>[94m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[94m{string_to_color}{ENDC}"

def fg_bright_cyan(text: object) -> str:
    """Wraps the input string with the 'FG_BRIGHT_CYAN' ANSI code (<ESC>[96m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[96m{string_to_color}{ENDC}"

def fg_bright_green(text: object) -> str:
    """Wraps the input string with the 'FG_BRIGHT_GREEN' ANSI code (<ESC>[92m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[92m{string_to_color}{ENDC}"

def fg_bright_magenta(text: object) -> str:
    """Wraps the input string with the 'FG_BRIGHT_MAGENTA' ANSI code (<ESC>[95m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[95m{string_to_color}{ENDC}"

def fg_bright_red(text: object) -> str:
    """Wraps the input string with the 'FG_BRIGHT_RED' ANSI code (<ESC>[91m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[91m{string_to_color}{ENDC}"

def fg_bright_white(text: object) -> str:
    """Wraps the input string with the 'FG_BRIGHT_WHITE' ANSI code (<ESC>[97m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[97m{string_to_color}{ENDC}"

def fg_bright_yellow(text: object) -> str:
    """Wraps the input string with the 'FG_BRIGHT_YELLOW' ANSI code (<ESC>[93m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[93m{string_to_color}{ENDC}"

def fg_cyan(text: object) -> str:
    """Wraps the input string with the 'FG_CYAN' ANSI code (<ESC>[36m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[36m{string_to_color}{ENDC}"

def fg_green(text: object) -> str:
    """Wraps the input string with the 'FG_GREEN' ANSI code (<ESC>[32m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[32m{string_to_color}{ENDC}"

def fg_magenta(text: object) -> str:
    """Wraps the input string with the 'FG_MAGENTA' ANSI code (<ESC>[35m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[35m{string_to_color}{ENDC}"

def fg_red(text: object) -> str:
    """Wraps the input string with the 'FG_RED' ANSI code (<ESC>[31m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[31m{string_to_color}{ENDC}"

def fg_white(text: object) -> str:
    """Wraps the input string with the 'FG_WHITE' ANSI code (<ESC>[37m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[37m{string_to_color}{ENDC}"

def fg_yellow(text: object) -> str:
    """Wraps the input string with the 'FG_YELLOW' ANSI code (<ESC>[33m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[33m{string_to_color}{ENDC}"

def green(text: object) -> str:
    """Wraps the input string with the 'GREEN' ANSI code (<ESC>[92m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[92m{string_to_color}{ENDC}"

def header(text: object) -> str:
    """Wraps the input string with the 'HEADER' ANSI code (<ESC>[95m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[95m{string_to_color}{ENDC}"

def hidden(text: object) -> str:
    """Wraps the input string with the 'HIDDEN' ANSI code (<ESC>[8m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[8m{string_to_color}{ENDC}"

def inverse(text: object) -> str:
    """Wraps the input string with the 'INVERSE' ANSI code (<ESC>[7m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[7m{string_to_color}{ENDC}"

def italic(text: object) -> str:
    """Wraps the input string with the 'ITALIC' ANSI code (<ESC>[3m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[3m{string_to_color}{ENDC}"

def red(text: object) -> str:
    """Wraps the input string with the 'RED' ANSI code (<ESC>[91m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[91m{string_to_color}{ENDC}"

def strikethrough(text: object) -> str:
    """Wraps the input string with the 'STRIKETHROUGH' ANSI code (<ESC>[9m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[9m{string_to_color}{ENDC}"

def underline(text: object) -> str:
    """Wraps the input string with the 'UNDERLINE' ANSI code (<ESC>[4m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[4m{string_to_color}{ENDC}"

def warning(text: object) -> str:
    """Wraps the input string with the 'WARNING' ANSI code (<ESC>[93m)."""
    # Explicitly convert to string
    string_to_color = str(text)
    return f"[93m{string_to_color}{ENDC}"
