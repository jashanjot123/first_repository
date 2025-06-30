import pytest
class TestClass:
    @pytest.mark.third
    def test_methodC(self):
        print("Running method third")

    @pytest.mark.second
    def test_methodB(self):
        print("Runninng method second")

    @pytest.mark.first
    def test_methodA(self):
        print("Running method First")