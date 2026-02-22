from src.elastic.connect import es

def create_edge_ngram_analyzer(index_name: str):
    index_body = {
        "settings": {
            "analysis": {
                "tokenizer": {
                    "autocomplete_tokenizer": {
                        "type": "edge_ngram",
                        "min_gram": 2,
                        "max_gram": 20,
                        "token_chars": ["letter", "digit"]
                    }
                },
                "analyzer": {
                    "autocomplete_analyzer": {
                        "type": "custom",
                        "tokenizer": "autocomplete_tokenizer",
                        "filter": ["lowercase"]
                    },
                    "autocomplete_search_analyzer": {
                        "type": "custom",
                        "tokenizer": "standard",
                        "filter": ["lowercase"]
                    }
                }
            }
        },
        "mappings": {
            "properties": {
                "name": {
                    "type": "text",
                    "analyzer": "autocomplete_analyzer",
                    "search_analyzer": "autocomplete_search_analyzer"
                }
            }
        }
    }

    if not es.indices.exists(index=index_name):
        es.indices.create(index=index_name, body=index_body)
    
    print(f"Created index '{index_name}' with edge_ngram analyzer👍")
    
def insert_doc(index_name: str, id: int, doc: dict):
    es.index(index=index_name, id=id, document=doc)
    print("Inserted doc👍")

def search_by_name(index_name: str, name: str) -> list[dict]:
    query={
        "match": {
            "name": name
        }
    }
    
    response = es.search(index=index_name, query=query)
    
    resolt = []
    
    for hit in response["hits"]["hits"]:
        resolt.append(hit["_source"])
    
    return resolt
    