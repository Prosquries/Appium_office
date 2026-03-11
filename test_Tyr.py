import pytest


class TestClass:

    @pytest.fixture()
    def Setup(self):
        print("opening try")
        yield
        print()
        print("closing try")

    # @pytest.mark.usefixtures("Setup")
    # def test_try1(self):
    #     print("This test case will pass of login the app with Android phone")
    #
    # @pytest.mark.usefixtures("Setup")
    # def test_try2(self):
    #     print("This test case will pass of login the app with IPhone Devices")

    @pytest.mark.sanity
    def test_try1(self,Setup):
        print("This test case will pass of login the app with Android phone")

    @pytest.mark.regression
    def test_try2(self,Setup):
        print("This test case will pass of login the app with IPhone Devices")



# To run all the test cases at once
# python -m pytest -s -v test_try.py

# -s stands for responses and -v is stands for verbal

# To run specific test cases
# python -m pytest -s -v -k test_try1
# python -m pytest -s -v -k test_try2


# python -m pytest -s -v -k "regression" .\test_Tyr.py - This is for regression testing

# python -m pytest -s -v -k "sanity" .\test_Tyr.py - This is for sanity testing.