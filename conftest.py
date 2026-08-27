import pytest
from playwright.sync_api import sync_playwright
from UIAuto.Utils.config_reader import get_config


@pytest.fixture(scope="session") # it will execute only once per the session
def config():
    return get_config()


@pytest.fixture() # by default scope is function
def browser(config):
    # this is setup
    print("****** Browser fixture start *******")
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=config["headless"], slow_mo=5000
        )
        yield browser
        # teardown
        browser.close()
    print("******* Browser fixture end ******")


@pytest.fixture
def page(browser, config):
    print("********** page started *********")
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(config["timeout"])
    page.goto(config["base_url"])
    yield page
    context.close()
    print("********* page end *********")

"""
@pytest.fixture
def fixture_a():
    print("setup a")
    yield "A"
    print("teardown A")

@pytest.fixture
def fixture_b(fixture_a):
    print("setup b")
    yield "B"
    print("teardown B")


@pytest.fixture(autouse=True)
def fixture_c():
    print("setup c")
    yield
    print("teardown c")

"""