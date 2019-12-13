from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_xpath('//*[@id="su"]').click()
time.sleep(3)
driver.save_screenshot('D:/animation/unluckyBody.png')

driver.quit()