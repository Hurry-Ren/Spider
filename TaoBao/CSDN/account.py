import time
from selenium.webdriver.common.keys import Keys
def account(driver):
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/div[5]/ul/li[2]/a').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="all"]').clear()
    driver.find_element_by_xpath('//*[@id="all"]').send_keys('15970152175')
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="all"]').send_keys(Keys.TAB)
    driver.find_element_by_xpath('//*[@id="password-number"]').clear()
    driver.find_element_by_xpath('//*[@id="password-number"]').send_keys('REN5201314...+')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/div[5]/div/div[6]/div/button').click()
    time.sleep(100)