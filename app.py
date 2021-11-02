import os
import time

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By


class Booster:
    def __init__(self) -> None:
        """
        Инициализация
        """
        self.f = Faker()
        self.url = os.getenv("YOU_REFERRAL_URL", False)
        if self.url is False:
            raise ValueError("Укажите вашу ссылку приглашения")
        self.browser = webdriver.Remote("http://selenium:4444")
        self.browser.implicitly_wait(5)
        self.browser.get(self.url)
        time.sleep(5)

    def __enter__(self) -> None:
        """
        Вход в контекстный менеджер
        """
        self.select_language()
        self.close_test()
        self.open_create_profile()
        self.set_age()
        self.set_name()
        self.set_email()
        self.set_password()
        self.submit_create_profile()

    def __exit__(self, type, value, traceback) -> None:
        """
        Выход из контекстного менеджера
        """
        self.browser.quit()

    def select_language(self) -> None:
        """
        Выбор языка для изучения
        """
        xpath = "//*[@id='root']/div/div/span/div/div/div/ul/button[8]"
        elem = self.browser.find_element(By.XPATH, xpath)
        elem.click()
        time.sleep(5)

    def close_test(self) -> None:
        """
        Пропуск теста на знание языка
        """
        xpath = "//*[@id='root']/div/div/div/div[1]/div/button"
        elem = self.browser.find_element(By.XPATH, xpath)
        elem.click()
        time.sleep(5)

    def open_create_profile(self) -> None:
        """
        Открыть форму создания профиля
        """
        xpath = "//*[@id='root']/div/div[4]/div/div/div[1]/div[2]/button[1]"
        elem = self.browser.find_element(By.XPATH, xpath)
        elem.click()
        time.sleep(2)

    def set_age(self) -> None:
        """
        Указать возраст
        """
        xpath = "//*[@id='overlays']/div[5]/div/div/form/div[1]/div[1]/div[1]/label/div/input"
        elem = self.browser.find_element(By.XPATH, xpath)
        self.account_age = self.f.random_int(14, 90)
        elem.send_keys(self.account_age)

    def set_name(self) -> None:
        """
        Указать имя
        """
        xpath = "//*[@id='overlays']/div[5]/div/div/form/div[1]/div[1]/div[2]/label/div/input"
        elem = self.browser.find_element(By.XPATH, xpath)
        self.account_name = self.f.name()
        elem.send_keys(self.account_name)

    def set_email(self) -> None:
        """
        Указать почту
        """
        xpath = "//*[@id='overlays']/div[5]/div/div/form/div[1]/div[1]/div[3]/label/div/input"
        elem = self.browser.find_element(By.XPATH, xpath)
        self.account_email = self.f.email()
        elem.send_keys(self.account_email)

    def set_password(self) -> None:
        """
        Указать пароль
        """
        xpath = "//*[@id='overlays']/div[5]/div/div/form/div[1]/div[1]/div[4]/label/div/input"
        elem = self.browser.find_element(By.XPATH, xpath)
        self.account_password = self.f.password()
        elem.send_keys(self.account_password)

    def submit_create_profile(self) -> None:
        """
        Подтвердить указанные данные
        """
        xpath = "//*[@id='overlays']/div[5]/div/div/form/div[1]/button"
        elem = self.browser.find_element(By.XPATH, xpath)
        elem.click()
        print(
            f"{self.account_name} {self.account_age} y.o {self.account_email}:{self.account_password}"
        )
        time.sleep(2)


if __name__ == "main":
    counter = os.getenv("COUNTER", False)
    if counter is False:
        raise ValueError("Укажите необходимое количество циклов")
    time.sleep(10)
    for i in range(1, counter):
        with Booster() as b:
            print(f"Created {i}")
