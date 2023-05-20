from fastapi import FastAPI

from service import config


app_config = config.load_from_env()


def create_app():
    app_fastapi = FastAPI()   

    return app_fastapi
