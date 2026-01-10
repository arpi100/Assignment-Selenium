from pages.login import LoginPage

def test_locked(driver):
    login = LoginPage(driver)
    login.login("locked_out_user", "secret_sauce")
    assert "locked out" in login.get_error_message()