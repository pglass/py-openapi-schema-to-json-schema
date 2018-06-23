[![Build Status](https://travis-ci.org/pglass/py-openapi-schema-to-json-schema.svg?branch=master)](https://travis-ci.org/pglass/py-openapi-schema-to-json-schema)

Overview
--------

**This is a straight Python port of the MIT-licensed
[mikunn/openapi-schema-to-json-schema](https://github.com/mikunn/openapi-schema-to-json-schema)
([v2.1.0](https://github.com/mikunn/openapi-schema-to-json-schema/tree/v2.1.0))**.
This port is similarly MIT-licensed.

It converts from converts from [OpenAPI 3.0](
https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md) to
[JSON Schema Draft 4](http://json-schema.org/specification-links.html#draft-4).

## Why?

OpenAPI 3 Schemas and JSON Schemas are mostly similar. However, JSON Schema
validators are unaware of the differences between the two formats. This means
that validating request/response JSON using a standard JSON Schema validator
with OpenAPI 3 Schemas will result in incorrect validations in certain common
cases.

One way to solve this problem is to translate the OpenAPI 3 schema to JSON
Schema, which is the purpose of this library.

See [here](https://github.com/mikunn/openapi-schema-to-json-schema/tree/v2.1.0#why)
for more rationale, as well as [Phil Sturgeon's blog post](
https://philsturgeon.uk/api/2018/03/30/openapi-and-json-schema-divergence/)
about the problem.

## Features

* converts OpenAPI 3.0 Schema Object to JSON Schema Draft 4
* deletes `nullable` and adds `"null"` to `type` array if `nullable` is `true`
* supports deep structures with nested `allOf`s etc.
* removes [OpenAPI specific
  properties](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md#fixed-fields-20)
such as `discriminator`, `deprecated` etc. unless specified otherwise
* optionally supports `patternProperties` with `x-patternProperties` in the
  Schema Object

**NOTE**: `$ref`s are not dereferenced. You will need another library to
read the spec and follow `$ref` fields.


## Installation

```bash
$ pip install py-openapi-schema-to-json-schema
```


## Usage

```python
import json
from openapi_schema_to_json_schema import to_json_schema

openapi_schema = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "nullable": True,
        }
    },
    "x-patternProperties": {
        "^[a-z]+$": {
            "type": "number",
        }
    }
}

options = {"supportPatternProperties": True}
converted = to_json_schema(openapi_schema, options)

print(json.dumps(converted, indent=2))
```

This outputs the following JSON schema. This shows the conversion of
`nullable: True` to `type: ["string", "null"]`, and the enablement of
unsupported JSON Schema features using OpenAPI extension fields
(`x-patternProperties` -> `patternProperties`).

```json
{
  "patternProperties": {
    "^[a-z]+$": {
      "type": "number"
    }
  },
  "properties": {
    "name": {
      "type": [
        "string",
        "null"
      ]
    }
  },
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object"
}
```

### Options

The `to_json_schema` function accepts an `options` dictionary as the second
argument.

```python
# Defaults
options = {
    'cloneSchema': True,
    'dateToDateTime': False,
    'supportPatternProperties': False,
    'keepNotSupported': [],
    'patternPropertiesHandler':
        openapi_schema_to_json_schema.patternPropertiesHandler,
    'removeReadOnly': False,
    'removeWriteOnly': True,
}
```

#### `cloneSchema` (bool)

If set to `False`, converts the provided schema in place. If `True`, clones the
schema using `copy.deepcopy`. Defaults to `True`.

#### `dateToDateTime` (bool)

This is `False` by default and leaves `date` format as is. If set to `True`,
sets `format: 'date'` to `format: 'date-time'`.

For example

```python
import json
from openapi_schema_to_json_schema import to_json_schema

schema = {
  'type': 'string',
  'format': 'date',
}

converted = to_json_schema(schema, {'dateToDateTime': True})

print(json.dumps(converted, indent=2))
```

prints

```json
{
  "format": "date-time",
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "string"
}
```

#### `keepNotSupported` (list)

By default, the following fields are removed from the result schema:
`nullable`, `discriminator`, `readOnly`, `writeOnly`, `xml`, `externalDocs`,
`example` and `deprecated` as they are not supported by JSON Schema Draft 4.
Provide a list of the ones you want to keep (as strings) and they won't be
removed.

#### `removeReadOnly` (bool)

If set to `True`, will remove properties set as `readOnly`. If the property is
set as `required`, it will be removed from the `required` list as well. The
property will be removed even if `readOnly` is set to be kept with
`keepNotSupported`.

#### `removeWriteOnly` (bool)

Similar to `removeReadOnly`, but for `writeOnly` properties.

#### `supportPatternProperties` (bool)

If set to `True` and `x-patternProperties` property is present, change
`x-patternProperties` to `patternProperties` and call
`patternPropertiesHandler`. If `patternPropertiesHandler` is not defined, call
the default handler. See `patternPropertiesHandler` for more information.

#### `patternPropertiesHandler` (function)

Provide a function to handle pattern properties and set
`supportPatternProperties` to take effect. The function takes the schema where
`x-patternProperties` is defined on the root level. At this point
`x-patternProperties` is changed to `patternProperties`. It must return the
modified schema.

If the handler is not provided, the default handler is used. If
`additionalProperties` is set and is an object, the default handler sets it to
false if the `additionalProperties` object has deep equality with a pattern
object inside `patternProperties`. This is because we might want to define
`additionalProperties` in OpenAPI spec file, but want to validate against a
pattern. The pattern would turn out to be useless if `additionalProperties` of
the same structure were allowed. Create you own handler to override this
functionality.

See `tests/to_jsonschema/test_pattern_properties.py` for examples of this.


Credits
-------

- [mikunn](https://github.com/mikunn) for the [original
openapi-schema-to-json-schema](https://github.com/mikunn/openapi-schema-to-json-schema)
- [Phil Sturgeon](https://github.com/philsturgeon) for his great blog post
[blog post](https://philsturgeon.uk/api/2018/03/30/openapi-and-json-schema-divergence/)
about the issue (and his [reverse implementation](https://github.com/wework/json-schema-to-openapi-schema))
