"""Handlers for post-processing options."""
import json
from jsonschema import validate

from .helper import get_tempfile


def grid_metrics(json_file):
    """Validate the file for custom grid metrics.

        Args:
            json_file: A JSON file with custom grid metrics.

        Returns:
            str -- Path to a the custom grid metrics file.
    """
    _of_schema = {
        'type': 'array',
        'items': {
            'properties': {
                'minimum': {'type': 'number'},
                'maximum': {'type': 'number'},
                'exclusiveMinimum': {'type': 'number'},
                'exclusiveMaximum': {'type': 'number'}
            },
            'additionalProperties': False
        }
    }
    schema = {
        'type': 'array',
        'items': {
            'type': 'object',
            'properties': {
                'minimum': {'type': 'number'},
                'maximum': {'type': 'number'},
                'exclusiveMinimum': {'type': 'number'},
                'exclusiveMaximum': {'type': 'number'},
                'allOf': _of_schema,
                'anyOf': _of_schema
            },
            'additionalProperties': False
        }
    }

    with open(json_file) as file:
        grid_metrics = json.load(file)
    validate(grid_metrics, schema)

    file_path = get_tempfile('json', 'grid_metrics')
    with open(file_path, 'w') as f:
        json.dump(grid_metrics, f)

    return file_path
