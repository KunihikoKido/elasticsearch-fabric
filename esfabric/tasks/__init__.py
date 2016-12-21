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
    """
    Get the basic info from the current cluster.
    http://www.elastic.co/guide/
    """
    res = request("info", None, **kwargs)
    jsonprint(res)
    return res

@task
def create(index, doc_type, id, body, **kwargs):
    """
    Adds a typed JSON document in a specific index, making it searchable.
    Behind the scenes this method calls index(..., op_type=’create’)
    http://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html
    """
    res = request("create", None, index, doc_type, id, body, **kwargs)
    jsonprint(res)
    return res

@task
def index(index, doc_type, body, id=None, **kwargs):
    """
    Adds or updates a typed JSON document in a specific index, making it searchable.
    http://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html
    """
    res = request("index", None, index, doc_type, body, id=None, **kwargs)
    jsonprint(res)
    return res

@task
def exists(index, doc_type, id, **kwargs):
    """
    Returns a boolean indicating whether or not given document exists in Elasticsearch.
    http://www.elastic.co/guide/en/elasticsearch/reference/current/docs-get.html
    """
    res = request("exists", None, index, doc_type, id, **kwargs)
    jsonprint(res)
    return res

@task
def bulk(body, index=None, doc_type=None, **kwargs):
    """
    Perform many index/delete operations in a single API call.
    See the bulk() helper function for a more friendly API.
    http://www.elastic.co/guide/en/elasticsearch/reference/current/docs-bulk.html
    """
    res = request("bulk", None, body, index=index, doc_type=doc_type, **kwargs)
    jsonprint(res)
    return res

@task
def clear_scroll(scroll_id=None, body=None, **kwargs):
    """
    Clear the scroll request created by specifying the scroll parameter to search.
    http://www.elastic.co/guide/en/elasticsearch/reference/current/search-request-scroll.html
    """
    res = request("clear_scroll", None, scroll_id=scroll_id, body=body, **kwargs)
    jsonprint(res)
    return res

@task
def count(index=None, doc_type=None, body=None, **kwargs):
    """
    Execute a query and get the number of matches for that query.
    http://www.elastic.co/guide/en/elasticsearch/reference/current/search-count.html
    """
    res = request("count", None, index=index, doc_type=doc_type, body=body, **kwargs)
    jsonprint(res)
    return res

@task
def count_percolate(index, doc_type, id=None, body=None, **kwargs):
    """
    The percolator allows to register queries against an index,
    and then send percolate requests which include a doc,
    and getting back the queries that match on that doc out of the set of registered queries.
    http://www.elastic.co/guide/en/elasticsearch/reference/current/search-percolate.html
    """
    res = request("count_percolate", None, index, doc_type, id=id, body=body, **kwargs)
    jsonprint(res)
    return res

@task
def delete(index, doc_type, id, **kwargs):
    """
    Delete a typed JSON document from a specific index based on its id.
    http://www.elastic.co/guide/en/elasticsearch/reference/current/docs-delete.html
    """
    res = request("delete", None, index, doc_type, id, **kwargs)
    jsonprint(res)
    return res

@task
def delete_by_query(index, body, doc_type=None, **kwargs):
    """
    Delete all documents matching a query.
    https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-delete-by-query.html
    """
    res = request("delete_by_query", None, index, body, doc_type=doc_type, **kwargs)
    jsonprint(res)
    return res

@task
def delete_script(lang, id, **kwargs):
    """
    Remove a stored script from elasticsearch.
    http://www.elastic.co/guide/en/elasticsearch/reference/current/modules-scripting.html
    """
    res = request("delete_script", None, lang, id, **kwargs)
    jsonprint(res)
    return res

@task
def delete_template(id, **kwargs):
    """
    Delete a search template.
    http://www.elastic.co/guide/en/elasticsearch/reference/current/search-template.html
    """
    res = request("delete_template", None, id, **kwargs)
    jsonprint(res)
    return res

@task
def explain(index, doc_type, id, body=None, **kwargs):
    """
    The explain api computes a score explanation for a query and a specific document.
    This can give useful feedback whether a document matches or didn’t match a specific query.
    http://www.elastic.co/guide/en/elasticsearch/reference/current/search-explain.html
    """
    res = request("explain", None, index, doc_type, id, body=body, **kwargs)
    jsonprint(res)
    return res

