import pytest

test_datas = [
    (11, 22, 33),
    (22, 33, 55)
]

datas_dict = [
    {"a": 1, "b": 2, "c": 3},
    {"a": 11, "b": 22, "c": 33},
    {"a": 111, "b": 222, "c": 333},
]


# 方式一:直接写
@pytest.mark.parametrize("a, b, c" , [(1, 2, 3), (4, 5, 9)])
def test_add01(a, b, c):
    res = a + b
    assert res == c


# 方式二:参数为列表中嵌套元组
@pytest.mark.parametrize("data", test_datas)
def test_add02(data):
    res = data[0] + data[1]
    assert res == data[2]


# 方式三:参数为列表中嵌套字典
@pytest.mark.parametrize("data", datas_dict)
def test_add03(data):
    res = data["a"] + data["b"]
    assert res == data["c"]


