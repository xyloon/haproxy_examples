from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/{full_path:path}")
async def root(request: Request, full_path: str):
    return {"full_path": full_path, "query_params": request.query_params}