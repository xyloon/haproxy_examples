from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/{full_path:path}")
async def get_root(request: Request, full_path: str):
    return {"method": request.method, "full_path": full_path, "query_params": request.query_params}

@app.post("/{full_path:path}")
async def post_root(request: Request, full_path: str):
    return {"method": request.method, "full_path": full_path, "json": await request.json()}