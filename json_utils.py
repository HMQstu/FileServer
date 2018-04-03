# coding: utf-8

import json

from flask import Response


def serialize_instance(obj):
    d = {}
    d.update(vars(obj))
    return d


def to_json(obj):
    if obj is None:
        return '{}'
    return json.dumps(obj, default=serialize_instance)


def from_json(src):
    return json.loads(src)


def to_json_res(obj):
    json_str = to_json(obj)
    return Response((json_str, '\n'), mimetype='application/json')
