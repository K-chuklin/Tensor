from driver import Driver
from pages.Sbis import Sbis
from pages.SbisContacts import SbisContacts
from pages.Tensor import Tensor
from pages.TensorAbout import TensorAbout


def test_first_case(browser: Driver):
    searching_title = 'Сила в людях'
    searching_url = 'https://tensor.ru/about'

    Sbis.go_on_the_contacts_link(browser)
    SbisContacts.go_on_the_tensor_logo(browser)
    Tensor.check_searching_title(browser, searching_title)
    Tensor.go_on_the_about_link(browser)
    TensorAbout.check_about_url(browser, searching_url)
    TensorAbout.check_images_size(browser)


def test_second_case(browser: Driver):

    Sbis.go_on_the_contacts_link(browser)
    SbisContacts.check_current_region(browser)
    SbisContacts.check_sbis_contacts(browser)
    SbisContacts.check_region(browser)


# Пока не удалось победить данный кейс
# def test_third_case(browser: Driver):
#     Sbis.go_on_the_download_page(browser)
#     Sbis.download_file(browser)
