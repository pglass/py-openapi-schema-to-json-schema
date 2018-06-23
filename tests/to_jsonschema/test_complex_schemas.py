from openapi_jsonschema_converter import openapi_to_json_schema as convert
from tests.to_jsonschema.utils import get_schema_file


def test_complex_schema():
    schema = get_schema_file('schema-1.json')
    result = convert(schema)
    expected = get_schema_file('schema-1-expected.json')
    assert schema is not result
    assert result == expected


def test_complex_schema_in_place():
    schema = get_schema_file('schema-1.json')
    result = convert(schema, {'cloneSchema': False})
    expected = get_schema_file('schema-1-expected.json')

    assert schema is result
    assert schema == expected
    assert result == expected
