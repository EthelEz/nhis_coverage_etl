import os
import pandas as pd
from whoosh.index import create_in, open_dir # type: ignore
from whoosh.fields import Schema, TEXT, ID # type: ignore
from whoosh.qparser import QueryParser # type: ignore

# Function to read CSV with the correct encoding
def read_csv_with_encoding(file_path):
    encodings = ['utf-8', 'latin1', 'iso-8859-1', 'cp1252']  # List of possible encodings
    for encoding in encodings:
        try:
            return pd.read_csv(file_path, encoding=encoding)
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError(f"Unable to read the file with provided encodings: {encodings}")

# Step 1: Read the CSV file
csv_path = "./hmo_list.csv"
df = read_csv_with_encoding(csv_path)

# Step 2: Define the schema for the index
schema = Schema(code=ID(stored=True), name=TEXT(stored=True), category=TEXT(stored=True))

# Create the index directory
index_dir = "indexdir"
if not os.path.exists(index_dir):
    os.mkdir(index_dir)

# Step 3: Create the index
ix = create_in(index_dir, schema)
writer = ix.writer()

# Add rows from the CSV to the index
for index, row in df.iterrows():
    writer.add_document(code=str(row['Code']), name=row['Name of HMO'], category=row['Category'])
writer.commit()

# Step 4: Implement the search function
def search(query_str, search_field, return_field):
    ix = open_dir(index_dir)
    with ix.searcher() as searcher:
        query = QueryParser(search_field, ix.schema).parse(query_str)
        results = searcher.search(query)
        for result in results:
            return (f"{result[return_field]}")

# Example search
# search("Hygeia HMO", "name", "category")
