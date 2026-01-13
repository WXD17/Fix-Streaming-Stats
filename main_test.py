from main import *

run_cases = [
    (120, 150, 2, (2.0, 300, 150.0)),
    (240, 100, 3, (4.0, 300, 75.0)),
]

submit_cases = run_cases + [
    (60, 200, 1, (1.0, 200, 200.0)),
    (180, 90, 4, (3.0, 360, 120.0)),
    (300, 80, 5, (5.0, 400, 80.0)),
]


def test(total_minutes, snack_calories, snacks_eaten, expected_output):
    print("---------------------------------")
    print("Input:")
    print(f"  total_minutes:   {total_minutes}")
    print(f"  snack_calories:  {snack_calories}")
    print(f"  snacks_eaten:    {snacks_eaten}")
    print("")
    result = calculate_streaming_stats(total_minutes, snack_calories, snacks_eaten)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        return True
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
            print("Pass")
        else:
            failed += 1
            print("Fail")
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
