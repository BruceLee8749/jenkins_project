from time import sleep

from selenium import webdriver


class BackDriver:
    def __init__(self):
        self.driver = webdriver.Firefox();

    def back_driver(self):
        return self.driver;


class Base:
    def __init__(self, driver):
        self.driver = driver

    def driverInfo(self):
        print('driver地址：', self.driver)


class Login1(Base):
    def driver_quit(self):
        self.driver.quit()

    pass


class Login2(Base):
    def driver_quit(self):
        self.driver.quit()

    def driver_get(self):
        self.driver.get('http://www.baidu.com')


if __name__ == '__main__':
    driver_var = BackDriver().back_driver();
    login1 = Login1(driver_var)
    login1.driverInfo()

    sleep(5)

    # login1.driver_quit()

    login2 = Login2(driver_var)
    login2.driverInfo()
    login2.driver_get()
    sleep(5)
    login1.driver_quit()


# 即便调用了driver.quit() driver变量依然存在
