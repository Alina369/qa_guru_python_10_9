from selene import browser, be, by
from selene.support.shared.jquery_style import s


def test_github():
    browser.open("https://github.com")

    s(".header-search-button").click()
    # browser.element(".header-search-button").type('eroshenkoam/allure-example').press_enter()
    # s(".header-search-button").send_keys("eroshenkoam/allure-example")
    browser.element("#query-builder-test").should(be.visible).send_keys('').press_enter()
    s(".header-search-button").submit()

    s(by.link_text("eroshenkoam/allure-example")).click()

    s("#issues-tab").click()

    s(by.partial_text("#76")).should(be.visible)
