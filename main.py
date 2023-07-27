import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import NoSuchElementException

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")


chrome_driver_path = "Users\Lenovo\Developer\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, executable_path=chrome_driver_path)
driver.maximize_window()
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3438293170&f_AL=true&geoId=102908739&keywords=junior%20python%20developer&location=Sofia%20City%2C%20Bulgaria&refresh=true")
time.sleep(2)
accept_button = driver.find_element(By.XPATH, '//*[@id="artdeco-global-alert-container"]/div/section/div/div[2]/button[1]')
accept_button.click()
sign_in_button = driver.find_element(By.CSS_SELECTOR, "body > div.base-serp-page > header > nav > div > a.nav__button-secondary.btn-md.btn-secondary-emphasis")
sign_in_button.click()

time.sleep(2)
username = driver.find_element(By.ID, "username")
username.send_keys(EMAIL)
password = driver.find_element(By.ID, "password")
password.send_keys(PASSWORD)
log_in_button = driver.find_element(By.CSS_SELECTOR, "#organic-div > form > div.login__form_action_container > button")
log_in_button.click()
time.sleep(2)
all_listings = driver.find_elements(By.CSS_SELECTOR, '#ember123 > div > div.job-card-container.relative.job-card-list.job-card-container--clickable.job-card-list--underline-title-on-hover.jobs-search-two-pane__job-card-container--viewport-tracking-0')
for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    try:
        apply = driver.find_element(By.CSS_SELECTOR, '#ember345')
        apply.click()
        time.sleep(5)
        phone_fill = driver.find_element(By.CLASS_NAME,  "artdeco-text-input--input")
        if phone_fill.text == "":
            phone_fill.send_keys("222875122")
        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")

        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(By.XPATH, '//*[@id="ember367"]/li-icon/svg/path')
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_element(By.XPATH, '//*[@id="ember409"]')
            discard_button.click()
            print("Complex application, skipped.")
            continue

    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
