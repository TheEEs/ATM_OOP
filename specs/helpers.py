from termcolor import colored

def should_eq(input, expected_output):
    try:
        assert input == expected_output
    except AssertionError:
        raise AssertionError(
            f'Output: {colored(input, "red")}. Kết quả mong đợi: {colored(expected_output,"green")}'
        )

