import time

# @pytest.mark.parametrize()
class TestSelenium1py(object):
    def test_button_add_card(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(30)
        assert len(browser.find_elements_by_css_selector(".btn-add-to-basket")) > 0, \
               "Кнопка добавить в корзину не найдена!"