@task
def field_stats(index=None, body=None, **kwargs):
    """
    The field stats api allows one to find statistical properties of a field without executing a search,
    but looking up measurements that are natively available in the Lucene index.
    http://www.elastic.co/guide/en/elasticsearch/reference/current/search-field-stats.html
    """
    res = request("field_stats", None, index=index, body=body, **kwargs)
    jsonprint(res)
    return res

@task
def get(index, id, doc_type='_all', **kwargs):
    """
    Get a typed JSON document from the index based on its id.
    http://www.elastic.co/guide/en/elasticsearch/reference/current/docs-get.html
    """
    res = request("get", None, index, id, doc_type=doc_type, **kwargs)
    jsonprint(res)
    return res

@task
def get_script(lang, id, **kwargs):
    """
    Retrieve a script from the API.
    http://www.elastic.co/guide/en/elasticsearch/reference/current/modules-scripting.html
    """
    res = request("get_script", None, lang, id, **kwargs)
    jsonprint(res)
    return res

@task
def get_source(index, doc_type, id, **kwargs):
    """
    Get the source of a document by it’s index, type and id.
    http://www.elastic.co/guide/en/elasticsearch/reference/current/docs-get.html
    """
    res = request("get_source", None, index, doc_type, id, **kwargs)
    jsonprint(res)
    return res

@task
def get_template(id, **kwargs):
    """
    Retrieve a search template.
    http://www.elastic.co/guide/en/elasticsearch/reference/current/search-template.html
    """
    res = request("get_template", None, id, **kwargs)
    jsonprint(res)
    return res

@task
def mget(body, index=None, doc_type=None, **kwargs):
    """
    Get multiple documents based on an index, type (optional) and ids.
    http://www.elastic.co/guide/en/elasticsearch/reference/current/docs-multi-get.html
    """
    res = request("mget", None, body, index=index, doc_type=doc_type, **kwargs)
    jsonprint(res)
    return res

@task
def mpercolate(body, index=None, doc_type=None, **kwargs):
    """
    The percolator allows to register queries against an index,
    and then send percolate requests which include a doc,
    and getting back the queries that match on that doc out of the set of registered queries.
    http://www.elastic.co/guide/en/elasticsearch/reference/current/search-percolate.html
    """
    res = request("mpercolate", None, body, index=index, doc_type=doc_type, **kwargs)
    jsonprint(res)
    return res

@task
def msearch(body, index=None, doc_type=None, **kwargs):
    """
    Execute several search requests within the same API.
    http://www.elastic.co/guide/en/elasticsearch/reference/current/search-multi-search.html
    """
    res = request("msearch", None, body, index=index, doc_type=doc_type, **kwargs)
    jsonprint(res)
    return res

@task
def msearch_template(body, index=None, doc_type=None, **kwargs):
    """
    The /_search/template endpoint allows to use the mustache language to pre render search requests,
    before they are executed and fill existing templates with template parameters.
    http://www.elastic.co/guide/en/elasticsearch/reference/current/search-template.html
    """
    res = request("msearch_template", None, body, index=index, doc_type=doc_type, **kwargs)
    jsonprint(res)
    return res

@task
def mtermvectors(index=None, doc_type=None, body=None, **kwargs):
    """
    Multi termvectors API allows to get multiple termvectors based on an index, type and id.
    http://www.elastic.co/guide/en/elasticsearch/reference/current/docs-multi-termvectors.html
    """
    res = request("mtermvectors", None, index=index, doc_type=doc_type, body=body, **kwargs)
    jsonprint(res)
    return res

@task
def percolate(index, doc_type, id=None, body=None, **kwargs):
    """
    The percolator allows to register queries against an index,
    and then send percolate requests which include a doc,
    and getting back the queries that match on that doc out of the set of registered queries.
    http://www.elastic.co/guide/en/elasticsearch/reference/current/search-percolate.html
    """
    res = request("percolate", None, index, doc_type, id=id, body=body, **kwargs)
    jsonprint(res)
    return res

@task
def ping(**kwargs):
    """
    Returns True if the cluster is up, False otherwise.
    http://www.elastic.co/guide/
    """
    res = request("ping", None, **kwargs)
    jsonprint(res)
    return res

