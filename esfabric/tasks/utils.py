# coding=utf-8
import sys
import json
from pygments import highlight
from pygments import lexers
from pygments import formatters
from fabric.api import env
from fabric.api import task
from fabric.utils import abort


def jsonprint(obj):
    formatted_json = json.dumps(obj, ensure_ascii=False, indent=2)
    colorful_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
    print(colorful_json)


def stdin_body(func):
    def wrapper(*args, **kwargs):
        if sys.stdin.isatty() is False:
            kwargs["body"] = sys.stdin.read()
        return func(*args, **kwargs)
    return wrapper


def cleaned_kwargs(func):
    def wrapper(*args, **kwargs):
        LIST_PARAMS = ("_source", "filter_path", )
        for key, val in kwargs.items():
            if key in LIST_PARAMS:
                kwargs[key] = val.split(";")
        return func(*args, **kwargs)
    return wrapper


def get_client(alias):
    try:
        client = env.elasticsearch_clients[alias]
    except Exception as e:
        abort(e)
    return client

@stdin_body
@cleaned_kwargs
def request(func_name, module_name, *args, **kwargs):
    es = get_client(env.elasticsearch_alias)
    if module_name is "cat":
        func = getattr(es.cat, func_name)
    elif module_name is "cluster":
        func = getattr(es.cluster, func_name)
    elif module_name is "indices":
        func = getattr(es.indices, func_name)
    elif module_name is "nodes":
        func = getattr(es.nodes, func_name)
    else:
        func = getattr(es, func_name)
    try:
        res = func(*args, ignore=[400, 401, 404, 500], **kwargs)
    except Exception as e:
        abort(e)
    return res
