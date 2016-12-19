# coding=utf-8
from fabric.api import task
from .utils import request

@task
def aliases(name=None, **kwargs):
    res = request("aliases", "cat", name=name, **kwargs)
    print(res)
    return res

@task
def allocation(node_id=None, **kwargs):
    res = request("allocation", "cat", node_id=node_id, **kwargs)
    print(res)
    return res

@task
def count(index=None, **kwargs):
    res = request("count", "cat", index=index, **kwargs)
    print(res)
    return res

@task
def fielddata(fields=None, **kwargs):
    res = request("fielddata", "cat", fields=fields, **kwargs)
    print(res)
    return res

@task
def health(**kwargs):
    res = request("health", "cat", **kwargs)
    print(res)
    return res

@task
def indices(index=None, **kwargs):
    res = request("indices", "cat", index=index, **kwargs)
    print(res)
    return res

@task
def master(**kwargs):
    res = request("master", "cat", **kwargs)
    print(res)
    return res

@task
def nodeattrs(**kwargs):
    res = request("nodeattrs", "cat", **kwargs)
    print(res)
    return res

@task
def nodes(**kwargs):
    res = request("nodes", "cat", **kwargs)
    print(res)
    return res

@task
def pending_tasks(**kwargs):
    res = request("pending_tasks", "cat", **kwargs)
    print(res)
    return res

@task
def plugins(**kwargs):
    res = request("plugins", "cat", **kwargs)
    print(res)
    return res

@task
def recovery(index=None, **kwargs):
    res = request("recovery", "cat", index=index, **kwargs)
    print(res)
    return res

@task
def repositories(**kwargs):
    res = request("repositories", "cat", **kwargs)
    print(res)
    return res

@task
def segments(index=None, **kwargs):
    res = request("segments", "cat", index=index, **kwargs)
    print(res)
    return res

@task
def shards(index=None, **kwargs):
    res = request("shards", "cat", index=index, **kwargs)
    print(res)
    return res

@task
def snapshots(repository=None, **kwargs):
    res = request("snapshots", "cat", repository=repository, **kwargs)
    print(res)
    return res

@task
def thread_pool(thread_pools=None, **kwargs):
    res = request("thread_pool", "cat", thread_pools=thread_pools, **kwargs)
    print(res)
    return res
