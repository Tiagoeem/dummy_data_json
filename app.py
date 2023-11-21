from sanic import Sanic
from sanic.response import json
import os

app = Sanic("app")

@app.get("/")
async def handler(request):
    return json({"info": "API em execução."})

cpus_count = os.cpu_count()
workers = cpus_count * 2 + 1

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=bool(os.environ.get('DEBUG', '')), access_log=False, workers=int(os.environ.get('WEB_CONCURRENCY', 1)))