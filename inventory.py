from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def open_hamburger_menu(self):
        menu_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
        )
        menu_button.click()
        

    def reset_app_state(self):
        self.open_hamburger_menu()

        reset_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "reset_sidebar_link"))
        )
        reset_button.click()

        # Close menu to avoid overlay issues
        close_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "react-burger-cross-btn"))
        )
        close_button.click()

    def add_first_n_items(self, n):
        buttons = self.wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "btn_inventory"))
        )

        for i in range(min(n, len(buttons))):
            buttons[i].click()

    def sort_z_to_a(self):
        dropdown = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "product_sort_container"))
        )
        Select(dropdown).select_by_visible_text("Name (Z to A)")

    def go_to_cart(self):
        cart_icon = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        )
        cart_icon.click()

    def logout(self):
        self.open_hamburger_menu()
        logout_link = self.wait.until(
            EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
        )
        logout_link.click()