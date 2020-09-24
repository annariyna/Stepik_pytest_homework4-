from selenium import webdriver


page_link = "http://selenium1py.pythonanywhere.com/fr/catalogue/coders-at-work_207/"

busket_submit_locator = ".btn.btn-lg.btn-primary.btn-add-to-basket"



def test_busket_button():
# Arrange
browser = webdriver.Chrome()
browser.get(page_link)
# Act
basket_button = browser.find_element_by_css_selector(busket_submit_locator)
#Assert
assert basket_button is not None, "Basket button was found"