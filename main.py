from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get('https://orteil.dashnet.org/cookieclicker/')
driver.maximize_window()
driver.implicitly_wait(5)
language = driver.find_element(By.ID, "langSelect-EN")
bigCookie = driver.find_element("xpath", "//button[@id='bigCookie']")
language.click()
for i in range(10):
    bigCookie.click()



# cookie_count = driver.find_element(By.ID, "cookies")
# items = [driver.find_element(By.ID, "productPrice" + str(i))
#          for i in range(1, -1, -1)]
# driver.execute_script("arguments[0].click();", language)
# for i in range(5000):
#     driver.execute_script("arguments[0].click();", cookie)