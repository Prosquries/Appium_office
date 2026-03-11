import pytest

def test_Assertions():
    print("Testing the Assertions")

    Expected_Outcome = "Chrome"
    Actual_Outcome = "Firefox"

    assert Expected_Outcome == Actual_Outcome, "Test is failed"

## soft assert is not available in this python version (3.14)