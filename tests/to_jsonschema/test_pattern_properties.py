from openapi_schema_to_json_schema import to_json_schema as convert


def test_handling_additional_properties_of_the_same_type_string():
    schema = {
        "type": 'object',
        "additionalProperties": {
            "type": 'string'
        },
        'x-patternProperties': {
            '^[a-z]*$': {
                "type": 'string'
            }
        }
    }
    result = convert(schema, {"supportPatternProperties": True})
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'object',
        "additionalProperties": False,
        "patternProperties": {
            '^[a-z]*$': {
                "type": 'string'
            }
        }
    }
    assert result == expected


def test_handling_additional_properties_of_the_same_type_number():
    schema = {
        "type": 'object',
        "additionalProperties": {
            "type": 'number'
        },
        'x-patternProperties': {
            '^[a-z]*$': {
                "type": 'number'
            }
        }
    }
    result = convert(schema, {"supportPatternProperties": True})
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'object',
        "additionalProperties": False,
        "patternProperties": {
            '^[a-z]*$': {
                "type": 'number'
            }
        }
    }
    assert result == expected


def test_handling_additional_properties_with_one_of_patternProperty_types():
    schema = {
        "type": 'object',
        "additionalProperties": {
            "type": 'number'
        },
        'x-patternProperties': {
            '^[a-z]*$': {
                "type": 'string'
            },
            '^[A-Z]*$': {
                "type": 'number'
            }
        }
    }
    result = convert(schema, {"supportPatternProperties": True})
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'object',
        "additionalProperties": False,
        "patternProperties": {
            '^[a-z]*$': {
                "type": 'string'
            },
            '^[A-Z]*$': {
                "type": 'number'
            }
        }
    }
    assert result == expected


def test_handling_additionalProperties_with_matching_objects():
    schema = {
        "type": 'object',
        "additionalProperties": {
            "type": 'object',
            "properties": {
                "test": {
                    "type": 'string'
                }
            }
        },
        'x-patternProperties': {
            '^[a-z]*$': {
                "type": 'string'
            },
            '^[A-Z]*$': {
                "type": 'object',
                "properties": {
                    "test": {
                        "type": 'string'
                    }
                }
            }
        }
    }
    result = convert(schema, {"supportPatternProperties": True})
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'object',
        "additionalProperties": False,
        "patternProperties": {
            '^[a-z]*$': {
                "type": 'string'
            },
            '^[A-Z]*$': {
                "type": 'object',
                "properties": {
                    "test": {
                        "type": 'string'
                    }
                }
            }
        }
    }
    assert result == expected


def test_handling_additionalProperties_with_non_matching_objects():

    schema = {
        "type": 'object',
        "additionalProperties": {
            "type": 'object',
            "properties": {
                "test": {
                    "type": 'string'
                }
            }
        },
        'x-patternProperties': {
            '^[a-z]*$': {
                "type": 'string'
            },
            '^[A-Z]*$': {
                "type": 'object',
                "properties": {
                    "test": {
                        "type": 'integer'
                    }
                }
            }
        }
    }
    result = convert(schema, {"supportPatternProperties": True})
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'object',
        "additionalProperties": {
            "type": 'object',
            "properties": {
                "test": {
                    "type": 'string'
                }
            }
        },
        "patternProperties": {
            '^[a-z]*$': {
                "type": 'string'
            },
            '^[A-Z]*$': {
                "type": 'object',
                "properties": {
                    "test": {
                        "type": 'integer'
                    }
                }
            }
        }
    }
    assert result == expected


def test_handling_additionalProperties_with_matching_array():
    schema = {
        "type": 'object',
        "additionalProperties": {
            "type": 'array',
            "items": {
                "type": 'string'
            }
        },
        'x-patternProperties': {
            '^[a-z]*$': {
                "type": 'string'
            },
            '^[A-Z]*$': {
                "type": 'array',
                "items": {
                    "type": 'string'
                }
            }
        }
    }
    result = convert(schema, {"supportPatternProperties": True})
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'object',
        "additionalProperties": False,
        "patternProperties": {
            '^[a-z]*$': {
                "type": 'string'
            },
            '^[A-Z]*$': {
                "type": 'array',
                "items": {
                    "type": 'string'
                }
            }
        }
    }
    assert result == expected


def test_handling_additionalProperties_with_composition_types():
    schema = {
        "type": 'object',
        "additionalProperties": {
            "oneOf": [
                {
                    "type": 'string'
                },
                {
                    "type": 'integer'
                }
            ]
        },
        'x-patternProperties': {
            '^[a-z]*$': {
                "oneOf": [
                    {
                        "type": 'string'
                    },
                    {
                        "type": 'integer'
                    }
                ]
            }
        }
    }
    result = convert(schema, {"supportPatternProperties": True})
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'object',
        "additionalProperties": False,
        "patternProperties": {
            '^[a-z]*$': {
                "oneOf": [
                    {
                        "type": 'string'
                    },
                    {
                        "type": 'integer'
                    }
                ]
            }
        }
    }
    assert result == expected


def test_not_supporting_patternProperties():
    schema = {
        "type": 'object',
        "additionalProperties": {
            "type": 'string'
        },
        'x-patternProperties': {
            '^[a-z]*$': {
                "type": 'string'
            }
        }
    }
    result = convert(schema, {"supportPatternProperties": False})
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'object',
        "additionalProperties": {
            "type": 'string'
        },
        'x-patternProperties': {
            '^[a-z]*$': {
                "type": 'string'
            }
        }
    }
    assert result == expected


def test_not_supporting_patternProperties_by_default():
    schema = {
        "type": 'object',
        "additionalProperties": {
            "type": 'string'
        },
        'x-patternProperties': {
            '^[a-z]*$': {
                "type": 'string'
            }
        }
    }
    result = convert(schema)
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'object',
        "additionalProperties": {
            "type": 'string'
        },
        'x-patternProperties': {
            '^[a-z]*$': {
                "type": 'string'
            }
        }
    }
    assert result == expected


def test_setting_custom_pattern_properties_handler():
    schema = {
        "type": 'object',
        "additionalProperties": {
            "type": 'string'
        },
        'x-patternProperties': {
            '^[a-z]*$': {
                "type": 'string'
            }
        }
    }

    def handler(sch):
        sch['patternProperties'] = False
        return sch

    options = {
        "supportPatternProperties": True,
        "patternPropertiesHandler": handler,
    }

    result = convert(schema, options)
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'object',
        "additionalProperties": {
            "type": 'string'
        },
        "patternProperties": False
    }
    assert result == expected


def test_additionalProperties_not_modified_if_set_to_true():
    schema = {
        "type": 'object',
        "additionalProperties": True,
        'x-patternProperties': {
            '^[a-z]*$': {
                "type": 'string'
            }
        }
    }
    result = convert(schema, {"supportPatternProperties": True})
    expected = {
        "$schema": 'http://json-schema.org/draft-04/schema#',
        "type": 'object',
        "additionalProperties": True,
        "patternProperties": {
            '^[a-z]*$': {
                "type": 'string'
            }
        }
    }
    assert result == expected
