from my_tes.case_3.pages.header_nav import HeaderNav


class PageInCommon:
    def __init__(self, driver):
        self.header_navbar = HeaderNav(driver)
