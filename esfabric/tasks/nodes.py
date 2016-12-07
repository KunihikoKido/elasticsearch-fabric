# coding=utf-8
from fabric.api import task
from .utils import jsonprint
from .utils import request


@task
def hot_threads(*args, **kwargs):
    res = request("hot_threads", "nodes", *args, **kwargs)
    jsonprint(res)
    return res

@task
def info(*args, **kwargs):
    res = request("info", "nodes", *args, **kwargs)
    jsonprint(res)
    return res

@task
def stats(*args, **kwargs):
    res = request("stats", "nodes", *args, **kwargs)
    jsonprint(res)
    return res
