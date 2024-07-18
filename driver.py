from selenium.webdriver import Chrome


class Driver(Chrome):
    def __init__(self, *args, **kwards):
        super().__init__(*args, **kwards)
        self.implicitly_wait(5)
