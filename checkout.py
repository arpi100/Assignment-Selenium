from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_info(self, first, last, zip_code):
        self.wait.until(EC.element_to_be_clickable((By.ID, "first-name"))).send_keys(first)
        self.wait.until(EC.element_to_be_clickable((By.ID, "last-name"))).send_keys(last)
        self.wait.until(EC.element_to_be_clickable((By.ID, "postal-code"))).send_keys(zip_code)
        self.wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()

    def get_total_price(self):
        return self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
        ).text

    def finish(self):
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "finish"))
        ).click()

    def success_message(self):
        return self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
        ).text