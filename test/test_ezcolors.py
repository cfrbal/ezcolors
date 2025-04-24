import pytest
import sys
import inspect

import ezcolors
from ezcolors import _ezcolors_codes

functions_to_test = []


expected_func_names = set()
for name in vars(_ezcolors_codes):
    if name.isupper() and name != 'ENDC':
        func_name = name.lower()
        if func_name.startswith('ok'):
            func_name = func_name[2:]
        expected_func_names.add(func_name)

for name, obj in inspect.getmembers(ezcolors):
    if name in expected_func_names and inspect.isfunction(obj):
        functions_to_test.append(obj)

if not functions_to_test:
     pytest.fail("Could not dynamically find any ezcolors functions to test.")


# --- Define the test ---
@pytest.mark.parametrize("color_func", functions_to_test)
def test_color_function_modifies_string(color_func):
    """
    Tests that each generated color function wraps the input string
    with some codes, making it different from the original.
    """
    input_string = "sample text"
    original_string = str(input_string)
    
    result = color_func(input_string)

    print(f"\nTesting {color_func.__name__}:")
    print(f"  Input : {original_string!r}")
    print(f"  Output: {result!r}") # Use !r for unambiguous output in test logs

    # --- Assertions ---
    # 1. The result should still be a string
    assert isinstance(result, str)

    # 2. The result MUST be different from the original string
    assert result != original_string

    # 3. The original text must be contained within the result string
    assert original_string in result

    # 4. The result should start with an ANSI escape sequence introducer
    assert result.startswith('\033[')

    # 5. The result should end with the standard ENDC code
    #    (Requires ENDC to be exported from ezcolors.py)
    assert result.endswith(ezcolors.ENDC)

    # 6. Check that ENDC isn't immediately after the start code (meaning empty content)
    start_code_end_index = result.find('m')
    if start_code_end_index != -1:
         content_start_index = start_code_end_index + 1
         # Ensure the content part doesn't immediately start with ENDC unless input was empty
         if original_string: # Only check if input wasn't empty
              assert not result[content_start_index:].startswith(ezcolors.ENDC)
         else:
              # If input was empty, output should be like '\033[XXm\033[0m'
              assert result[content_start_index:].startswith(ezcolors.ENDC)


def test_endc_constant():
    """Verify the ENDC constant is exported and correct."""
    assert hasattr(ezcolors, 'ENDC')
    assert ezcolors.ENDC == '\033[0m'

@pytest.mark.parametrize("color_func", functions_to_test)
def test_non_string_input(color_func):
    """Test that non-string input is converted and colored."""
    input_data = 12345
    expected_original = str(input_data)

    result = color_func(input_data)

    print(f"\nTesting non-string input with bold:")
    print(f"  Input : {input_data!r}")
    print(f"  Output: {result!r}")

    assert isinstance(result, str)
    assert result != expected_original
    assert expected_original in result
    assert result.startswith('\033[')
    assert result.endswith(ezcolors.ENDC)