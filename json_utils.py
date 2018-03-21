# coding: utf-8

import json


def to_json(obj):
    if obj is None:
        return '{}'
    return json.dumps(obj.__dict__)


def from_json(src):
    return json.loads(src)
