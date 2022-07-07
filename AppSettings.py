from __future__ import annotations
from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class AppSettings:
    permit: PermitSettings

@dataclass
class PermitSettings:
    url: str
    welcome_page: bool

def get_application_settings() -> AppSettings:
    with open("AppSettings.json") as open_file:
        file = open_file.read()

    return AppSettings.from_json(file)

