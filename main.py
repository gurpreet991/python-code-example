import uvicorn
from fastapi import FastAPI, logger
from fastapi.security import HTTPBearer
from fastapi_versionizer.versionizer import Versionizer

from config import *
from routes import *


auth_scheme = HTTPBearer()

app = FastAPI(
    swagger_ui_parameters={"displayRequestDuration": True})

app.debug = get_settings().DEBUG
app.title = "APIs"
app.add_middleware(**cors_config)


# include routes
app.include_router(apis.routes.router)

versions = Versionizer(
    app=app,
    prefix_format='/api/v{major}',
    semantic_version_format='{major}',
    sort_routes=True
).versionize()


def run_server():
    try:
        uvicorn.run("main:app", reload=True)
    except Exception as e:
        logger.error(f"Server Already Running {e}")


application = app

if __name__ == "__main__":
    uvicorn.run(application, forwarded_allow_ips="*")
