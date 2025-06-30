import pytest
class TestClass:
    @pytest.mark.regression
    def test_loginbyemail(self):
        print("This is login by email")
        assert True==True

    @pytest.mark.sanity
    def test_loginbyfacebook(self):
        print("This is login by facebook")
        assert True==True

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_loginbytwitter(self):
        print("This is login by twitter")
        assert True==True
