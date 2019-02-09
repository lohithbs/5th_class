import time

from selenium import webdriver

browser='chrome'
if browser=='chrome':
    driver=webdriver.Chrome(executable_path='C:/Users/bsloh/PycharmProjects/s_class/drivers/chromedriver.exe')
elif browser=='firefox':
    driver=webdriver.Firefox(executable_path='C:/Users/bsloh/PycharmProjects/s_class/drivers/geckodriver.exe')
elif browser=='Ie':
    driver=webdriver.Ie(executable_path='C:/Users/bsloh/PycharmProjects/s_class/drivers/IEDriverServer.exe')
else:
    print('provide appropiate browser name')


driver.get('https://www.makemytrip.com')
time.sleep(5)
driver.find_element_by_id("header_tab_hotels").click()
driver.back()