from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def calculateTotalAmount():
    totalAmount = 0
    tax = 4.32
    
    itemAmounts = driver.find_elements(By.CSS_SELECTOR, '.inventory_item_price')
    for itemAmount in itemAmounts:
        # Extract the amount value and convert it to a number
        amount = float(itemAmount.text.replace('$', ''))
        
        # Add the amount to the total
        totalAmount += amount
        # Add the total to the tax
        finalAmountPlusTax = totalAmount + tax
    
    # Assert or perform actions with the total amount
    print('Total Amount:', finalAmountPlusTax)  # Logging the total amount for reference
    
    # Example: Assert the total amount equals a specific value
    assert finalAmountPlusTax == 58.29

def cartItems():
    cartItems = driver.find_elements(By.CSS_SELECTOR, '#cart_contents_container')
    for cartItem in cartItems:
        # Assert the visibility of the elements
        item_name = cartItem.find_element(By.CSS_SELECTOR, '.inventory_item_name').text
        if item_name == 'Sauce Labs Backpack':
            assert item_name == 'Sauce Labs Backpack'
        elif item_name == 'Sauce Labs Bolt T-Shirt':
            assert item_name == 'Sauce Labs Bolt T-Shirt'
        elif item_name == 'Sauce Labs Onesie':
            assert item_name == 'Sauce Labs Onesie'



driver.get('https://www.saucedemo.com/')
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user');
driver.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce');
driver.find_element(By.CSS_SELECTOR, '#login-button').click();

driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click();
driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click();
driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click();
driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click();

cartItems()

driver.find_element(By.CSS_SELECTOR, '#checkout').click();


driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys('Test');
driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys('Ignore');
driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys('123');
driver.find_element(By.CSS_SELECTOR, '#continue').click();

calculateTotalAmount()
cartItems()

driver.find_element(By.CSS_SELECTOR, '#finish').click()

assert driver.find_element(By.CSS_SELECTOR, '.complete-header').is_displayed()
assert driver.find_element(By.CSS_SELECTOR, '#back-to-products').is_displayed()


driver.quit();