from elasticsearch import Elasticsearch
from fabric.api import env
from esfabric import tasks as es
from esfabric.tasks.utils import server_selection


env.elasticsearch_clients = {
    "default": Elasticsearch(**{
        "host": "localhost",
        "port": 9200
    }),
    "prod": Elasticsearch(**{
        "host": "search.example.org",
        "port": 443,
        "use_ssl": True,
        "verify_certs": True
    })
}
