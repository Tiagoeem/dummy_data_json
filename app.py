from sanic import Sanic
from sanic.response import json
import os

app = Sanic(__name__)

@app.get("/")
async def handler(request):
    return json({"info": "API em execução."})

cpus_count = os.cpu_count()
workers = cpus_count * 2 + 1
app.run(host="0.0.0.0", port=7777, debug=True, access_log=False, single_process=True)#workers=workers)