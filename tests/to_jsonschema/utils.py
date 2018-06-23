import json
import os


def get_schema_file(filename):
    schema = os.path.realpath(
        os.path.join(os.path.dirname(__file__), 'schemas', filename)
    )
    with open(schema, 'r') as f:
        return json.load(f)
