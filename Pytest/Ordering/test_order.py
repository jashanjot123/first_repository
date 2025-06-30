import pytest
class TestClass:
    @pytest.mark.order(3)
    def test_methodC(self):
        print("Running method third")

    @pytest.mark.order(2)
    def test_methodB(self):
        print("Runninng method second")

    @pytest.mark.order(1)
    def test_methodA(self):
        print("Running method First")
