from openapi_schema_to_json_schema import to_json_schema as convert


def test_handles_nullable():
    schema = {
        "type": 'string',
        "nullable": True,
    }
    result = convert(schema)
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": ['string', 'null'],
    }
    assert result == expected

    schema = {
        "type": 'string',
        "nullable": False,
    }
    result = convert(schema)
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'string'
    }
    assert result == expected
