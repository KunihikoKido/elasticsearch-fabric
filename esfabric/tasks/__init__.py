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
def info(**kwargs):
    res = request("info", None, **kwargs)
    jsonprint(res)
    return res

@task
def create(index, doc_type, id, body, **kwargs):
    res = request("create", None, index, doc_type, id, body, **kwargs)
    jsonprint(res)
    return res

@task
def index(index, doc_type, body, id=None, **kwargs):
    res = request("index", None, index, doc_type, body, id=None, **kwargs)
    jsonprint(res)
    return res

@task
def exists(index, doc_type, id, **kwargs):
    res = request("exists", None, index, doc_type, id, **kwargs)
    jsonprint(res)
    return res

@task
def bulk(body, index=None, doc_type=None, **kwargs):
    res = request("bulk", None, body, index=index, doc_type=doc_type, **kwargs)
    jsonprint(res)
    return res

@task
def clear_scroll(scroll_id=None, body=None, **kwargs):
    res = request("clear_scroll", None, scroll_id=scroll_id, body=body, **kwargs)
    jsonprint(res)
    return res

@task
def count(index=None, doc_type=None, body=None, **kwargs):
    res = request("count", None, index=index, doc_type=doc_type, body=body, **kwargs)
    jsonprint(res)
    return res

@task
def count_percolate(index, doc_type, id=None, body=None, **kwargs):
    res = request("count_percolate", None, index, doc_type, id=id, body=body, **kwargs)
    jsonprint(res)
    return res

@task
def delete(index, doc_type, id, **kwargs):
    res = request("delete", None, index, doc_type, id, **kwargs)
    jsonprint(res)
    return res

@task
def delete_by_query(index, body, doc_type=None, **kwargs):
    res = request("delete_by_query", None, index, body, doc_type=doc_type, **kwargs)
    jsonprint(res)
    return res

@task
def delete_script(lang, id, **kwargs):
    res = request("delete_script", None, lang, id, **kwargs)
    jsonprint(res)
    return res

@task
def delete_template(id, **kwargs):
    res = request("delete_template", None, id, **kwargs)
    jsonprint(res)
    return res

@task
def explain(index, doc_type, id, body=None, **kwargs):
    res = request("explain", None, index, doc_type, id, body=body, **kwargs)
    jsonprint(res)
    return res

@task
def field_stats(index=None, body=None, **kwargs):
    res = request("field_stats", None, index=index, body=body, **kwargs)
    jsonprint(res)
    return res

@task
def get(index, id, doc_type='_all', **kwargs):
    res = request("get", None, index, id, doc_type=doc_type, **kwargs)
    jsonprint(res)
    return res

@task
def get_script(lang, id, **kwargs):
    res = request("get_script", None, lang, id, **kwargs)
    jsonprint(res)
    return res

@task
def get_source(index, doc_type, id, **kwargs):
    res = request("get_source", None, index, doc_type, id, **kwargs)
    jsonprint(res)
    return res

@task
def get_template(id, **kwargs):
    res = request("get_template", None, id, **kwargs)
    jsonprint(res)
    return res

@task
def mget(body, index=None, doc_type=None, **kwargs):
    res = request("mget", None, body, index=index, doc_type=doc_type, **kwargs)
    jsonprint(res)
    return res

@task
def mpercolate(body, index=None, doc_type=None, **kwargs):
    res = request("mpercolate", None, body, index=index, doc_type=doc_type, **kwargs)
    jsonprint(res)
    return res

@task
def msearch(body, index=None, doc_type=None, **kwargs):
    res = request("msearch", None, body, index=index, doc_type=doc_type, **kwargs)
    jsonprint(res)
    return res

@task
def msearch_template(body, index=None, doc_type=None, **kwargs):
    res = request("msearch_template", None, body, index=index, doc_type=doc_type, **kwargs)
    jsonprint(res)
    return res

@task
def mtermvectors(index=None, doc_type=None, body=None, **kwargs):
    res = request("mtermvectors", None, index=index, doc_type=doc_type, body=body, **kwargs)
    jsonprint(res)
    return res

@task
def percolate(index, doc_type, id=None, body=None, **kwargs):
    res = request("percolate", None, index, doc_type, id=id, body=body, **kwargs)
    jsonprint(res)
    return res

@task
def ping(**kwargs):
    res = request("ping", None, **kwargs)
    jsonprint(res)
    return res

@task
def put_script(lang, id, body, **kwargs):
    res = request("put_script", None, lang, id, body, **kwargs)
    jsonprint(res)
    return res

@task
def put_template(id, body, **kwargs):
    res = request("put_template", None, id, body, **kwargs)
    jsonprint(res)
    return res

@task
def reindex(body, **kwargs):
    res = request("reindex", None, body, **kwargs)
    jsonprint(res)
    return res

@task
def reindex_rethrottle(task_id=None, **kwargs):
    res = request("reindex_rethrottle", None, task_id=task_id, **kwargs)
    jsonprint(res)
    return res

@task
def render_search_template(id=None, body=None, **kwargs):
    res = request("render_search_template", None, id=id, body=body, **kwargs)
    jsonprint(res)
    return res

@task
def scroll(scroll_id=None, body=None, **kwargs):
    res = request("scroll", None, scroll_id=scroll_id, body=body, **kwargs)
    jsonprint(res)
    return res

@task
def search(index=None, doc_type=None, body=None, **kwargs):
    res = request("search", None, index=index, doc_type=doc_type, body=body, **kwargs)
    jsonprint(res)
    return res

@task
def search_shards(index=None, doc_type=None, **kwargs):
    res = request("search_shards", None, index=index, doc_type=doc_type, **kwargs)
    jsonprint(res)
    return res

@task
def search_template(index=None, doc_type=None, body=None, **kwargs):
    res = request("search_template", None, index=index, doc_type=doc_type, body=body, **kwargs)
    jsonprint(res)
    return res

@task
def suggest(body, index=None, **kwargs):
    res = request("suggest", None, body, index=index, **kwargs)
    jsonprint(res)
    return res

@task
def termvectors(index, doc_type, id=None, body=None, **kwargs):
    res = request("termvectors", None, index, doc_type, id=id, body=body, **kwargs)
    jsonprint(res)
    return res

@task
def update(index, doc_type, id, body=None, **kwargs):
    res = request("update", None, index, doc_type, id, body=body, **kwargs)
    jsonprint(res)
    return res

@task
def update_by_query(index, doc_type=None, body=None, **kwargs):
    res = request("update_by_query", None, index, doc_type=doc_type, body=body, **kwargs)
    jsonprint(res)
    return res
