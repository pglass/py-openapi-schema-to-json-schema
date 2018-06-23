from openapi_schema_to_json_schema import to_json_schema as convert


def test_properties():
    schema = {
        "type": 'object',
        "required": ['bar'],
        "properties": {
            "foo": {
                "type": 'string',
                "example": '2017-01-01T12:34:56Z'
            },
            "bar": {
                "type": 'string',
                "nullable": True
            }
        }
    }
    result = convert(schema)
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'object',
        "required": ['bar'],
        "properties": {
            "foo": {
                "type": 'string',
            },
            "bar": {
                "type": ['string', 'null']
            }
        }
    }
    assert result == expected


def test_additionalProperties_is_false():
    schema = {
        "type": 'object',
        "properties": {
            "foo": {
                "type": 'string',
                "example": '2017-01-01T12:34:56Z'
            }
        },
        "additionalProperties": False
    }
    result = convert(schema)
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'object',
        "properties": {
            "foo": {
                "type": 'string',
            }
        },
        "additionalProperties": False
    }
    assert result == expected


def test_additionalProperties_is_true():
    schema = {
        "type": 'object',
        "properties": {
            "foo": {
                "type": 'string',
                "example": '2017-01-01T12:34:56Z'
            }
        },
        "additionalProperties": True
    }
    result = convert(schema)
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'object',
        "properties": {
            "foo": {
                "type": 'string',
            }
        },
        "additionalProperties": True
    }
    assert result == expected


def test_additionalProperties_is_an_object():
    schema = {
        "type": 'object',
        "properties": {
            "foo": {
                "type": 'string',
                "example": '2017-01-01T12:34:56Z'
            }
        },
        "additionalProperties": {
            "type": 'object',
            "properties": {
                "foo": {
                    "type": 'string',
                    "format": 'date-time'
                }
            }
        }
    }
    result = convert(schema)
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'object',
        "properties": {
            "foo": {
                "type": 'string',
            }
        },
        "additionalProperties": {
            "type": 'object',
            "properties": {
                "foo": {
                    "type": 'string',
                    "format": 'date-time'
                }
            }
        }
    }
    assert result == expected
