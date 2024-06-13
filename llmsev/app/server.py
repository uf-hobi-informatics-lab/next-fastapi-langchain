from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from neo4j_advanced_rag import chain as neo4j_advanced_chain

app = FastAPI()


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


@app.get("/llmsev/python")
def hello_world():
    return {"message": "Hello World"}

# Edit this to add the chain you want to add
add_routes(app, neo4j_advanced_chain, path="/neo4j-advanced-rag")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
