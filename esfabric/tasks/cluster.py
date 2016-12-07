# coding=utf-8
from fabric.api import task
from .utils import jsonprint
from .utils import request

@task
def allocation_explain(*args, **kwargs):
    res = request("allocation_explain", "cluster", *args, **kwargs)
    jsonprint(res)
    return res

@task
def get_settings(*args, **kwargs):
    res = request("get_settings", "cluster", *args, **kwargs)
    jsonprint(res)
    return res

@task
def health(*args, **kwargs):
    res = request("health", "cluster", *args, **kwargs)
    jsonprint(res)
    return res

@task
def pending_tasks(*args, **kwargs):
    res = request("pending_tasks", "cluster", *args, **kwargs)
    jsonprint(res)
    return res

@task
def put_settings(*args, **kwargs):
    res = request("put_settings", "cluster", *args, **kwargs)
    jsonprint(res)
    return res

@task
def reroute(*args, **kwargs):
    res = request("reroute", "cluster", *args, **kwargs)
    jsonprint(res)
    return res

@task
def state(*args, **kwargs):
    res = request("state", "cluster", *args, **kwargs)
    jsonprint(res)
    return res

@task
def stats(*args, **kwargs):
    res = request("stats", "cluster", *args, **kwargs)
    jsonprint(res)
    return res
