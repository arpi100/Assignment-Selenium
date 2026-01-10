import time
from pages.login import LoginPage
from pages.inventory import InventoryPage
from pages.cart import CartPage
from pages.checkout import CheckoutPage

def test_standard(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.reset_app_state()
    time.sleep(1)  
    inventory.add_first_n_items(3)
    inventory.go_to_cart()
    time.sleep(2)  
    cart = CartPage(driver)
    cart.checkout()
    time.sleep(2)  
    checkout = CheckoutPage(driver)
    checkout.fill_info("Arpita", "Majumder", "1200")
    time.sleep(2)  
    total = checkout.get_total_price()
    assert "Total" in total

    checkout.finish()
    assert checkout.success_message() == "Thank you for your order!"

    inventory = InventoryPage(driver)
    inventory.reset_app_state()
    inventory.logout()
