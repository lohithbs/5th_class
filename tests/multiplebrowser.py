from selenium import webdriver

browser='Ie'
if browser=='chrome':
    driver=webdriver.Chrome(executable_path='C:/Users/bsloh/PycharmProjects/s_class/drivers/chromedriver.exe')
elif browser=='firefox':
    driver=webdriver.Firefox(executable_path='C:/Users/bsloh/PycharmProjects/s_class/drivers/geckodriver.exe')
elif browser=='Ie':
    driver=webdriver.Ie(executable_path='C:/Users/bsloh/PycharmProjects/s_class/drivers/IEDriverServer.exe')
else:
    print('provide appropiate browser name')

driver.get('https://www.facebook.com')
driver.maximize_window()
driver.find_element_by_id('email').send_keys('test')
driver.find_element_by_id('pass').send_keys('12345')
driver.find_element_by_id('u_0_2').click()

