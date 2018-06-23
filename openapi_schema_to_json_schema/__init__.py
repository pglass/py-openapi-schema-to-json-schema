__all__ = [
    'to_json_schema',
    'InvalidTypeError',
    'patternPropertiesHandler',
]

from openapi_schema_to_json_schema.to_jsonschema import (
    InvalidTypeError,
    convert as to_json_schema,
    patternPropertiesHandler,
)
