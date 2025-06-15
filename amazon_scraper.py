# amazon_scraper.py

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")

product = input("Enter the product to track (e.g. wireless earbuds): ")

search_input = driver.find_element(By.ID, 'twotabsearchtextbox')
search_input.send_keys(product)
search_button = driver.find_element(By.ID, 'nav-search-submit-button')
search_button.click()

product_urls = []

# Get product links from 2 pages
for _ in range(2):
    time.sleep(3)
    links = driver.find_elements(By.XPATH, '//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
    product_urls += [link.get_attribute('href') for link in links]
    
    try:
        next_page = driver.find_element(By.XPATH, '//a[contains(@class,"s-pagination-next")]')
        next_page.click()
    except NoSuchElementException:
        break

brand, name, price, return_policy, delivery, availability = [], [], [], [], [], []

for url in product_urls[:20]:
    driver.get(url)
    time.sleep(2)

    def get(xpath):
        try:
            return driver.find_element(By.XPATH, xpath).text
        except:
            return "-"

    brand.append(get('//tr[./th[contains(text(),"Brand")]]/td'))
    name.append(get('//span[@id="productTitle"]'))
    price.append(get('//span[@class="a-price-whole"]'))
    return_policy.append(get('//div[@id="merchant-info"]'))
    delivery.append(get('//div[@id="ddmDeliveryMessage"]/b'))
    availability.append(get('//div[@id="availability"]//span'))

df = pd.DataFrame({
    "Product Title": name,
    "Brand": brand,
    "Price (INR)": price,
    "Return Policy": return_policy,
    "Delivery Info": delivery,
    "Availability": availability,
    "URL": product_urls[:20]
})

df.to_csv("amazon_product_report.csv", index=False)
print("✅ Report saved as 'amazon_product_report.csv'")
driver.quit()
