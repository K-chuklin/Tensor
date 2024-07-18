import os
import logging
import pytest
from driver import Driver


project_root = os.path.abspath(os.getcwd())
download_folder = 'Tensor'
download_path = os.path.join(project_root, download_folder)


logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Формат сообщений
    handlers=[
        logging.StreamHandler(),  # Вывод логов в консоль
        logging.FileHandler('app.log')  # Запись лога
    ])

# Создание логгера
logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def browser() -> Driver:
    driver = Driver()
    driver.get("https://sbis.ru/")
    # options = webdriver.ChromeOptions()
    # preferences = {"download.default_directory": download_path}
    yield driver

    driver.quit()
