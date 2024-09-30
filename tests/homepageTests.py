import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from objects.homepageElements import homepsgeElements
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()
driver.get("https://www.xe.com/")
driver.maximize_window()
time.sleep(5)

#XE logo clickable and redirect homepage
def test_logo_click():
    button = driver.find_element(By.XPATH, homepsgeElements.logo)
    button.click()
    expected_url = "https://www.xe.com/"
    if driver.current_url == expected_url:
        print("XE Logo Click Successfully and Correct Page Loaded")
    else:
        print("XE Logo Click Failed")
test_logo_click()
time.sleep(5)




# Personal button in header
def test_click_header_button():
    button = driver.find_element(By.XPATH, homepsgeElements.personal)
    assert button.is_displayed(), "Button is visible on the page."
    button.click()
    expected_url = "https://www.xe.com/"
    if driver.current_url == expected_url:
        print("personal Button Click Successfully and Correct Page Loaded")
    else:
        print("Personal Button Failed")
test_click_header_button()
time.sleep(5)




# Business button in header
def test_click_header_button():
    button = driver.find_element(By.XPATH, homepsgeElements.business)
    assert button.is_displayed(), "Button is visible on the page."
    button.click()
    expected_url = "https://www.xe.com/business/"
    if driver.current_url == expected_url:
        print("Business Button Click Successfully and Correct Page Loaded")
    else:
        print("Business Button Failed")
test_click_header_button()
time.sleep(5)
driver.back()
time.sleep(2)




# Send Money button in header
def test_click_header_button():
    button = driver.find_element(By.XPATH, homepsgeElements.send_money)
    assert button.is_displayed(), "Button is visible on the page."
    button.click()
    expected_url = "https://www.xe.com/send-money/"
    if driver.current_url == expected_url:
        print("Send Money Button Click Successfully and Correct Page Loaded")
    else:
        print("Send Money Button Failed")
test_click_header_button()
time.sleep(4)
driver.back()
time.sleep(3)



# Converter button in header
def test_click_header_button():
    button = driver.find_element(By.XPATH, homepsgeElements.converter)
    assert button.is_displayed(), "Button is visible on the page."
    button.click()
    expected_url = "https://www.xe.com/currencyconverter/"
    if driver.current_url == expected_url:
        print("Converter Button Click Successfully and Correct Page Loaded")
    else:
        print("Converter Button Failed")
test_click_header_button()
time.sleep(2)
driver.back()
time.sleep(2)




# Currency API button in header
def test_click_header_button():
    button = driver.find_element(By.XPATH, homepsgeElements.currency_api)
    assert button.is_displayed(), "Button is visible on the page."
    button.click()
    expected_url = "https://www.xe.com/xecurrencydata/"
    if driver.current_url == expected_url:
        print("Currency API Button Click Successfully and Correct Page Loaded")
    else:
        print("Currency API Button Failed")
test_click_header_button()
time.sleep(2)
driver.back()
time.sleep(2)



# Tools option currency chart
def tools_select_button():
    actions = ActionChains(driver)
    tools_dropdown = driver.find_element(By.XPATH, homepsgeElements.tools)
    actions.move_to_element(tools_dropdown).perform()
    tools_option1 = driver.find_element(By.XPATH, homepsgeElements.tool_option1)
    tools_option1.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/currencycharts/"
    if driver.current_url == expected_url:
        print("currency Chart option click successfully and correct page open")
    else:
        print("currency chart option not work")
tools_select_button()
time.sleep(3)
driver.back()
time.sleep(3)



# Tools option rate alert
def tools_select_button():
    actions = ActionChains(driver)
    tools_dropdown = driver.find_element(By.XPATH, homepsgeElements.tools)
    actions.move_to_element(tools_dropdown).perform()
    Tools_option2 = driver.find_element(By.XPATH,  homepsgeElements.tool_option2)
    Tools_option2.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/ratealerts/"
    if driver.current_url == expected_url:
        print("rate alerts option click successfully and correct page open")
    else:
        print("rate alerts option not work")
tools_select_button()
time.sleep(3)
driver.back()
time.sleep(3)



# Tools option historical country rate
def tools_select_button():
    actions = ActionChains(driver)
    tools_dropdown = driver.find_element(By.XPATH, homepsgeElements.tools)
    actions.move_to_element(tools_dropdown).perform()
    Tools_option3 = driver.find_element(By.XPATH, homepsgeElements.tool_option3)
    Tools_option3.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/currencytables/"
    if driver.current_url == expected_url:
        print("historical country rate Option Click Successfully and Correct Page Open")
    else:
        print("historical country cate Option Not Work")
tools_select_button()
time.sleep(2)
driver.back()
time.sleep(2)





