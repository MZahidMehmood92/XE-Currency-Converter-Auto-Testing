import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from objects.homepageElements import homepsgeElements


driver = webdriver.Chrome()
driver.get("https://www.xe.com/")
time.sleep(5)


def test_logo_click():
    button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/header/div[1]/div[1]/a/svg/path")
    assert button.is_displayed(), "logo is visible on the page."
    button.click()
    assert "xe" in driver.current_url, "Redirect to home page failed."
    print("XE Logo click successfully and redirect the homepage")
test_logo_click()
driver.quit()