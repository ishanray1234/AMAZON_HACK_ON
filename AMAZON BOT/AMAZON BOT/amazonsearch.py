from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# webdriver_path = 'E:/SELINIUM BOTS/CHROME_DRIVER/chromedriver.exe'
chrome_options = Options()
chrome_options.add_argument("--headless")

# service = Service(executable_path=webdriver_path)
driver = webdriver.Chrome(options=chrome_options)


driver.get('https://www.amazon.in/')


# Here we use the filter link
search_query = 'apple watch series 8'
search_bar = driver.find_element(By.ID, 'twotabsearchtextbox')
search_bar.send_keys(search_query)
search_bar.submit()


current_url = driver.current_url

driver.quit()


print("Current webpage URL:", current_url)