# Tools option IBAN Calculator
def tools_select_button():
    actions = ActionChains(driver)
    tools_dropdown = driver.find_element(By.XPATH, homepsgeElements.tools)
    actions.move_to_element(tools_dropdown).perform()
    Tools_option4 = driver.find_element(By.XPATH, homepsgeElements.tool_option4)
    Tools_option4.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/ibancalculator/"
    if driver.current_url == expected_url:
        print("IBAN Calculator Option Click Successfully and Correct Page Open")
    else:
        print("IBAN Calculator Option Not Work")
tools_select_button()
time.sleep(3)
driver.back()
time.sleep(3)






# Tools option Apps
def tools_select_button():
    actions = ActionChains(driver)
    tools_dropdown = driver.find_element(By.XPATH, homepsgeElements.tools)
    actions.move_to_element(tools_dropdown).perform()
    Tools_option5 = driver.find_element(By.XPATH, homepsgeElements.tool_option5)
    Tools_option5.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/apps/"
    if driver.current_url == expected_url:
        print("Apps Option Click Successfully and Correct Page Open")
    else:
        print("Apps Option Not Work")
tools_select_button()
time.sleep(3)
driver.back()
time.sleep(3)






# Tools option More Tools
def tools_select_button():
    actions = ActionChains(driver)
    tools_dropdown = driver.find_element(By.XPATH,  homepsgeElements.tools)
    actions.move_to_element(tools_dropdown).perform()
    Tools_option6 = driver.find_element(By.XPATH, homepsgeElements.tool_option6)
    Tools_option6.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/tools/"
    if driver.current_url == expected_url:
        print("More Tools Option Click Successfully and Correct Page Open")
    else:
        print("More Tools Option Not Work")
tools_select_button()
time.sleep(3)
driver.back()
time.sleep(3)







'''
# Resources option Help Center
def resource_select_button():
    actions = ActionChains(driver)
    resource_selection = driver.find_element(By.XPATH,  Element.resource)
    actions.move_to_element(resource_selection).perform()
    Resource_option1 = driver.find_element(By.XPATH, Element.resource_option1)
    Resource_option1.click()
    driver.implicitly_wait(5)
    main_window = driver.current_window_handle
    for handle in driver.window_handles:
        if handle != main_window:
            driver.switch_to.window(handle)
    expected_url = "https://help.xe.com/hc/en-gb"
    if driver.current_url == expected_url:
        print("Help Center Option Clicked Successfully and Correct Page Opened")
    else:
        print("Help Center Option Not Working")
    driver.close()
resource_select_button()
time.sleep(2)
'''



# Resources option Refer a Friend
def resource_select_button():
    actions = ActionChains(driver)
    resource_selection = driver.find_element(By.XPATH,  homepsgeElements.resource)
    actions.move_to_element(resource_selection).perform()
    Resource_option2 = driver.find_element(By.XPATH, homepsgeElements.resource_option2)
    Resource_option2.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/mt/uk-money-transfer/lp/refer-a-friend-onsite/?utm_content=xecom-banner-perscorp/?generic=xemoneytransfer"
    if driver.current_url == expected_url:
        print("Refer a Friend Option Click Successfully and Correct Page Open")
    else:
        print("Refer a Friend Option Not Work")
resource_select_button()
time.sleep(3)
driver.back()






# Resources option blog
def resource_select_button():
    actions = ActionChains(driver)
    resource_selection = driver.find_element(By.XPATH,  homepsgeElements.resource)
    actions.move_to_element(resource_selection).perform()
    Resource_option3 = driver.find_element(By.XPATH, homepsgeElements.resource_option3)
    Resource_option3.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/blog/"
    if driver.current_url == expected_url:
        print("Blog Option Click Successfully and Correct Page Open")
    else:
        print(" Blog Option Not Work")
resource_select_button()
time.sleep(3)
driver.back()
time.sleep(3)








# Resources option Money Transfer Tip
def resource_select_button():
    actions = ActionChains(driver)
    resource_selection = driver.find_element(By.XPATH,  homepsgeElements.resource)
    actions.move_to_element(resource_selection).perform()
    Resource_option4 = driver.find_element(By.XPATH, homepsgeElements.resource_option4)
    Resource_option4.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/moneytransfertips/"
    if driver.current_url == expected_url:
        print("Money Transfer Tip Option Click Successfully and Correct Page Open")
    else:
        print("Money Transfer Tip Option Not Work")
resource_select_button()
time.sleep(3)
driver.back()








# Currency Encyclopedia Money Transfer Tip
def resource_select_button():
    actions = ActionChains(driver)
    resource_selection = driver.find_element(By.XPATH,  homepsgeElements.resource)
    actions.move_to_element(resource_selection).perform()
    Resource_option5 = driver.find_element(By.XPATH, homepsgeElements.resource_option5)
    Resource_option5.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/currency/"
    if driver.current_url == expected_url:
        print("Currency Encyclopedia Option Click Successfully and Correct Page Open")
    else:
        print("Currency Encyclopedia Option Not Work")
resource_select_button()
time.sleep(3)
driver.back()








