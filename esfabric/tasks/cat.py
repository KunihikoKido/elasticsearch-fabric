# coding=utf-8
from fabric.api import task
from .utils import request

@task
def aliases(*args, **kwargs):
    res = request("aliases", "cat", *args, **kwargs)
    print(res)
    return res

@task
def allocation(*args, **kwargs):
    res = request("allocation", "cat", *args, **kwargs)
    print(res)
    return res

@task
def count(*args, **kwargs):
    res = request("count", "cat", *args, **kwargs)
    print(res)
    return res

@task
def fielddata(*args, **kwargs):
    res = request("fielddata", "cat", *args, **kwargs)
    print(res)
    return res

@task
def health(*args, **kwargs):
    res = request("health", "cat", *args, **kwargs)
    print(res)
    return res

@task
def indices(*args, **kwargs):
    res = request("indices", "cat", *args, **kwargs)
    print(res)
    return res

@task
def master(*args, **kwargs):
    res = request("master", "cat", *args, **kwargs)
    print(res)
    return res

@task
def nodeattrs(*args, **kwargs):
    res = request("nodeattrs", "cat", *args, **kwargs)
    print(res)
    return res

@task
def nodes(*args, **kwargs):
    res = request("nodes", "cat", *args, **kwargs)
    print(res)
    return res

@task
def pending_tasks(*args, **kwargs):
    res = request("pending_tasks", "cat", *args, **kwargs)
    print(res)
    return res

@task
def plugins(*args, **kwargs):
    res = request("plugins", "cat", *args, **kwargs)
    print(res)
    return res

@task
def recovery(*args, **kwargs):
    res = request("recovery", "cat", *args, **kwargs)
    print(res)
    return res

@task
def repositories(*args, **kwargs):
    res = request("repositories", "cat", *args, **kwargs)
    print(res)
    return res

@task
def segments(*args, **kwargs):
    res = request("segments", "cat", *args, **kwargs)
    print(res)
    return res

@task
def shards(*args, **kwargs):
    res = request("shards", "cat", *args, **kwargs)
    print(res)
    return res

@task
def snapshots(*args, **kwargs):
    res = request("snapshots", "cat", *args, **kwargs)
    print(res)
    return res

@task
def thread_pool(*args, **kwargs):
    res = request("thread_pool", "cat", *args, **kwargs)
    print(res)
    return res
