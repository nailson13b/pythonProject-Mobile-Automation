import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

# Part 1 "Desired Capabilities"

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'Pixel 2 API 30'
desired_caps['app'] = ('C:\workspace\Automation\Android_Appium_Demo.apk')
desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'
desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'

# Part 2 "WebDriver object"
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

wait = WebDriverWait(driver, 25, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])

ele = wait.until(lambda x: x.find_element_by_android_uiautomator('text("TAB ACTIVITY")'))
ele.click()

print("Device Width and Height: ", driver.get_window_size())
#out of print statement is: Device Width and Height: {'width': 1440, 'height': 2621}
deviceSize = driver.get_window_size()
screenWidth = deviceSize['width']
screenHeight = deviceSize['height']

#######Right to Left#######
startx = screenWidth*8/9
endx = screenWidth/9
starty = screenHeight/2
endy = screenHeight/2

#######Left to Right#######
startx2 = screenWidth/9
endx2 = screenWidth*8/9
starty2 = screenHeight/2
endy2 = screenHeight/2

actions = TouchAction(driver)
actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()
time.sleep(2)
actions.long_press(None, startx2, starty2).move_to(None, endx2, endy2).release().perform()