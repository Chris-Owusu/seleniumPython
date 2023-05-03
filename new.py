from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import json

with open("data.json", "w") as f:
    json.dump([], f)

def write_json(new_data, filename='data.json'):
    with open(filename, 'r+') as file:
        # First we load exiting data into a dict
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data.append(new_data)
        # set current file position to offset
        file.seek(0)
        # convert back to jsone
        json.dump(file_data, file, indent=4)

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)

browser.get('https://www.amazon.com/')
assert 'Amazon' in browser.title
assert 'https://www.amazon.com/' in browser.current_url

browser.maximize_window()

searchBar = browser.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
searchBar.send_keys('sneakers for men' + Keys.RETURN)
# browser.refresh()
# browser.back()
# browser.forward()

isNextDisabled = False

while not isNextDisabled:
    try:
        result = browser.find_element(By.XPATH, "//div[@class='s-main-slot s-result-list s-search-results sg-row']")
        items = browser.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')

        for item in items:
            title = item.find_element(By.TAG_NAME, 'h2').text
            price = "Price not found"
            img =  "Image not found"
            productLink = browser.find_element(By.CLASS_NAME, "a-link-normal").get_attribute('href')
            deliveryToGhana = "Delivery information not found"

            try:
                price = item.find_element(By.CSS_SELECTOR, ".a-price").text.replace("\n", ".")
            except:
                pass

            try:
                img = item.find_element(By.CSS_SELECTOR, ".s-image").get_attribute('src')
            except:
                pass

            try:
                deliveryToGhana = item.find_element(By.CSS_SELECTOR, "div.a-section.a-spacing-small.puis-padding-left-small.puis-padding-right-small > div:nth-child(4) > div:nth-child(1)").text
                assert "Ships to Ghana" in item.find_element(By.CSS_SELECTOR, 'a-row').text
            except:
                pass

            print("Title: " + title)
            print("Price: " + price)
            print("Image: " + img)
            print("Product Link: " + productLink)
            print("Delivery to Ghana: " + deliveryToGhana)
            print('\n')

            write_json({
                "title": title,
                "price": price,
                "img": img,
                "productLink": productLink,
                "deliveryToGhana": deliveryToGhana
            })

    
        nxtBtn = wait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".s-pagination-next")))
        nxtClass = nxtBtn.get_attribute('class')
        if 's-pagination-disabled' in nxtClass:
            isNextDisabled = True
            break
        else:  
            browser.find_element(By.CSS_SELECTOR, ".s-pagination-next").click()
        
    except Exception as e:
        print(f"{e} + Main Error")
        isNextDisabled = True
        

browser.quit()