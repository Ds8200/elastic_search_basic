from src.elastic.dal import create_products_index, insert_many_docs, refresh_index, search_by_name
from src.file.json import read_json_file

path_data_products = "data/products.json"
index_name = "products"

def main():
    create_products_index(index_name)

    products = read_json_file(path_data_products)

    insert_many_docs(index_name, products)
    
    refresh_index(index_name)

    while True:
        name = input("Enter product name to search (or 'exit' to quit): ")
        if name.lower() == "exit":
            break
        result_search = search_by_name(index_name, name)
        print(result_search)
    
if __name__ == "__main__":
    main()
