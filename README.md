# elasticsearch-cli
This package provides a unified command line interface to Elasticsearch.

## Installation

```sh
$ git clone https://github.com/KunihikoKido/elasticsearch-cli.git ~/.escli
$ cd ~/.escli
$ ./setup.sh
```

``` sh
# cat ~/.profile or ~/.bash_profile
export PATH=~/.escli/env/bin:$PATH
alias es="fab -f ~/.escli/fabfile"
```

## Examples

``` sh
# curl -XGET 'http://localhost:9200/?pretty' -d ''
$ es info

# curl -XGET 'http://localhost:9200/_search?pretty' -d ''
$ es search

# curl -XGET 'http://localhost:9200/blog/posts/_search?pretty' -d ''
$ es search:blog,posts

# curl -XGET 'http://localhost:9200/blog/posts/_search?pretty&q=Hello+Elasticsearch' -d ''
$ es search:blog,posts,q="Hello Elasticsearch"


# curl -XPOST 'http://localhost:9200/blog/posts/_search?pretty' -d '{
#   "query": {
#     "match_all": {}
#   }
# }'
$ cat query.json | es search:blog,posts

```

## Server Selection


``` yaml
# cat config/server_config.yml
default:
  host: localhost
  port: 9200
prod:
  host: prod.example.org
  port: 443
  use_ssl: true
  verify_certs: true
dev:
  host: dev.example.org
  port: 80
```


``` sh
# Request default ES Server
$ es search # OR `es s search` OR `es s:default search`

# Request `prod` ES Server
$ es s:prod search

# Request `dev` ES Server
$ es s:dev search
```
