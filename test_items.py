# команды запуска:
# pytest --language=fr test_items.py
# pytest --language=es test_items.py

from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

# браузер передается в тест как параметр
# название метода соответствует задача (проверка существования кнопки добавления в корзину)
def test_add_to_basket_button_exist(browser):
    browser.get(link)

    # уникальный селектор: тэг button и значение атрибута type 'submit', такое только у этой кнопки
    button = browser.find_elements(By.XPATH, "//button[@type='submit']")
    # чтобы проверить работоспособность assert'a, можно раскомментить строку
    # ниже (с селектором //submit), и закомментить строку выше (с правильным селектором),
    # тогда тест упадет и в short test summary info ты увидишь assertion-message
    # button = browser.find_elements(By.XPATH, "//submit")
    assert button, 'THERE IS NO ADD BUTTON ON THIS PAGE, SO SAD :('
    # таймаут для визуальной проверки правильности языка, если надо, поставь побольше
    time.sleep(15)

