import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from objects.homepageElements import homepsgeElements
driver = webdriver.Chrome()


try:

    actions = ActionChains(driver)
    driver.maximize_window()
    driver.get('https://www.xe.com/')
    time.sleep(5)

    Amount = driver.find_element(By.XPATH, homepsgeElements.amount)
    Amount.send_keys('10')

    Country = driver.find_element(By.XPATH, homepsgeElements.currency_country_from)
    Country.send_keys('USD')

    Country1 = driver.find_element(By.XPATH, '//ul[@id="midmarketFromCurrency-listbox"]/li[1]')
    Country1.click()

    country = driver.find_element(By.XPATH, homepsgeElements.currency_country_to)
    country.send_keys('EUR')

    Country2 = driver.find_element(By.XPATH, '//ul[@id="midmarketToCurrency-listbox"]/li[2]')
    Country2.click()

    ConverterButton = driver.find_element(By.XPATH, homepsgeElements.currency_covert_button)
    ConverterButton.click()
    driver.implicitly_wait(5)
    time.sleep(10)

    Actual_Result = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[4]/div[2]/section/div[2]/div/main/div/div[2]/div[1]/div/p[2]')

    a = Actual_Result.text
    b = "8.96 Euros"
    if a == b:
        print("USD to EURO Money Converter is Working successfully and the correct amount is converted")
    else:
        print("Money Converter is working successfully and the correct amount is converted")
finally:
    driver.quit()