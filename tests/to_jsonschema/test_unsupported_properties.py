from openapi_jsonschema_converter import openapi_to_json_schema as convert


def test_remove_discriminator_by_default():
    schema = {
        "oneOf": [
            {
                "type": 'object',
                "required": ['foo'],
                "properties": {
                    "foo": {
                        "type": 'string'
                    }
                }
            },
            {
                "type": 'object',
                "required": ['foo'],
                "properties": {
                    "foo": {
                        "type": 'string'
                    }
                }
            }
        ],
        "discriminator": {
            "propertyName": 'foo'
        }
    }
    result = convert(schema)
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "oneOf": [
            {
                "type": 'object',
                "required": ['foo'],
                "properties": {
                    "foo": {
                        "type": 'string'
                    }
                }
            },
            {
                "type": 'object',
                "required": ['foo'],
                "properties": {
                    "foo": {
                        "type": 'string'
                    }
                }
            }
        ],
    }
    assert result == expected


def test_remove_readonly_by_default():
    schema = {
        "type": 'object',
        "properties": {
            "readOnly": {
                "type": 'string',
                "readOnly": True
            }
        }
    }
    result = convert(schema)
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'object',
        "properties": {
            "readOnly": {
                "type": 'string'
            }
        }
    }
    assert result == expected


def test_remove_writeonly_by_default():
    schema = {
        "type": 'object',
        "properties": {
            "test": {
                "type": 'string',
                "format": 'password',
                "writeOnly": True
            }
        }
    }
    result = convert(schema)
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'object',
        "properties": {
            "test": {
                "type": 'string',
                "format": 'password'
            }
        }
    }
    assert result == expected


def test_remove_xml_by_default():
    schema = {
        "type": 'object',
        "properties": {
            "foo": {
                "type": 'string',
                "xml": {
                    "attribute": True
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
                "type": 'string'
            }
        }
    }
    assert result == expected


def test_remove_externaldocs_by_default():
    schema = {
        "type": 'object',
        "properties": {
            "foo": {
                "type": 'string'
            }
        },
        "externalDocs": {
            "url": 'http://foo.bar'
        }
    }
    result = convert(schema)
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'object',
        "properties": {
            "foo": {
                "type": 'string'
            }
        }
    }
    assert result == expected


def test_remove_example_by_default():
    schema = {
        "type": 'string',
        "example": 'foo'
    }
    result = convert(schema)
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'string'
    }
    assert result == expected


def test_remove_deprecated_by_default():
    schema = {
        "type": 'string',
        "deprecated": True
    }
    result = convert(schema)
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'string'
    }
    assert result == expected


def test_retaining_fields():
    schema = {
        "type": 'object',
        "properties": {
            "readOnly": {
                "type": 'string',
                "readOnly": True,
                "example": 'foo'
            },
            "anotherProp": {
                "type": 'object',
                "properties": {
                    "writeOnly": {
                        "type": 'string',
                        "writeOnly": True
                    }
                }
            }
        },
        "discriminator": 'bar'
    }
    options = {"keepNotSupported": ['readOnly', 'discriminator']}
    result = convert(schema, options)
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'object',
        "properties": {
            "readOnly": {
                "type": 'string',
                "readOnly": True,
            },
            "anotherProp": {
                "type": 'object',
                "properties": {
                    "writeOnly": {
                        "type": 'string',
                    }
                }
            }
        },
        "discriminator": 'bar'
    }
    assert result == expected
