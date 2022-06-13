from jsonschema.validators import validate


def check_default_response(response, status_code, response_type, message):
    assert response.status_code == status_code
    assert response.type == response_type
    assert response.message.lower() == message


def check_login_response(response, status_code, response_type, message):
    assert response.status_code == status_code
    assert response.type == response_type
    assert message in response.message


def validate_user(response, status_code, expected_user):
    assert response.status_code == status_code
    assert response.user == expected_user


def validate_order(response, status_code, expected_order):
    assert response.status_code == status_code
    assert response.order == expected_order


def validate_pet(response, status_code, expected_pet):
    assert response.status_code == status_code
    assert response.pet == expected_pet


def validate_json_schema(response_json, schema):
    validate(instance=response_json, schema=schema())
