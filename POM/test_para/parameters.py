import pytest
class TestClass:
    @pytest.mark.parametrize("num1,num2",[(10,10),(2,5),(4,4),(4,8)])
    def test_calculate(self,num1,num2):
        assert num1==num2
