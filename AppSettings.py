from __future__ import annotations
from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass
class PermitSettings:
    url: str
    welcome_page: bool

@dataclass
class VehicleDetails:
    vrm: str
    colour: str
    make: str

@dataclass
class TestCardDetails:
    card_number: str
    expiry_month: str
    expiry_year: str
    security_code: str

@dataclass_json
@dataclass
class AppSettings:
    test_card: TestCardDetails
    permit: PermitSettings
    headless: bool
    vehicle_details: VehicleDetails





def get_application_settings() -> AppSettings:
    with open("c:\AppSettings.json", "r") as open_file:
        file = open_file.read()

    return AppSettings.from_json(file)

