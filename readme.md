# Readme

This is an MS Edge selenium test package for user workflow through the KVL application. We have added BDD testing using the package behave, allowing us to make tests from gherkin feature files.

## What is currently being worked on?

Looking at converting test complete tests for the permit application into gherkin.

## How should my app setting json look?

Reminder the app setting file should be in the c:\ drive. This is used for CI to ensure confidential information is not shared.

```json
{
    "permit": {
        "url": "",
        "welcome_page": true
    },
    "headless": true,
    "test_card": {
        "card_number": "",
        "expiry_month": "",
        "expiry_year": "",
        "security_code": ""
    }
}
```

## how do i run the tests localy?

Ensure you have the latest version of python installed
in a command console run the following:

```bash
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    behave
```
