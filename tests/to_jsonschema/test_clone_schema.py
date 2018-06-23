from openapi_schema_to_json_schema import to_json_schema as convert


def test_clone_schema_by_default():
    """Test the the default behavior is to clone the schema"""
    schema = {
        'type': 'string',
        'nullable': True,
    }
    result = convert(schema)
    expected = {
        '$schema': 'http://json-schema.org/draft-04/schema#',
        'type': ['string', 'null'],
    }
    assert result == expected
    assert schema is not result


def test_clone_schema_true():
    """Test that the schema is clone when cloneSchema is True"""
    schema = {
        'type': 'string',
        'nullable': True,
    }
    result = convert(schema, {"cloneSchema": True})
    expected = {
        '$schema': 'http://json-schema.org/draft-04/schema#',
        'type': ['string', 'null'],
    }
    assert result == expected
    assert schema is not result


def test_clone_schema_false():
    """Test that the schema is modified in place when cloneSchema is False"""
    schema = {
        'type': 'string',
        'nullable': True,
    }
    result = convert(schema, {"cloneSchema": False})
    expected = {
        '$schema': 'http://json-schema.org/draft-04/schema#',
        'type': ['string', 'null'],
    }
    assert schema == expected
    assert result == expected
    assert schema is result
