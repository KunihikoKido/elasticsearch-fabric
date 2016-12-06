# coding=utf-8
import sys
import json
import yaml
from elasticsearch import Elasticsearch
from pygments import highlight, lexers, formatters
from fabric.api import env, task
from fabric.colors import green
from fabric.utils import puts
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


def get_esclient(*args, **kwargs):
    try:
        client = env.elasticsearch_clients[env.elasticsearch]
    except Exception as e:
        abort(e)
    return client

@stdin_body
@cleaned_kwargs
def request(func_name, module_name, *args, **kwargs):
    es = get_esclient()
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
    res = func(*args, ignore=[400, 401, 404, 500], **kwargs)
    return res


@task(alias="s")
def server_selection(name="default", dest=None):
    env.elasticsearch = name
    env.elasticsearch_dest = dest
    if dest is None:
        env.elasticsearch_dest = env.elasticsearch
