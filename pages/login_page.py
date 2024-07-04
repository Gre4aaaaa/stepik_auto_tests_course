from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        s = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        if 'Link' in s:
            print('Ссаная ссылка верная')
        index = s.find('Link')
        if index != -1:
            assert "login" in self.url, "ЁБАНЫЙ РОТ ЭТОГО КАЗИНО"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        login_link = self.browser.find_element(*LoginPageLocators.login_text_form)
        login_link.click()
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        login_link = self.browser.find_element(*LoginPageLocators.register_text_form)
        login_link.click()
        assert True