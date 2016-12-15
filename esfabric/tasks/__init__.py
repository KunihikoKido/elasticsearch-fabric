# coding=utf-8
import os
import json

import fabric
from elasticsearch import Elasticsearch
from fabric.api import env
from fabric.api import task
from .utils import jsonprint
from .utils import request

import cat
import cluster
import helpers
import indices
import nodes
import snapshot

fabric.state.output.status = False

env.elasticsearch_alias = "default"
env.elasticsearch_dest_alias = "default"
env.elasticsearch_clients = {
    "default": Elasticsearch(**{
        "send_get_body_as": "POST"
    })
}


@task(alias="c")
def client_selection(alias="default", dest=None):
    env.elasticsearch_alias = alias
    env.elasticsearch_dest_alias = dest
    if dest is None:
        env.elasticsearch_dest_alias = env.elasticsearch_alias

@task
def bulk(*args, **kwargs):
    res = request("bulk", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def clear_scroll(*args, **kwargs):
    res = request("clear_scroll", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def count(*args, **kwargs):
    res = request("count", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def count_percolate(*args, **kwargs):
    res = request("count_percolate", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def create(*args, **kwargs):
    res = request("create", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def delete(*args, **kwargs):
    res = request("delete", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def delete_by_query(*args, **kwargs):
    res = request("delete_by_query", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def delete_script(*args, **kwargs):
    res = request("delete_script", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def delete_template(*args, **kwargs):
    res = request("delete_template", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def exists(*args, **kwargs):
    res = request("exists", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def explain(*args, **kwargs):
    res = request("explain", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def field_stats(*args, **kwargs):
    res = request("field_stats", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def get(*args, **kwargs):
    res = request("get", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def get_script(*args, **kwargs):
    res = request("get_script", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def get_source(*args, **kwargs):
    res = request("get_source", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def get_template(*args, **kwargs):
    res = request("get_template", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def index(*args, **kwargs):
    res = request("index", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def info(*args, **kwargs):
    res = request("info", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def mget(*args, **kwargs):
    res = request("mget", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def mpercolate(*args, **kwargs):
    res = request("mpercolate", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def msearch(*args, **kwargs):
    res = request("msearch", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def msearch_template(*args, **kwargs):
    res = request("msearch_template", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def mtermvectors(*args, **kwargs):
    res = request("mtermvectors", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def percolate(*args, **kwargs):
    res = request("percolate", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def ping(*args, **kwargs):
    res = request("ping", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def put_script(*args, **kwargs):
    res = request("put_script", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def put_template(*args, **kwargs):
    res = request("put_template", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def reindex(*args, **kwargs):
    res = request("reindex", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def reindex_rethrottle(*args, **kwargs):
    res = request("reindex_rethrottle", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def render_search_template(*args, **kwargs):
    res = request("render_search_template", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def scroll(*args, **kwargs):
    res = request("scroll", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def search(*args, **kwargs):
    res = request("search", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def search_shards(*args, **kwargs):
    res = request("search_shards", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def search_template(*args, **kwargs):
    res = request("search_template", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def suggest(*args, **kwargs):
    res = request("suggest", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def termvectors(*args, **kwargs):
    res = request("termvectors", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def update(*args, **kwargs):
    res = request("update", None, *args, **kwargs)
    jsonprint(res)
    return res

@task
def update_by_query(*args, **kwargs):
    res = request("update_by_query", None, *args, **kwargs)
    jsonprint(res)
    return res
