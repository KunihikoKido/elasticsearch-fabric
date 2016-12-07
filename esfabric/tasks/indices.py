# coding=utf-8
from fabric.api import task
from .utils import jsonprint
from .utils import request


@task
def analyze(*args, **kwargs):
    res = request("analyze", "indices", *args, **kwargs)
    jsonprint(res)
    return res

@task
def clear_cache(*args, **kwargs):
    res = request("clear_cache", "indices", *args, **kwargs)
    jsonprint(res)
    return res

@task
def close(*args, **kwargs):
    res = request("close", "indices", *args, **kwargs)
    jsonprint(res)
    return res

@task
def create(*args, **kwargs):
    res = request("create", "indices", *args, **kwargs)
    jsonprint(res)
    return res

@task
def delete(*args, **kwargs):
    res = request("delete", "indices", *args, **kwargs)
    jsonprint(res)
    return res

@task
def delete_alias(*args, **kwargs):
    res = request("delete_alias", "indices", *args, **kwargs)
    jsonprint(res)
    return res

@task
def delete_template(*args, **kwargs):
    res = request("delete_template", "indices", *args, **kwargs)
    jsonprint(res)
    return res

@task
def exists(*args, **kwargs):
    res = request("exists", "indices", *args, **kwargs)
    jsonprint(res)
    return res

@task
def exists_alias(*args, **kwargs):
    res = request("exists_alias", "indices", *args, **kwargs)
    jsonprint(res)
    return res

@task
def exists_template(*args, **kwargs):
    res = request("exists_template", "indices", *args, **kwargs)
    jsonprint(res)
    return res

@task
def exists_type(*args, **kwargs):
    res = request("exists_type", "indices", *args, **kwargs)
    jsonprint(res)
    return res

@task
def flush(*args, **kwargs):
    res = request("flush", "indices", *args, **kwargs)
    jsonprint(res)
    return res

@task
def flush_synced(*args, **kwargs):
    res = request("flush_synced", "indices", *args, **kwargs)
    jsonprint(res)
    return res

@task
def forcemerge(*args, **kwargs):
    res = request("forcemerge", "indices", *args, **kwargs)
    jsonprint(res)
    return res

@task
def get(*args, **kwargs):
    res = request("get", "indices", *args, **kwargs)
    jsonprint(res)
    return res

@task
def get_alias(*args, **kwargs):
    res = request("get_alias", "indices", *args, **kwargs)
    jsonprint(res)
    return res

@task
def get_field_mapping(*args, **kwargs):
    res = request("get_field_mapping", "indices", *args, **kwargs)
    jsonprint(res)
    return res

@task
def get_mapping(*args, **kwargs):
    res = request("get_mapping", "indices", *args, **kwargs)
    jsonprint(res)
    return res

@task
def get_settings(*args, **kwargs):
    res = request("get_settings", "indices", *args, **kwargs)
    jsonprint(res)
    return res

@task
def get_template(*args, **kwargs):
    res = request("get_template", "indices", *args, **kwargs)
    jsonprint(res)
    return res

@task
def get_upgrade(*args, **kwargs):
    res = request("get_upgrade", "indices", *args, **kwargs)
    jsonprint(res)
    return res

@task
def open(*args, **kwargs):
    res = request("open", "indices", *args, **kwargs)
    jsonprint(res)
    return res

@task
def put_alias(*args, **kwargs):
    res = request("put_alias", "indices", *args, **kwargs)
    jsonprint(res)
    return res

@task
def put_mapping(*args, **kwargs):
    res = request("put_mapping", "indices", *args, **kwargs)
    jsonprint(res)
    return res

@task
def put_settings(*args, **kwargs):
    res = request("put_settings", "indices", *args, **kwargs)
    jsonprint(res)
    return res

@task
def put_template(*args, **kwargs):
    res = request("put_template", "indices", *args, **kwargs)
    jsonprint(res)
    return res

@task
def recovery(*args, **kwargs):
    res = request("recovery", "indices", *args, **kwargs)
    jsonprint(res)
    return res

@task
def refresh(*args, **kwargs):
    res = request("refresh", "indices", *args, **kwargs)
    jsonprint(res)
    return res

@task
def rollover(*args, **kwargs):
    res = request("rollover", "indices", *args, **kwargs)
    jsonprint(res)
    return res

@task
def segments(*args, **kwargs):
    res = request("segments", "indices", *args, **kwargs)
    jsonprint(res)
    return res

@task
def shard_stores(*args, **kwargs):
    res = request("shard_stores", "indices", *args, **kwargs)
    jsonprint(res)
    return res

@task
def shrink(*args, **kwargs):
    res = request("shrink", "indices", *args, **kwargs)
    jsonprint(res)
    return res

@task
def stats(*args, **kwargs):
    res = request("stats", "indices", *args, **kwargs)
    jsonprint(res)
    return res

@task
def update_aliases(*args, **kwargs):
    res = request("update_aliases", "indices", *args, **kwargs)
    jsonprint(res)
    return res

@task
def upgrade(*args, **kwargs):
    res = request("upgrade", "indices", *args, **kwargs)
    jsonprint(res)
    return res

@task
def validate_query(*args, **kwargs):
    res = request("validate_query", "indices", *args, **kwargs)
    jsonprint(res)
    return res
