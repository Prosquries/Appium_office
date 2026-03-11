import pytest

class TestClass:

    def test_UserLogin(self):
        print("Logining the app by the Email and password")

    @pytest.mark.skip(reason="This test fails") # Reason and skip it
    def test_UserLogin2(self):
        print("Logining the app by the Phone number and OTP")

    def test_UserLogin3(self):
        print("Logining the app by the Google account")

    def test_UserLogin4(self):
        print("Logining the app by the facebook account")

    def test_UserLogin5(self):
        print("Logining the app by the twitter account")
