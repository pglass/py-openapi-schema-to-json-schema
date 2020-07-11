from openapi_schema_to_json_schema.to_jsonschema import convertDoc
from tests.to_jsonschema.utils import get_schema_file


def test_doc():
    schema = get_schema_file('doc.yaml')
    result = convertDoc(schema, {
        'keepNotSupported': ['readOnly', 'writeOnly'],
    })
    expected = get_schema_file('doc-expected.yaml')

    assert schema is not result
    assert result == expected


def test_doc_in_place():
    schema = get_schema_file('doc.yaml')
    result = convertDoc(schema, {
        'cloneSchema': False,
        'keepNotSupported': ['readOnly', 'writeOnly'],
    })
    expected = get_schema_file('doc-expected.yaml')

    assert result == expected
    assert schema is result
