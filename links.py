from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.expected_conditions.title_is()


options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get('https://demoqa.com/')
driver.maximize_window()

element = driver.find_element(By.CSS_SELECTOR, 'div.home-body > div > div:nth-child(1)').click()

# # # action = ActionChains(driver)
# links = driver.find_element(By.XPATH, '//*[@id="item-5"]')
# print(links)
# links.click()
driver.execute_script("window.scrollBy(0, 250)")
link = wait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//li/span[text()="Links"]'))).click()

def home():
    home = driver.find_element(By.CSS_SELECTOR, "#simpleLink").click()
    driver.implicitly_wait(10)
    # print(home.get_attribute('href'))
    print(driver.current_url)
    # assert driver.current_url == "https://demoqa.com/"
    print("Href Value = ", home.get_attribute("href"))


def new():
    # Store the ID of the original window
    original_window = driver.current_window_handle

    # Check we don't have other windows open already
    assert len(driver.window_handles) == 1

    # Click the link which opens in a new window
    driver.find_element(By.CSS_SELECTOR, "#simpleLink").click()

    # Wait for the new window or tab
    wait(driver, 10).until(EC.number_of_windows_to_be(2))

    # Loop through until we find a new window handle
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    # Wait for the new tab to finish loading content
    wait(driver, 60).until(EC.title_is("DEMOQA"))
    print(EC.title_is("DEMOQA"))


def created():
    driver.find_element(By.CSS_SELECTOR, "#created").click()
    driver.implicitly_wait(5)
    assert driver.find_element(By.CSS_SELECTOR, "#linkResponse").is_displayed() == True
    assert driver.find_element(By.CSS_SELECTOR, "#linkResponse").text == "Link has responded with staus 201 and status text Created";


def no_content():
    driver.find_element(By.CSS_SELECTOR, "#no-content").click()
    driver.implicitly_wait(5)
    assert driver.find_element(By.CSS_SELECTOR, "#linkResponse").is_displayed() == True
    assert driver.find_element(By.CSS_SELECTOR, "#linkResponse").text == "Link has responded with staus 204 and status text No Content";


def moved():
    driver.find_element(By.CSS_SELECTOR, "#moved").click()
    driver.implicitly_wait(5)
    assert driver.find_element(By.CSS_SELECTOR, "#linkResponse").is_displayed() == True
    assert driver.find_element(By.CSS_SELECTOR, "#linkResponse").text == "Link has responded with staus 301 and status text Moved Permanently";


def bad_request():
    driver.find_element(By.CSS_SELECTOR, "#bad-request").click()
    driver.implicitly_wait(5)
    assert driver.find_element(By.CSS_SELECTOR, "#linkResponse").is_displayed() == True
    assert driver.find_element(By.CSS_SELECTOR, "#linkResponse").text == "Link has responded with staus 400 and status text Bad Request";
    


def unauthorized():
    driver.find_element(By.CSS_SELECTOR, "#unauthorized").click()
    driver.implicitly_wait(5)
    assert driver.find_element(By.CSS_SELECTOR, "#linkResponse").is_displayed() == True
    assert driver.find_element(By.CSS_SELECTOR, "#linkResponse").text == "Link has responded with staus 401 and status text Unauthorized";
    

def forbidden():
    driver.find_element(By.CSS_SELECTOR, "#forbidden").click()
    driver.implicitly_wait(5)
    assert driver.find_element(By.CSS_SELECTOR, "#linkResponse").is_displayed() == True
    assert driver.find_element(By.CSS_SELECTOR, "#linkResponse").text == "Link has responded with staus 403 and status text Forbidden";


def not_found():
    driver.implicitly_wait(5)
    driver.find_element(By.CSS_SELECTOR, "#invalid-url").click()
    assert driver.find_element(By.CSS_SELECTOR, "#linkResponse").is_displayed() == True
    assert driver.find_element(By.CSS_SELECTOR, "#linkResponse").text == "Link has responded with staus 404 and status text Not Found";
    















# new()
# home()
# created()
# no_content()
# moved()
# bad_request()
# unauthorized()
# forbidden()
# not_found()

driver.close()