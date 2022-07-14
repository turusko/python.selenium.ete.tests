from behave import fixture
from BrowserObject import Browser

@fixture
def vrm_lookup(context):
    context.driver = Browser()
    context.landpage = context.driver.navigate_to_permits()
    context.vrm_lookup_page = context.landpage.click_next()