@task
def put_script(lang, id, body, **kwargs):
    """
    Create a script in given language with specified ID.
    http://www.elastic.co/guide/en/elasticsearch/reference/current/modules-scripting.html
    """
    res = request("put_script", None, lang, id, body, **kwargs)
    jsonprint(res)
    return res

@task
def put_template(id, body, **kwargs):
    """
    Create a search template.
    http://www.elastic.co/guide/en/elasticsearch/reference/current/search-template.html
    """
    res = request("put_template", None, id, body, **kwargs)
    jsonprint(res)
    return res

@task
def reindex(body, **kwargs):
    """
    Reindex all documents from one index to another.
    https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-reindex.html
    """
    res = request("reindex", None, body, **kwargs)
    jsonprint(res)
    return res

@task
def reindex_rethrottle(task_id=None, **kwargs):
    """
    Change the value of requests_per_second of a running reindex task.
    https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-reindex.html
    """
    res = request("reindex_rethrottle", None, task_id=task_id, **kwargs)
    jsonprint(res)
    return res

@task
def render_search_template(id=None, body=None, **kwargs):
    """
    http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/search-template.html
    """
    res = request("render_search_template", None, id=id, body=body, **kwargs)
    jsonprint(res)
    return res

@task
def scroll(scroll_id=None, body=None, **kwargs):
    """
    Scroll a search request created by specifying the scroll parameter.
    http://www.elastic.co/guide/en/elasticsearch/reference/current/search-request-scroll.html
    """
    res = request("scroll", None, scroll_id=scroll_id, body=body, **kwargs)
    jsonprint(res)
    return res

@task
def search(index=None, doc_type=None, body=None, **kwargs):
    """
    Execute a search query and get back search hits that match the query.
    http://www.elastic.co/guide/en/elasticsearch/reference/current/search-search.html
    """
    res = request("search", None, index=index, doc_type=doc_type, body=body, **kwargs)
    jsonprint(res)
    return res

@task
def search_shards(index=None, doc_type=None, **kwargs):
    """
    The search shards api returns the indices and shards that a search request would be executed against.
    This can give useful feedback for working out issues or planning optimizations with routing and shard preferences.
    http://www.elastic.co/guide/en/elasticsearch/reference/current/search-shards.html
    """
    res = request("search_shards", None, index=index, doc_type=doc_type, **kwargs)
    jsonprint(res)
    return res

@task
def search_template(index=None, doc_type=None, body=None, **kwargs):
    """
    A query that accepts a query template and a map of key/value pairs to fill in template parameters.
    http://www.elastic.co/guide/en/elasticsearch/reference/current/search-template.html
    """
    res = request("search_template", None, index=index, doc_type=doc_type, body=body, **kwargs)
    jsonprint(res)
    return res

@task
def suggest(body, index=None, **kwargs):
    """
    The suggest feature suggests similar looking terms based on a provided text by using a suggester.
    http://www.elastic.co/guide/en/elasticsearch/reference/current/search-suggesters.html
    """
    res = request("suggest", None, body, index=index, **kwargs)
    jsonprint(res)
    return res

@task
def termvectors(index, doc_type, id=None, body=None, **kwargs):
    """
    Returns information and statistics on terms in the fields of a particular document.
    The document could be stored in the index or artificially provided by the user (Added in 1.4).
    Note that for documents stored in the index,
    this is a near realtime API as the term vectors are not available until the next refresh.
    http://www.elastic.co/guide/en/elasticsearch/reference/current/docs-termvectors.html
    """
    res = request("termvectors", None, index, doc_type, id=id, body=body, **kwargs)
    jsonprint(res)
    return res

@task
def update(index, doc_type, id, body=None, **kwargs):
    """
    Update a document based on a script or partial data provided.
    http://www.elastic.co/guide/en/elasticsearch/reference/current/docs-update.html
    """
    res = request("update", None, index, doc_type, id, body=body, **kwargs)
    jsonprint(res)
    return res

@task
def update_by_query(index, doc_type=None, body=None, **kwargs):
    """
    Perform an update on all documents matching a query.
    https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-update-by-query.html
    """
    res = request("update_by_query", None, index, doc_type=doc_type, body=body, **kwargs)
    jsonprint(res)
    return res
