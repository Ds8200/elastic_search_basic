from pathlib import Path

from src.file.json import read_json_file
from src.elastic.connect import es
from elasticsearch.helpers import bulk

current_path = Path(__file__).parent.parent.parent
path_data_config =  current_path / "data" / "config_elastic.json"


def create_products_index(index_name: str):
    index_body = read_json_file(path_data_config)

    if not es.indices.exists(index=index_name):
        es.indices.create(index=index_name, body=index_body)
        print(f"Created index '{index_name}' with edge_ngram analyzer 👍")
    else:
        print(f"Index '{index_name}' already exists 👍")
    

def insert_doc(index_name: str, id: int, doc: dict):
    es.index(index=index_name, id=id, document=doc)
    print("Inserted doc👍")
    

def insert_many_docs(index_name: str, docs: list[dict]):
    actions = [
        {
            "_index": index_name,
            "_id": idx + 1,
            "_source": product
        }
        for idx, product in enumerate(docs)
    ]

    success, errors = bulk(es, actions)

    print("Inserted:", success)
    print("Errors:", errors)


def refresh_index(index_name: str):
    es.indices.refresh(index=index_name)
    print("Refreshed index👍")


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
    