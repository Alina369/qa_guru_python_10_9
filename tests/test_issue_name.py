from selene.support.shared.jquery_style import s
from selene import browser, be, by
import allure
from allure_commons.types import Severity

# Чистый тест на Selene
def test_git_issue_clear_selene():
    browser.open("https://github.com")

    s(".header-search-button").click()
    s("#query-builder-test").send_keys('eroshenkoam/allure-example').press_enter()

    s(by.link_text("eroshenkoam/allure-example")).click()

    s("#issues-tab").click()

    s("#issue_76_link").should(be.visible)
    allure.dynamic.severity(Severity.BLOCKER)

# Лямбда шаги через with allure.step
@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("Alina", "Lang")
@allure.feature("Git's Issue")
@allure.story("Пользователь видит Issue")
@allure.link("https://github.com", name="Testing")
def test_git_issue_with_decorator():
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Ищем репозиторий"):
        s(".header-search-button").click()
        s("#query-builder-test").send_keys('eroshenkoam/allure-example').press_enter()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открываем таб Issue"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие названия Issue"):
        s("#issue_76_link").should(be.visible)


# Шаги с декоратором @allure.step
def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue("#issue_76_link")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    s(".header-search-button").click()
    s("#query-builder-test").send_keys(repo).press_enter()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем наличие названия Issue {name}")
def should_see_issue(name):
    s(name).should(be.visible)
