from config import Config
from fastapi import FastAPI


def create_app():
    config = Config()
    app = FastAPI(title="ETNA Search API", log_level=config.LOG_LEVEL)
    base_uri = "/api/v1"

    @app.get("/healthcheck/live/", include_in_schema=False)
    def healthcheck():
        return {"status": "ok"}

    from .articles import routes as article_routes
    from .records import routes as record_routes

    app.include_router(
        record_routes.router, prefix=f"{base_uri}/records", tags=["Records"]
    )
    app.include_router(
        article_routes.router, prefix=f"{base_uri}/articles", tags=["Articles"]
    )

    return app
