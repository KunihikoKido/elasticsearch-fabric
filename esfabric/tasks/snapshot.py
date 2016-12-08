# coding=utf-8
# coding=utf-8
from fabric.api import task
from .utils import jsonprint
from .utils import request


@task
def create(*args, **kwargs):
    res = request("create", "snapshot", *args, **kwargs)
    jsonprint(res)
    return res

@task
def create_repository(*args, **kwargs):
    res = request("create_repository", "snapshot", *args, **kwargs)
    jsonprint(res)
    return res

@task
def delete(*args, **kwargs):
    res = request("delete", "snapshot", *args, **kwargs)
    jsonprint(res)
    return res

@task
def delete_repository(*args, **kwargs):
    res = request("delete_repository", "snapshot", *args, **kwargs)
    jsonprint(res)
    return res

@task
def get(*args, **kwargs):
    res = request("get", "snapshot", *args, **kwargs)
    jsonprint(res)
    return res

@task
def get_repository(*args, **kwargs):
    res = request("get_repository", "snapshot", *args, **kwargs)
    jsonprint(res)
    return res

@task
def restore(*args, **kwargs):
    res = request("restore", "snapshot", *args, **kwargs)
    jsonprint(res)
    return res

@task
def status(*args, **kwargs):
    res = request("status", "snapshot", *args, **kwargs)
    jsonprint(res)
    return res

@task
def verify_repository(*args, **kwargs):
    res = request("verify_repository", "snapshot", *args, **kwargs)
    jsonprint(res)
    return res
