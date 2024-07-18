import logging
from selenium.webdriver.common.by import By
from driver import Driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Sbis:
    contacts_link_xpath = '//*[@id="wasaby-content"]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/a'
    download_link_xpath = '//*[@id="container"]/div[2]/div[1]/div[3]/div[3]/ul/li[8]/a'
    download_xpath = '//*[@id="ws-q4tsjjllwyb1721329569792"]/div[1]/div[2]/div[2]/div/a'

    @staticmethod
    def go_on_the_contacts_link(driver: Driver):
        element = driver.find_element(By.XPATH, Sbis.contacts_link_xpath)
        element.click()

    @staticmethod
    def go_on_the_download_page(driver: Driver):
        element = driver.find_element(By.XPATH, Sbis.download_link_xpath)
        element.click()

    # @staticmethod
    # def download_file(driver: Driver):
    #     try:
    #         element = WebDriverWait(driver, 10).until(
    #             EC.visibility_of_element_located((By.XPATH, Sbis.download_xpath))
    #         )
    #         element.click()
    #     except Exception as e:
    #         logging.error(f"An unexpected error occurred: {e}")
