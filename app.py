from sanic import Sanic
from sanic.response import json
import os

app = Sanic(__name__)

@app.get("/")
async def root_path(request):
    return json({"message": "API está em execução."})

app.run(host="0.0.0.0", port=7777, debug=True, access_log=False, fast=True)