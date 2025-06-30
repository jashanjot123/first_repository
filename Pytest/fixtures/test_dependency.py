import pytest
from pytest_dependency import depends


class TestClass:
    @pytest.mark.dependency
    def test_openapp(self):
        assert  False

    @pytest.mark.dependency(depends=['TestClass::test_openapp'])
    def test_loginapp(self):
        assert True

    @pytest.mark.dependency(depends=['TestClass::test_loginapp'])
    def test_search(self):
        assert True

    @pytest.mark.dependency(depends=['TestClass::test_loginapp','TestClass::test_search'])
    def test_Advancedsearch(self):
        assert True

    @pytest.mark.dependency
    def test_Logoutapp(self):
        assert True
