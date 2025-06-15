# 🛍️ Amazon Competitive Intelligence Tool

**Goal**: Scrape Amazon.in product listings to track price, availability, and delivery estimates for competitive product analysis.

## 🔧 Technologies
- Python
- Selenium WebDriver
- Pandas
- ChromeDriver

## 💡 Features
- Input a product name (e.g. “wireless headphones”)
- Automatically scrapes 2 pages of Amazon results
- Extracts product name, brand, price, return policy, delivery date, and stock status
- Saves output to `amazon_product_report.csv`

## 📁 Example Output

| Product Title | Brand | Price (INR) | Return Policy | Delivery Info | Availability |
|---------------|-------|-------------|----------------|----------------|----------------|
| Boat Rockerz 255 | Boat | 999 | Returnable | Delivered by June 18 | In stock |

## 📜 Sample Code

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd, time

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
product = input("Enter product name: ")
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys(product)
driver.find_element(By.ID, "nav-search-submit-button").click()

# Then continue scraping...
