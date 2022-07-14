from behave import *
from pageObjects import PermitVehicle
from selenium.webdriver.remote.webelement import WebElement


@when('user looksup {vrm:w}')
def user_looks_up(context, vrm:str):
    vehicle_page: PermitVehicle
    vehicle_page = context.vrm_lookup_page
    context.vehicle_details = vehicle_page.lookup_vrm(vrm)

@then('vehicle colour is displayed as {colour:w}')
def check_vehicle_colour(context, colour:str):
    colour = f'colour {colour}'
    vehicle_details: list[WebElement]
    vehicle_details = context.vehicle_details
    result = vehicle_details[2].text.lower()
    assert result == colour.lower(), f'expected "{colour}" but got "{result}"'

@then('vehicle make is displayed as {make:w}')
def check_vehicle_make(context, make:str):
    make = f'make {make}'
    vehicle_details: list[WebElement]
    vehicle_details = context.vehicle_details
    result = vehicle_details[1].text.lower()
    assert result == make.lower(), f'expected "{make}" but got "{result}"'