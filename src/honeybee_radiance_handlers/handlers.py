import os
import json
import tempfile
import uuid
from honeybee.model import Model


def model_to_json_path(model_obj):
    """Save Honeybee model to a JSON file and return JSON path."""
    if isinstance(model_obj, str):
        hb_file = model_obj
    elif isinstance(model_obj, Model):
        file_name = str(uuid.uuid4())[:6]
        temp_dir = tempfile.gettempdir()
        hb_file = os.path.join(temp_dir, file_name + '.hbjson')

        try:
            obj_dict = model_obj.to_dict(abridged=True)
        except TypeError:  # no abridged option
            obj_dict = model_obj.to_dict()

        # write the dictionary into a file
        with open(hb_file, 'w') as fp:
            json.dump(obj_dict, fp)
    else:
        raise ValueError(
            'model input should be a string or a Honeybee Model not a ' + type(model_obj)
        )
    return hb_file


def read_DF_from_path(resultFile):
    """Read daylight factor values from a radiance .res result file."""
    result = []
    resultFile = open(resultFile, "r")
    for line in resultFile:
        res = float(line)
        if res > 100:
            res = 100
        result.append(res)
    return result

