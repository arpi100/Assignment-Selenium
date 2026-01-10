from pages.login import LoginPage
from pages.inventory import InventoryPage
from pages.cart import CartPage
from pages.checkout import CheckoutPage

def test_performance(driver):
    LoginPage(driver).login("performance_glitch_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.reset_app_state()
    inventory.sort_z_to_a()
    inventory.add_first_n_items(1)
    inventory.go_to_cart()

    cart = CartPage(driver)
    cart.checkout()
    checkout = CheckoutPage(driver)
    checkout.fill_info("Arpita", "Majumder", "1200")

    checkout.finish()
    assert checkout.success_message() == "Thank you for your order!"

    inventory = InventoryPage(driver)
    inventory.reset_app_state()
    inventory.logout()