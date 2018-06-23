from openapi_jsonschema_converter import openapi_to_json_schema as convert


def test_removing_readonly_prop():
    schema = {
        "type": 'object',
        "properties": {
            "prop1": {
                "type": 'string',
                "readOnly": True
            },
            "prop2": {
                "type": 'string',
            }
        }
    }
    result = convert(schema, {"removeReadOnly": True})
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'object',
        "properties": {
            "prop2": {
                "type": 'string',
            }
        }
    }
    assert result == expected


def test_removing_readonly_prop_even_if_keeping():
    schema = {
        "type": 'object',
        "properties": {
            "prop1": {
                "type": 'string',
                "readOnly": True
            },
            "prop2": {
                "type": 'string',
            }
        }
    }
    options = {
        "removeReadOnly": True,
        "keepNotSupported": ['readOnly']
    }
    result = convert(schema, options)
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'object',
        "properties": {
            "prop2": {
                "type": 'string',
            }
        }
    }
    assert result == expected


def test_removing_writeonly_prop():
    schema = {
        "type": 'object',
        "properties": {
            "prop1": {
                "type": 'string',
                "writeOnly": True
            },
            "prop2": {
                "type": 'string',
            }
        }
    }
    result = convert(schema, {"removeWriteOnly": True})
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'object',
        "properties": {
            "prop2": {
                "type": 'string',
            }
        }
    }
    assert result == expected


def test_removing_readonly_from_required():
    schema = {
        "type": 'object',
        "required": ['prop1', 'prop2'],
        "properties": {
            "prop1": {
                "type": 'string',
                "readOnly": True
            },
            "prop2": {
                "type": 'string',
            }
        }
    }
    result = convert(schema, {"removeReadOnly": True})
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'object',
        "required": ['prop2'],
        "properties": {
            "prop2": {
                "type": 'string',
            }
        }
    }
    assert result == expected


def test_deleting_required_if_empty():
    schema = {
        "type": 'object',
        "required": ['prop1'],
        "properties": {
            "prop1": {
                "type": 'string',
                "readOnly": True
            },
            "prop2": {
                "type": 'string',
            }
        }
    }
    result = convert(schema, {"removeReadOnly": True})
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'object',
        "properties": {
            "prop2": {
                "type": 'string',
            }
        }
    }
    assert result == expected


def test_deleting_properties_if_empty():
    schema = {
        "type": 'object',
        "required": ['prop1'],
        "properties": {
            "prop1": {
                "type": 'string',
                "readOnly": True
            }
        }
    }
    result = convert(schema, {"removeReadOnly": True})
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'object'
    }
    assert result == expected


def test_not_removing_readonly_props_by_default():
    schema = {
        "type": 'object',
        "required": ['prop1', 'prop2'],
        "properties": {
            "prop1": {
                "type": 'string',
                "readOnly": True
            },
            "prop2": {
                "type": 'string',
            }
        }
    }
    result = convert(schema)
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'object',
        "required": ['prop1', 'prop2'],
        "properties": {
            "prop1": {
                "type": 'string',
            },
            "prop2": {
                "type": 'string',
            }
        }
    }
    assert result == expected


def test_not_removing_writeonly_props_by_default():
    schema = {
        "type": 'object',
        "required": ['prop1', 'prop2'],
        "properties": {
            "prop1": {
                "type": 'string',
                "writeOnly": True
            },
            "prop2": {
                "type": 'string',
            }
        }
    }
    result = convert(schema)
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'object',
        "required": ['prop1', 'prop2'],
        "properties": {
            "prop1": {
                "type": 'string',
            },
            "prop2": {
                "type": 'string',
            }
        }
    }
    assert result == expected


def test_deep_schema():
    schema = {
        "type": 'object',
        "required": ['prop1', 'prop2'],
        "properties": {
            "prop1": {
                "type": 'string',
                "readOnly": True
            },
            "prop2": {
                "allOf": [
                    {
                        "type": 'object',
                        "required": ['prop3'],
                        "properties": {
                            "prop3": {
                                "type": 'object',
                                "readOnly": True
                            }
                        }
                    },
                    {
                        "type": 'object',
                        "properties": {
                            "prop4": {
                                "type": 'object',
                                "readOnly": True
                            }
                        }
                    },
                ]
            }
        }
    }
    result = convert(schema, {"removeReadOnly": True})
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'object',
        "required": ['prop2'],
        "properties": {
            "prop2": {
                "allOf": [
                    {
                        "type": 'object'
                    },
                    {
                        "type": 'object'
                    },
                ]
            }
        }
    }
    assert result == expected
