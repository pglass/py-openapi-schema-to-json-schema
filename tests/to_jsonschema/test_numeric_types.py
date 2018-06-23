from openapi_schema_to_json_schema import to_json_schema as convert


def test_handles_integer_types():
    schema = {
        "type": 'integer',
    }
    result = convert(schema)
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'integer',
    }
    assert result == expected

    schema = {
        "type": 'integer',
        "format": 'int32',
    }
    result = convert(schema)
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'integer',
        "format": 'int32',
    }
    assert result == expected


def test_handles_number_types():
    schema = {
        "type": 'number',
    }
    result = convert(schema)
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'number',
    }
    assert result == expected

    schema = {
        "type": 'number',
        "format": 'float',
    }
    result = convert(schema)
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'number',
        "format": 'float',
    }
    assert result == expected
