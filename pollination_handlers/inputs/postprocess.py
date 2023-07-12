"""Handlers for post-processing options."""
import json


def grid_metrics(json_file):
    with open(json_file) as file:
        grid_metrics = json.load(file)
    assert isinstance(grid_metrics, list), \
        'Information in the grid metrics file must be a list.'
    for grid_metric in grid_metrics:
        assert isinstance(grid_metric, dict), \
        'Each item in grid metrics must be a dictionary.'
    for grid_metric in grid_metrics:
        if 'allOf' in grid_metric:
            assert isinstance(grid_metric['allOff'], list)
            for gr_m in grid_metric['allOff']:
                assert isinstance(gr_m, dict)
        elif 'anyOf' in grid_metric:
            assert isinstance(grid_metric['anyOf'], list)
            for gr_m in grid_metric['anyOf']:
                assert isinstance(gr_m, dict)

    return json_file
