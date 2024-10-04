from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service  # Import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


profile_path = r'/home/mateo/.mozilla/firefox/v31x69ag.default-release'
options = Options()
options.add_argument("--headless")
options.profile = webdriver.FirefoxProfile(profile_path)
service = Service("/usr/bin/geckodriver")
driver = webdriver.Firefox(service=service, options=options)
driver.get("https://myactivity.google.com/page?utm_source=my-activity&hl=hu&page=youtube_comments")
while True:
    # Wait until the element is located
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    "c-wiz.xDtZAf:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1) > svg:nth-child(3)"))
    )
    element.click()
