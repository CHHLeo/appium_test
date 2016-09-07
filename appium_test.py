# coding=utf-8
from appium import webdriver
import appium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = 'Nexus 5'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# driver.execute_script("mobile: scroll", {"direction": "down"})
driver.swipe(0, 0, 0, 1)
time.sleep(1)
driver.swipe(0, 0, 0, 1)
time.sleep(1)
driver.find_element_by_name("Accounts").click()
time.sleep(1)
driver.find_element_by_name("Add account").click()
time.sleep(1)
driver.find_element_by_name("Google").click()
time.sleep(5)
# driver.find_element_by_xpath("//*[@class='android.view.View' and @content-desc='Or create a new "
#                              "account']").click()
driver.tap([(400, 1450)], 500)
time.sleep(5)
driver.press_keycode(99)
driver.press_keycode(31)
# driver.find_element_by_id('com.android.settings:id/digit9').click()
# driver.find_element_by_xpath("//android.widget.TextView[@text='Google']").click()
# print driver.find_element_by_name("1").click()
# time.sleep(5)
# print "abc"
# WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_repList_ctl00_hypViewBulletin")))
driver.quit()
