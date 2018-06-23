from openapi_jsonschema_converter import openapi_to_json_schema as convert


def test_iterate_allOfs():
    schema = {
        "allOf": [
            {
                "type": "object",
                "required": ["foo"],
                "properties": {
                    "foo": {
                        "type": "integer",
                        "format": "int64"
                    }
                }
            },
            {
                "allOf": [
                    {
                        "type": "number",
                        "format": "double"
                    }
                ]
            }
        ]
    }
    result = convert(schema)
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "allOf": [
            {
                "type": 'object',
                "required": ['foo'],
                "properties": {
                    "foo": {
                        "type": 'integer',
                        "format": 'int64'
                    }
                }
            },
            {
                "allOf": [
                    {
                        "type": 'number',
                        "format": 'double'
                    }
                ]
            }
        ]
    }
    assert result == expected


def test_iterate_anyOfs():
    schema = {
        "anyOf": [
            {
                "type": 'object',
                "required": ['foo'],
                "properties": {
                    "foo": {
                        "type": 'integer'
                    }
                }
            },
            {
                "anyOf": [
                    {
                        "type": 'object',
                        "properties": {
                            "bar": {
                                "type": 'number'
                            }
                        }
                    }
                ]
            }
        ]
    }
    result = convert(schema)
    expected = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "anyOf": [
            {
                "type": "object",
                "required": ["foo"],
                "properties": {
                    "foo": {
                        "type": "integer",
                    }
                }
            },
            {
                "anyOf": [
                    {
                        "type": "object",
                        "properties": {
                            "bar": {
                                "type": "number",
                            }
                        }
                    }
                ]
            }
        ]
    }
    assert result == expected


def test_iterate_oneOfs():
    schema = {
        "oneOf": [
            {
                "type": 'object',
                "required": ['foo'],
                "properties": {
                    "foo": {
                        "type": 'integer'
                    }
                }
            },
            {
                "oneOf": [
                    {
                        "type": 'object',
                        "properties": {
                            "bar": {
                                "type": 'number'
                            }
                        }
                    }
                ]
            }
        ]
    }
    result = convert(schema)
    expected = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "oneOf": [
            {
                "type": "object",
                "required": ["foo"],
                "properties": {
                    "foo": {
                        "type": "integer",
                    }
                }
            },
            {
                "oneOf": [
                    {
                        "type": "object",
                        "properties": {
                            "bar": {
                                "type": "number",
                            }
                        }
                    }
                ]
            }
        ]
    }
    assert result == expected


def test_converts_types_in_not():
    schema = {
        "type": 'object',
        "properties": {
            "not": {
                "type": 'string',
                "format": 'password',
                "minLength": 8
            }
        }
    }
    result = convert(schema)
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'object',
        "properties": {
            "not": {
                "type": 'string',
                "format": 'password',
                "minLength": 8
            }
        }
    }
    assert result == expected


def test_converts_types_in_not_2():
    schema = {
        "not": {
            "type": 'string',
            "format": 'password',
            "minLength": 8
        }
    }
    result = convert(schema)
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "not": {
            "type": 'string',
            "format": 'password',
            "minLength": 8
        }
    }
    assert result == expected


def test_nested_combination_keywords():
    schema = {
        "anyOf": [
            {
                "allOf": [
                    {
                        "type": 'object',
                        "properties": {
                            "foo": {
                                "type": 'string',
                                "nullable": True
                            }
                        }
                    },
                    {
                        "type": 'object',
                        "properties": {
                            "bar": {
                                "type": 'integer',
                                "nullable": True
                            }
                        }
                    }
                ]
            },
            {
                "type": 'object',
                "properties": {
                    "foo": {
                        "type": 'string',
                    }
                }
            },
            {
                "not": {
                    "type": 'string',
                    "example": 'foobar'
                }
            }
        ]
    }
    result = convert(schema)
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "anyOf": [
            {
                "allOf": [
                    {
                        "type": 'object',
                        "properties": {
                            "foo": {
                                "type": ['string', 'null']
                            }
                        }
                    },
                    {
                        "type": 'object',
                        "properties": {
                            "bar": {
                                "type": ['integer', 'null']
                            }
                        }
                    }
                ]
            },
            {
                "type": 'object',
                "properties": {
                    "foo": {
                        "type": 'string',
                    }
                }
            },
            {
                "not": {
                    "type": 'string',
                }
            }
        ]
    }
    assert result == expected
