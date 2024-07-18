import logging

from selenium.common import WebDriverException, NoSuchElementException
from selenium.webdriver.common.by import By
from driver import Driver


class TensorAbout:

    @staticmethod
    def check_about_url(driver: Driver, expected_url: str):
        try:
            # Получаем текущий URL
            current_url = driver.current_url
            # Проверяем, что ожидаемый URL содержится в текущем URL
            assert expected_url in current_url, f"Expected URL '{expected_url}' not found in '{current_url}'"
        except AssertionError as ae:
            logging.error(f"Assertion error: {ae}")
        except WebDriverException as we:
            logging.error(f"WebDriverException occurred: {we}")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")

    @staticmethod
    def check_images_size(driver: Driver):
        pairs_list = []
        try:
            for _ in range(1, 5):
                # Пытаемся найти элементы и получить их атрибуты
                image_element = driver.find_element(By.XPATH,
                                                    f'//*[@id="container"]/div[1]/div/div[4]/div[2]/div[{_}]/a/div[1]/div')
                image_width = image_element.get_attribute("width")
                image_height = image_element.get_attribute("height")
                pairs_list.append((image_width, image_height))

            # Проверяем, что все пары равны первой паре
            assert all(pair == pairs_list[0] for pair in pairs_list), \
                f"Не все размеры изображений совпадают: {pairs_list}"
        except NoSuchElementException as e:
            logging.error(f"Element not found: {e}")
        except WebDriverException as we:
            logging.error(f"WebDriverException occurred: {we}")
        except AssertionError as ae:
            logging.error(f"Assertion error: {ae}")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
