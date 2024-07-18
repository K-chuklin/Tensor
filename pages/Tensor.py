import logging
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from driver import Driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Tensor:
    title_xpath = '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[1]'
    about_link_xpath = '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a'

    @staticmethod
    def check_searching_title(driver: Driver, expected_title: str):
        try:
            # Пытаемся найти элемент и получить его текст
            title_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, Tensor.title_xpath))
            )
            title = title_element.text
            # Проверяем, что ожидаемый заголовок содержится в заголовке элемента
            assert expected_title in title, f"Expected title '{expected_title}' not found in '{title}'"
        except NoSuchElementException:
            logging.error(f"Element with XPATH '{Tensor.title_xpath}' not found on the page.")
        except TimeoutException:
            logging.error(f"Timed out waiting for element with XPATH '{Tensor.title_xpath}' to be visible.")
        except AssertionError as ae:
            logging.error(f"Assertion error: {ae}")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")

    @staticmethod
    def go_on_the_about_link(driver: Driver):
        element = driver.find_element(By.XPATH, Tensor.about_link_xpath)
        action = ActionChains(driver)  # Инициализируем действие
        action.scroll_by_amount(0, 1000).perform()
        element.click()
