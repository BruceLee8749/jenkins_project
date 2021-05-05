import pytest
import yaml


def read_contact_data(key, filename):
    with open('../data/' + filename, 'r', encoding='UTF-8') as f:
        data = yaml.full_load(f)
        data_dict = data[key].values()
        data_list = list(data_dict)
        print('打印列表：{}  打印类型：{}'.format(data_list, type(data_list)))
        return data_list


class TestContact:
    @pytest.mark.parametrize("args", read_contact_data('test_contact01', 'contact_data.yaml'))
    def test_contact1(self, args):
        self.name = args['name']
        self.phone = args['phone']
        print("打印  name:{}，age:{}".format(self.name, self.phone))

    @pytest.mark.parametrize("args", read_contact_data('test_contact02', "contact_data.yaml"))
    def test_contact1(self, args):
        self.name = args['name']
        self.age = args['age']
        self.height = args['height']
        print("打印  name:{}，age:{}，height:{}".format(self.name, self.age, self.height))


if __name__ == '__main__':
    pytest.main()
