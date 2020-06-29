import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: es or fr")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = None
    if language == "en":
        print("\nstart test language en..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'en'})  # ru en
        browser = webdriver.Chrome(options=options)

    elif language == "es":
        print("\nstart test language es..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'es'})  # ru en
        browser = webdriver.Chrome(options=options)

    elif language == "fr":
        print("\nstart test language fr..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'fr'})  # ru en
        browser = webdriver.Chrome(options=options)
    else:
        print("\n--language should be es or fr")
    yield browser
    print("\nquit browser..")
    browser.quit()