# Resources option Currency News Letter
def resource_select_button():
    actions = ActionChains(driver)
    resource_selection = driver.find_element(By.XPATH,  homepsgeElements.resource)
    actions.move_to_element(resource_selection).perform()
    Resource_option6 = driver.find_element(By.XPATH, homepsgeElements.resource_option6)
    Resource_option6.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/currencyemail/"
    if driver.current_url == expected_url:
        print("Currency News Letter Option Click Successfully and Correct Page Open")
    else:
        print("Currency News Letter Option Not Work")
resource_select_button()
time.sleep(2)
driver.back()






# Resources option Glossary
def resource_select_button():
    actions = ActionChains(driver)
    resource_selection = driver.find_element(By.XPATH,  homepsgeElements.resource)
    actions.move_to_element(resource_selection).perform()
    Resource_option7 = driver.find_element(By.XPATH, homepsgeElements.resource_option7)
    Resource_option7.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/"
    if driver.current_url == expected_url:
        print("Glossary Option Click Successfully and Correct Page Open")
    else:
        print("Glossary Option Not Work")
resource_select_button()
time.sleep(2)






# Resources option More Resource
def resource_select_button():
    actions = ActionChains(driver)
    resource_selection = driver.find_element(By.XPATH,  homepsgeElements.resource)
    actions.move_to_element(resource_selection).perform()
    Resource_option8 = driver.find_element(By.XPATH, homepsgeElements.resource_option8)
    Resource_option8.click()
    driver.implicitly_wait(5)
    expected_url = "https://www.xe.com/learn/"
    if driver.current_url == expected_url:
        print("More Resource Option Click Successfully and Correct Page Open")
    else:
        print("More Resource Option Not Work")
resource_select_button()
time.sleep(2)
driver.back()






# Sign In option Money Transfer
def sign_in_select_button():
    actions = ActionChains(driver)
    sign_in_selection = driver.find_element(By.XPATH,  homepsgeElements.sign_in)
    actions.move_to_element(sign_in_selection).perform()
    sign_in_option1 = driver.find_element(By.XPATH, homepsgeElements.sign_in_money_transfer)
    sign_in_option1.click()
    driver.implicitly_wait(5)
    expected_url = "https://account.xe.com/signin/?icid=XECOM:Home:LoginBut:Login:Glob:HPXEMTLogin&ctaPosition=header"
    if driver.current_url == expected_url:
        print("Money Transfer Option Click Successfully and Correct Page Open")
    else:
        print("Money Transfer Option Not Work")
sign_in_select_button()
time.sleep(2)
driver.back()







# Sign In option Rate Alert
def sign_in_select_button():
    actions = ActionChains(driver)
    sign_in_selection = driver.find_element(By.XPATH,  homepsgeElements.sign_in)
    actions.move_to_element(sign_in_selection).perform()
    sign_in_option2 = driver.find_element(By.XPATH, homepsgeElements.sign_in_rate_alerts)
    sign_in_option2.click()
    driver.implicitly_wait(5)
    expected_url = "https://accounts.xe.com/login?client_id=68pd6tgjc1s83divlnc1bgrbqo&redirect_uri=https%3A%2F%2Fxera.xe.com&response_type=code&scope=openid"
    if driver.current_url == expected_url:
        print("Rate Alert Option Click Successfully and Correct Page Open")
    else:
        print("Rate Alert Option Not Work")
sign_in_select_button()
time.sleep(2)
driver.back()








# Register option Money Transfer
def register_select_button():
    actions = ActionChains(driver)
    register_selection = driver.find_element(By.XPATH,  homepsgeElements.register)
    actions.move_to_element(register_selection).perform()
    register_option1 = driver.find_element(By.XPATH, homepsgeElements.register_money_transfer)
    register_option1.click()
    driver.implicitly_wait(5)
    expected_url = "https://account.xe.com/signup?redirect_uri=https%3A%2F%2Fpersonal-registration.xe.com&ctaPosition=header"
    if driver.current_url == expected_url:
        print("Money Transfer Option Click Successfully and Correct Page Open")
    else:
        print("Money Transfer Option Not Work")
register_select_button()
time.sleep(2)
driver.back()








# Register option Rate Alert
def register_select_button():
    actions = ActionChains(driver)
    register_selection = driver.find_element(By.XPATH,  homepsgeElements.register)
    actions.move_to_element(register_selection).perform()
    register_option2 = driver.find_element(By.XPATH, homepsgeElements.register_rate_alerts)
    register_option2.click()
    driver.implicitly_wait(5)
    expected_url = "https://accounts.xe.com/signup?client_id=68pd6tgjc1s83divlnc1bgrbqo&redirect_uri=https%3A%2F%2Fxera.xe.com&response_type=code&scope=openid"
    if driver.current_url == expected_url:
        print("Rate Alert Option Click Successfully and Correct Page Open")
    else:
        print("Rate Alert Option Not Work")
register_select_button()
time.sleep(2)
driver.back()





driver.quit()