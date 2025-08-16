import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://magento.softwaretestingboard.com/")
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Sign In").click()
driver.find_element(By.ID, "email").send_keys("seleniumdemo@yopmail.com")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@name='login[password]']").send_keys("Automate123")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "button[class='action login primary']").click()
time.sleep(5)
login_success = driver.find_element(By.CSS_SELECTOR, "div[class='panel header'] ul li span[class='logged-in']").text
assert "Welcome, Test User!" in login_success

# add to cart
driver.find_element(By.CSS_SELECTOR, "input[id='search']").send_keys("jack")
time.sleep(3)
jackets = driver.find_elements(By.CSS_SELECTOR, "li[role='option']")
for i in jackets:
    if i.text.__contains__("women"):
        i.click()
        break
title = driver.find_element(By.CSS_SELECTOR, ".page-title").text
assert "women" in title
driver.find_element(By.XPATH, "//li[@class='item product product-item'][5]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='swatch-attribute size']/div/div[3]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='swatch-option color'][3]").click()
time.sleep(2)
item_qty = driver.find_element(By.CSS_SELECTOR, "div[class='field qty'] div input")
item_qty.clear()
item_qty.send_keys('2')
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "button[class='action primary tocart']").click()
time.sleep(3)
driver.back()
time.sleep(3)
driver.find_element(By.XPATH, "//li[@class='item product product-item'][6]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='swatch-attribute size']/div/div[1]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='swatch-option color'][1]").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "button[class='action primary tocart']").click()
time.sleep(3)
# validate cart value
number_of_items = driver.find_element(By.CLASS_NAME, "counter-number")
assert number_of_items.text == '3'
driver.find_element(By.CLASS_NAME, "action.showcart").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "a[class='action viewcart']").click()
time.sleep(3)
prices = driver.find_elements(By.XPATH, "//td[@class='col price']/span/span/span")
qty = driver.find_elements(By.XPATH, "//input[@class='input-text qty']")
subtotal = driver.find_elements(By.XPATH, "//td[@class='col subtotal']/span/span")
# if multiple items in cart, and you need price of only the first element,
# then use XPATH = "//tbody[@class='cart item'][1]/tr[1]/td[2]/span/span"
# driver.find_element(By.CSS_SELECTOR, "a[class='action action-delete']").click()
time.sleep(2)
for price, quant, subtots in zip(prices, qty, subtotal):
    price_value = float(price.text[1:])
    qty_value = int(quant.get_attribute('value'))
    subtotal_value = float(subtots.text[1:])
    assert price_value * qty_value == subtotal_value

# delete from cart
# driver.find_element(By.XPATH, "//a[@class='action action-delete']").click()
driver.find_element(By.XPATH, "//tbody[@class='cart item'][2]/tr/td/div/a[3]").click()
time.sleep(5)
# cart_empty = driver.find_element(By.CLASS_NAME, ".cart-empty").text
# assert "You have no items in your shopping cart." in cart_empty

# edit cart to edit the first item in your cart. Same you can edit each item by traversing in a loop by changing the
# [1] in the below statement
# driver.find_element(By.XPATH, "a[class='action action-edit']").click()
driver.find_element(By.XPATH, "//tbody[@class='cart item'][1]/tr[@class='item-actions'][1]/td/div/a[2]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='swatch-attribute size']/div/div[3]").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "div[class='swatch-option color']:nth-of-type(1)").click()
time.sleep(2)
item_qty = driver.find_element(By.CSS_SELECTOR, "div[class='field qty'] div input")
item_qty.clear()
item_qty.send_keys('2')
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "button[class='action primary tocart']").click()
time.sleep(5)
update_success = driver.find_element(By.CSS_SELECTOR, "div[class='page messages']").text
assert "was updated in your shopping cart." in update_success
time.sleep(3)

# checkout
driver.find_element(By.XPATH, "//ul/li/button").click()
time.sleep(8)
driver.find_element(By.XPATH, "//input[@name='street[0]']").send_keys("Vijay Nagar")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "select[name='region_id']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "select[name='region_id'] option[data-title='Utah']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//input[@name='city']").send_keys("Salt Lake")
time.sleep(3)
driver.find_element(By.NAME, "postcode").send_keys('12345')
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "input[name='telephone']").send_keys('1234567890')
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "input[value='tablerate_bestway']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[contains(text(),'Next')]").click()
time.sleep(7)
# place_order = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[class='action primary checkout']")))
sub_total = driver.find_element(By.XPATH, "//tr[@class='totals sub']/td/span").text
shipping = driver.find_element(By.XPATH, "//tr[@class='totals shipping excl']/td/span").text
total = driver.find_element(By.XPATH, "//tr[@class='grand totals']/td/strong").text
float_sub_total = float(sub_total[1:])
float_shipping = float(shipping[1:])
float_total = float(total[1:])
assert (float_sub_total + float_shipping) == float_total
driver.find_element(By.CSS_SELECTOR, "button[class='action primary checkout']").click()
time.sleep(5)
order_success = driver.find_element(By.CSS_SELECTOR, "h1[class='page-title']").text
assert "Thank you for your purchase!" in order_success

# from home screen > search an element > add to wishlist
# driver.find_element(By.XPATH, "//li[@class='item product product-item'][9]/div/div/div/div/div[2]/a[1]").click()
# added_success = driver.find_element(By.XPATH, "//div[@role='alert']").text
# assert "been added to your Wish List." in added_success
