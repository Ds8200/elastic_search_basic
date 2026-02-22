from src.elastic.dal import create_edge_ngram_analyzer, insert_doc, search_by_name
from src.file.json import read_json_file

path_data_products = "data/products.json"
index_name = "products"

def main():
    # create_edge_ngram_analyzer(index_name)

    # products = read_json_file(path_data_products)

    # for i, product in enumerate(products, start=1):
    #     insert_doc(index_name, i, product)

    while True:
        name = input("Enter product name to search (or 'exit' to quit): ")
        if name.lower() == "exit":
            break
        result_search = search_by_name(index_name, name)
        print(result_search)
    
if __name__ == "__main__":
    main()
