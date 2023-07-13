"""Handlers for post-processing options."""
import json

from .helper import get_tempfile


def grid_metrics(json_file):
    with open(json_file) as file:
        grid_metrics = json.load(file)
    assert isinstance(grid_metrics, list), \
        'Information in the grid metrics file must be a list.'
    for grid_metric in grid_metrics:
        assert isinstance(grid_metric, dict), \
        'Each item in grid metrics must be a dictionary.'
        if 'allOf' in grid_metric:
            assert isinstance(grid_metric['allOf'], list)
            for gr_m in grid_metric['allOf']:
                assert isinstance(gr_m, dict)
        elif 'anyOf' in grid_metric:
            assert isinstance(grid_metric['anyOf'], list)
            for gr_m in grid_metric['anyOf']:
                assert isinstance(gr_m, dict)

    file_path = get_tempfile('json', 'grid_metrics')
    with open(file_path, 'w') as f:
        json.dump(grid_metrics, f)

    return file_path
