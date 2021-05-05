import pytest


class TestResult:
    @classmethod
    def setup_class(cls):
        print('--看看谁先被执行--')

    def test_20(self):
        print('这是test_20')
        assert 1

    @pytest.mark.run(order=10)
    def test_10(self):
        print('这是test_10')
        assert 0

    def test_01(self):
        print('这是test_01')
        assert 1
if __name__ == '__main__':
    pytest.main()