from openapi_schema_to_json_schema import to_json_schema as convert


def test_items():
    schema = {
        "type": 'array',
        "items": {
            "type": 'string',
            "format": 'date-time',
            "example": '2017-01-01T12:34:56Z'
        }
    }
    result = convert(schema)
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'array',
        "items": {
            "type": 'string',
            "format": 'date-time'
        }
    }
    assert result == expected
