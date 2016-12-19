# coding=utf-8
from fabric.api import task
from .utils import jsonprint
from .utils import request

@task
def allocation_explain(body=None, **kwargs):
    res = request("allocation_explain", "cluster", body=body, **kwargs)
    jsonprint(res)
    return res

@task
def get_settings(**kwargs):
    res = request("get_settings", "cluster", **kwargs)
    jsonprint(res)
    return res

@task
def health(index=None, **kwargs):
    res = request("health", "cluster", index=index, **kwargs)
    jsonprint(res)
    return res

@task
def pending_tasks(**kwargs):
    res = request("pending_tasks", "cluster", **kwargs)
    jsonprint(res)
    return res

@task
def put_settings(body=None, **kwargs):
    res = request("put_settings", "cluster", body=body, **kwargs)
    jsonprint(res)
    return res

@task
def reroute(body=None, **kwargs):
    res = request("reroute", "cluster", body=body, **kwargs)
    jsonprint(res)
    return res

@task
def state(metric=None, index=None, **kwargs):
    res = request("state", "cluster", metric=metric, index=None, **kwargs)
    jsonprint(res)
    return res

@task
def stats(node_id=None, **kwargs):
    res = request("stats", "cluster", node_id=node_id, **kwargs)
    jsonprint(res)
    return res
