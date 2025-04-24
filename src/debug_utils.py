# debug_utils.py

import sys
import inspect # Needed to reliably check for functions

# Define constants outside or as defaults
_DEFAULT_ESCAPE_CHAR = '\x1B' # Use hex \x1B or octal \033
_DEFAULT_REPLACEMENT_STR = '<ESC>'

def print_sanitized_namespace(
    namespace_dict,
    title="--- User-Accessible Namespace Contents ---", # Changed default title
    skip_underscores=True,
    # New parameter to control filtering: Default True to show only user funcs/ENDC
    filter_user_items=True,
    escape_char=_DEFAULT_ESCAPE_CHAR,
    replacement_str=_DEFAULT_REPLACEMENT_STR
):
    """
    Prints a formatted and sanitized representation of a namespace dictionary.

    By default, filters to show only likely user-accessible items: generated
    functions and the ENDC constant. Set `filter_user_items=False` to show
    all non-underscore items.

    Replaces ANSI escape characters in strings and docstrings with a
    placeholder for safe terminal output.

    Args:
        namespace_dict (dict): The dictionary representing the namespace (e.g., globals()).
        title (str, optional): A title to print before the listing.
                                Defaults to "--- User-Accessible Namespace Contents ---".
        skip_underscores (bool, optional): If True, skips names starting with '_'.
                                            Defaults to True.
        filter_user_items (bool, optional): If True, only shows functions and the
                                            'ENDC' constant. If False, shows all
                                            non-underscore items. Defaults to True.
        escape_char (str, optional): The ANSI escape character sequence to replace.
                                     Defaults to '\x1B'.
        replacement_str (str, optional): The string to substitute for escape_char.
                                         Defaults to '<ESC>'.
    """
    print(f"\n{title}")
    print("-" * (len(title) if title else 70))

    items_snapshot = list(namespace_dict.items())
    items_printed = 0 # Counter for items actually printed

    for name, obj in items_snapshot:
        # --- Initial Filtering (Underscores) ---
        if skip_underscores and name.startswith('_'):
            continue

        # --- Filtering for User Items (if enabled) ---
        if filter_user_items:
            is_endc_constant = (name == 'ENDC' and isinstance(obj, str))
            # Use inspect.isfunction to be specific about generated functions
            is_likely_user_function = inspect.isfunction(obj)

            # If it's not one of the items we want to show in filter mode, skip
            if not (is_endc_constant or is_likely_user_function):
                continue
        # --- End Filtering ---

        items_printed += 1 # Increment counter if item wasn't filtered out

        # Determine type representation
        try:
            type_repr = type(obj).__name__
        except Exception:
            type_repr = str(type(obj))

        # Print basic info (adjust padding as needed)
        print(f"Name: {name:<20} | Type: {type_repr:<15}", end="")

        # Sanitization and Value/Doc printing
        try:
            # Special handling for the ENDC constant value (since it contains ESC)
            if name == 'ENDC' and isinstance(obj, str):
                 sanitized_repr = obj.replace(escape_char, replacement_str)
                 print(f" | Value: {sanitized_repr}")
            # Handle other strings containing ANSI codes (e.g., if original constants were kept)
            elif isinstance(obj, str) and escape_char in obj:
                print(f" | Value: <String with ANSI codes>")
            # Handle functions (likely generated ones)
            elif inspect.isfunction(obj): # Use inspect check again for consistency
                doc = getattr(obj, '__doc__', None)
                if doc and isinstance(doc, str): # Check doc is a string
                    try:
                        first_doc_line = doc.strip().splitlines()[0]
                        sanitized_doc_line = first_doc_line.replace(escape_char, replacement_str)
                        print(f" | Doc: {sanitized_doc_line}")
                    except IndexError: # Handles empty docstring split
                        print(" | Doc: <Empty docstring>")
                elif doc: # Doc exists but is not a string?
                    print(" | Doc: <Non-string docstring>")
                else: # No docstring
                    print(" | Doc: <No docstring>")
            # Handle other non-callable, non-string types
            else:
                obj_repr = repr(obj)
                sanitized_repr = obj_repr.replace(escape_char, replacement_str)
                if len(sanitized_repr) > 60:
                     sanitized_repr = sanitized_repr[:57] + "..."
                print(f" | Value: {sanitized_repr}")

        except Exception as e: # Catch other potential errors during processing
             # Added error context
             print(f" | Error processing value/doc: {e!r}")

    if items_printed == 0:
        print("No items matched the current filter criteria.")

    print("-" * (len(title) if title else 70))