"""
Concept: FastAPI (Basics)
FastAPI is a modern web framework. You define routes using decorators like `@app.get("/")`.

Task: Define a root route `/` that returns `{"message": "Hello World"}`.
"""

from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

# FIX ME: Create a root route "/" that returns {"message": "Hello World"}
# @app.get("/")
# def read_root():
#     return {"message": "Hello World"}

client = TestClient(app)

def main():
    response = client.get("/")
    if response.status_code == 404:
         raise Exception("Root route not found! Define @app.get('/')")
         
    if response.json() != {"message": "Hello World"}:
        raise Exception(f"Wrong response: {response.json()}")
        
    print("FastAPI app verified!")

if __name__ == "__main__":
    main()
