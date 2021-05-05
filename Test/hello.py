from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0'
desired_caps['deviceName'] = 'c5e5d5eb'  # 真机名 可以随便写
desired_caps['appPackage'] = 'com.android.settings'  # 程序名 --设置
desired_caps['appActivity'] = '.Settings$LockAndSecuritySettingsActivity'  # 界面名
desired_caps['noReset'] = True  # appium每次起动时，默认每次都会重置程序

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.implicitly_wait(5)
print('当前包名为：{} 当前起动名为：{}'.format(driver.current_package,driver.current_activity))
el = driver.find_element_by_xpath('//*[@text="图案"]')
TouchAction(driver).tap(el).perform()
# TouchAction(driver).press(el).perform()
# TouchAction(driver).press(el).wait(1000).perform()
sleep(2) # 界面要延时2s才能出来必须等待
TouchAction(driver).press(x=380,y=1764).move_to(x=718,y=1764).move_to(x=718,y=2104).move_to(x=1059,y=2107).perform()
driver.press_keycode(4)
driver.press_keycode(3)
sleep(10)
driver.quit()