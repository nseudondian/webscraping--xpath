from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd

# To schedule periodic display
from datetime import datetime
import os
import sys

application_path = os.path.dirname(sys.executable)

now = datetime().now()

# convert time gotten from line 13 to string
detailed_time = now.strftime("%m%d%Y")

url = "https://www.cnbc.com/"
path = "Users\nseab\Downloads\chromedriver_win32/chromedriver.exe"

# Headless
options = Options()
options.headless = True

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)

driver.get(url)

containers = driver.find_elements(by="xpath", value='//*[@id="MainContentContainer"]')

# //*[@id="market-data-scroll-container"]/a[1]

titles = []

for container in containers:
   title = container.find_element(by="xpath", value='//*[@id="MainContentContainer"]').text
   titles.append(title)

dict_to_use = {"titles" : titles }
df_test = pd.DataFrame(dict_to_use)

file_name = f'/test-{detailed_time}.csv'
joined_path = os.path.join(application_path, file_name)

# Not using headless
# df_test.to_csv('test.csv')

# Using headless
# df_test.to_csv('test-headless.csv')

# Edit df_test to show datetime
df_test.to_csv(joined_path)

driver.quit()