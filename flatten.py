#!/usr/bin/env python3
"""Build a dict flattening function in flatten.py"""

import json
import sys

def flatten_dict(d, sep='.'):
    result = {}
    for key, value in d.items():
        if isinstance(value, dict):
            for k, v in flatten_dict(value, sep).items():
                result[f"{key}{sep}{k}"] = v
        else:
            result[key] = value
    return result


if __name__ == "__main__":
    data = json.loads(sys.stdin.read() or '{}')
    result = flatten_dict(data)
    print(json.dumps(result, indent=2))
