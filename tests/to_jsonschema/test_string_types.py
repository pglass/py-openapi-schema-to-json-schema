from openapi_jsonschema_converter import openapi_to_json_schema as convert


def test_plain_string_is_untouched():
    schema = {
        "type": 'string'
    }
    result = convert(schema)
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'string'
    }
    assert result == expected


def test_handling_date():
    schema = {
        "type": 'string',
        "format": 'date'
    }
    result = convert(schema)
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'string',
        "format": 'date'
    }
    assert result == expected

    schema = {
        "type": 'string',
        "format": 'date'
    }
    result = convert(schema, {'dateToDateTime': True})
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'string',
        "format": 'date-time'
    }
    assert result == expected


def test_retaining_custom_formats():
    schema = {
        "type": 'string',
        "format": 'email'
    }
    result = convert(schema)
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'string',
        "format": 'email'
    }
    assert result == expected
