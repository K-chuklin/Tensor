import logging
from selenium.common import NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from driver import Driver
from location import get_ip_location
from transliterate import slugify


class SbisContacts:
    tensor_logo_xpath = '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a/img'
    location_link_xpath = '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span'
    sbis_contacts_link_xpath = '//*[@id="contacts_list"]/div/div[2]/div[2]'
    region_link_xpath = '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span'
    new_region_link_xpath = '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span'

    @staticmethod
    def go_on_the_tensor_logo(driver: Driver):
        element = driver.find_element(By.XPATH, SbisContacts.tensor_logo_xpath)
        element.click()
        driver.switch_to.window(driver.window_handles[1])

    @staticmethod
    def check_current_region(driver: Driver):
        try:
            # Ожидание, пока элемент станет видимым
            region_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, SbisContacts.location_link_xpath))
            )
            current_region = get_ip_location().split(' ')[0]

            # Ожидание обновления текста элемента
            WebDriverWait(driver, 10).until(
                EC.text_to_be_present_in_element((By.XPATH, SbisContacts.location_link_xpath), current_region)
            )

            # Проверяем, что текущий регион содержится в тексте элемента
            assert current_region in region_element.text, f"Expected region '{current_region}' " \
                                                          f"not found in '{region_element.text}'"
        except NoSuchElementException as e:
            logging.error(f"Element with XPATH '{SbisContacts.location_link_xpath}' not found on the page: {e}")
        except TimeoutException as te:
            logging.error(f"Timeout waiting for element or text update: {te}")
        except AssertionError as ae:
            logging.error(f"Assertion error: {ae}")
        except WebDriverException as we:
            logging.error(f"WebDriverException occurred: {we}")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")

    @staticmethod
    def check_sbis_contacts(driver: Driver):
        try:
            # Пытаемся найти все контакты
            contacts = driver.find_elements(By.XPATH, SbisContacts.sbis_contacts_link_xpath)
            for contact in contacts:
                assert contact in contacts, f"Contact '{contact.text}' not found in contacts list"
        except NoSuchElementException as e:
            logging.error(f"Element with XPATH '{SbisContacts.sbis_contacts_link_xpath}' not found on the page: {e}")
        except AssertionError as ae:
            logging.error(f"Assertion error: {ae}")
        except WebDriverException as we:
            logging.error(f"WebDriverException occurred: {we}")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")

    @staticmethod
    def check_region(driver: Driver):
        try:
            # Ожидание, пока элемент станет кликабельным
            title = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, SbisContacts.location_link_xpath))
            )
            title.click()

            # Получение списка контактов
            contacts_list = []
            contacts = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, SbisContacts.sbis_contacts_link_xpath))
            )
            for contact in contacts:
                contacts_list.append(contact.text)

            # Ожидание, пока элемент станет видимым
            location = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, SbisContacts.region_link_xpath))
            )

            new_title = location.text[3:]
            new_url = slugify(location.text.replace(" ", "-"))

            location.click()

            # Ожидание, пока URL обновится
            WebDriverWait(driver, 10).until(EC.url_contains(new_url))

            url = driver.current_url

            # Получение нового списка контактов
            new_contacts_list = []
            new_contacts = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, SbisContacts.sbis_contacts_link_xpath))
            )
            for contact in new_contacts:
                new_contacts_list.append(contact.text)

            # Проверки
            assert new_title in title.text, f'text {new_title} not in {title.text}'
            assert new_url in url, f'text {new_url} not in {url}'
            assert not [contact for contact in contacts_list if contact in new_contacts_list]

        except NoSuchElementException as e:
            logging.error(f"Element not found: {e}")
        except TimeoutException as e:
            logging.error(f"Timeout waiting for element or URL update: {e}")
        except AssertionError as e:
            logging.error(f"Assertion error: {e}")
        except WebDriverException as e:
            logging.error(f"WebDriverException occurred: {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
