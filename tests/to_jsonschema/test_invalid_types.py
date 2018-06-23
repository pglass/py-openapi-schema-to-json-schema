from openapi_schema_to_json_schema import to_json_schema as convert
from openapi_schema_to_json_schema import InvalidTypeError
from tests.to_jsonschema.utils import get_schema_file
import pytest


def test_invalid_types():
    schema = {"type": "dateTime"}
    with pytest.raises(InvalidTypeError) as e:
        convert(schema)
    assert 'Type "dateTime" is not a valid type' in str(e)

    schema = {"type": "foo"}
    with pytest.raises(InvalidTypeError) as e:
        convert(schema)
    assert 'Type "foo" is not a valid type' in str(e)

    schema = get_schema_file('schema-2-invalid-type.json')
    with pytest.raises(InvalidTypeError) as e:
        convert(schema)
    assert 'Type "invalidtype" is not a valid type'


def test_valid_types():
    types = ['integer', 'number', 'string', 'boolean', 'object', 'array']

    for ttype in types:
        schema = {'type': ttype}
        result = convert(schema)
        expected = {
            "$schema": 'http://json-schema.org/draft-04/schema#',
            "type": ttype,
        }
        assert result == expected
