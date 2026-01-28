"""
Concept: FastAPI (Path Parameters)
You can capture values from the URL path using `{variable_name}` syntax in the path and function arguments.

Task: Define a route `/items/{item_id}` that accepts an integer `item_id`.
"""

from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

# FIX ME: Define a route /items/{item_id} that returns {"item_id": item_id}
# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     return {"item_id": item_id}

client = TestClient(app)

def main():
    # We send 42 as a path parameter
    response = client.get("/items/42")
    
    if response.status_code == 404:
        raise Exception("Route /items/{item_id} not found!")
        
    data = response.json()
    if data.get("item_id") != 42:
        raise Exception(f"Expected item_id 42, got {data.get('item_id')}")
        
    print("FastAPI path params verified!")

if __name__ == "__main__":
    main()
