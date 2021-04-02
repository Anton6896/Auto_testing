from my_tes.case_1.pages.navigation import HeaderNav


class PageBase:
    """
    provide accesses to navbar thu all pages
    """

    def __init__(self, driver):
        self.header_nav = HeaderNav(driver)