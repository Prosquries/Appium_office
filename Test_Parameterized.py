import pytest

# @staticmethod
def get_Data():
    return[
        ('Aarav','Aarav2005'),
        ('Rohit','Rohit2004')
    ]

@pytest.mark.parametrize("Username,password",get_Data())
def test_Param(Username,password):
    print(f"Username is {Username} and the password id {password}")
