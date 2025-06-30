import pytest
class TestClass:
    def test_loginbyFacebook(self):
        print("This is login by facebook")
        assert True

    @pytest.mark.skip
    def test_loginbyemail(self):
        print("This is login by email")
        assert True

    @pytest.mark.skip
    def test_search(self):
        print("This is search functionality")
        assert True