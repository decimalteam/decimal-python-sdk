def beautify_json(value):
    if type(value) == list:
        return [beautify_json(elem) for elem in value]
    elif type(value) == dict:
        keys = list(value.keys())
        keys.sort()
        return {key: beautify_json(value[key]) for key in keys}
    else:
        return value
