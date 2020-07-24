import json
import os

import yaml


def get_schema_file(filename):
    schema = os.path.realpath(
        os.path.join(os.path.dirname(__file__), 'schemas', filename)
    )
    with open(schema, 'r') as f:
        if schema.endswith('.yaml'):
            return yaml.load(f, Loader=yaml.SafeLoader)
        return json.load(f)
