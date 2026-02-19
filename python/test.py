"""
error_fiesta.py

A test script that produces many different Python exception types.
Run: python error_fiesta.py
"""

import importlib
import math

def ex_syntax_error():
    # Produces SyntaxError by exec'ing invalid code
    bad_code = "def broken(:\n    pass"
    exec(bad_code)  # SyntaxError

def ex_indentation_error():
    # Produces IndentationError via exec
    bad_code = "def f():\nprint('no indent')"
    exec(bad_code)  # IndentationError

def ex_name_error():
    # NameError: undefined name
    return undefined_variable  # NameError

def ex_type_error():
    # TypeError: unsupported operand types
    return 5 + "five"  # TypeError

def ex_value_error():
    # ValueError: invalid literal for int()
    return int("not-an-int")  # ValueError

def ex_index_error():
    # IndexError: list index out of range
    a = [1, 2, 3]
    return a[10]  # IndexError

def ex_key_error():
    # KeyError: missing dict key
    d = {"a": 1}
    return d["missing"]  # KeyError

def ex_zero_division_error():
    # ZeroDivisionError
    return 1 / 0  # ZeroDivisionError

def ex_attribute_error():
    # AttributeError: object has no attribute 'nope'
    return (42).nope  # AttributeError

def ex_module_not_found_error():
    # ModuleNotFoundError (a subclass of ImportError)
    importlib.import_module("this_module_does_not_exist_12345")  # ModuleNotFoundError

def ex_file_not_found_error():
    # FileNotFoundError
    open("definitely_nonexistent_file_xyz.txt", "r")  # FileNotFoundError

def ex_os_error():
    # OSError example (raise directly with a message)
    raise OSError("simulated OSError")

def ex_recursion_error():
    # RecursionError by deep recursion (we'll call a recursive function until it fails)
    def recurse(n=0):
        return recurse(n+1)
    recurse()  # RecursionError

def ex_overflow_error():
    # OverflowError via math.exp on a huge value (may raise OverflowError on some builds)
    math.exp(10000)  # OverflowError or returns inf on some systems

def ex_memory_error():
    # Simulate MemoryError by raising directly (safer than actually exhausting memory)
    raise MemoryError("simulated MemoryError for testing")

def ex_assertion_error():
    # AssertionError
    assert False, "simulated assertion"

def ex_runtime_error():
    # RuntimeError
    raise RuntimeError("simulated runtime error")

def ex_not_implemented_error():
    # NotImplementedError
    raise NotImplementedError("simulated not implemented")

def ex_unicode_decode_error():
    # UnicodeDecodeError constructed directly
    raise UnicodeDecodeError("utf-8", b"\xff", 0, 1, "invalid start byte")

def ex_unicode_encode_error():
    # UnicodeEncodeError constructed directly
    raise UnicodeEncodeError("utf-8", "😊", 0, 1, "simulated encode error")

def ex_stop_iteration():
    # StopIteration by calling next() on an exhausted iterator
    it = iter([])
    next(it)  # StopIteration

def ex_permission_error():
    # PermissionError (simulated)
    raise PermissionError("simulated permission denied")

def ex_floating_point_error():
    # FloatingPointError (manually raised)
    raise FloatingPointError("simulated floating point error")

def ex_lookup_error():
    # LookupError is a base for IndexError/KeyError; raise directly
    raise LookupError("simulated lookup error")

def ex_zero_length_slice_error():
    # Demonstrates ValueError via slicing parameters (rare); we just raise ValueError directly
    raise ValueError("simulated zero-length slice / value error")

# Collect tests: (name, function)
TESTS = [
    ("SyntaxError", ex_syntax_error),
    ("IndentationError", ex_indentation_error),
    ("NameError", ex_name_error),
    ("TypeError", ex_type_error),
    ("ValueError", ex_value_error),
    ("IndexError", ex_index_error),
    ("KeyError", ex_key_error),
    ("ZeroDivisionError", ex_zero_division_error),
    ("AttributeError", ex_attribute_error),
    ("ModuleNotFoundError", ex_module_not_found_error),
    ("FileNotFoundError", ex_file_not_found_error),
    ("OSError", ex_os_error),
    ("RecursionError", ex_recursion_error),
    ("OverflowError", ex_overflow_error),
    ("MemoryError", ex_memory_error),
    ("AssertionError", ex_assertion_error),
    ("RuntimeError", ex_runtime_error),
    ("NotImplementedError", ex_not_implemented_error),
    ("UnicodeDecodeError", ex_unicode_decode_error),
    ("UnicodeEncodeError", ex_unicode_encode_error),
    ("StopIteration", ex_stop_iteration),
    ("PermissionError", ex_permission_error),
    ("FloatingPointError", ex_floating_point_error),
    ("LookupError", ex_lookup_error),
    ("Extra ValueError (slice)", ex_zero_length_slice_error),
]

def run_all_tests():
    report = []
    for name, func in TESTS:
        try:
            print(f"\n--- Running test: {name} ---")
            func()
            # If the function returns normally, note that no exception was raised
            report.append((name, "NO EXCEPTION (unexpected)"))
            print(f"[WARN] {name} did not raise an exception.")
        except Exception as e:
            # Capture exception type and message
            ex_type = type(e).__name__
            print(f"[CAUGHT] {name} -> {ex_type}: {e!s}")
            report.append((name, f"{ex_type}: {e!s}"))
    print("\n=== SUMMARY ===")
    for name, result in report:
        print(f"{name:30s} -> {result}")
    print(f"\nTotal tests run: {len(TESTS)}")

if __name__ == "__main__":
    run_all_tests()
