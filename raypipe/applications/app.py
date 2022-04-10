from fastapi.routing import APIRoute as FastAPIRoute
from fastapi import FastAPI, Request, Response,status
from typing import Callable, Any, Optional
from fastapi.responses import ORJSONResponse
from fastapi import Request
import orjson

from exceptions import _EXCEPTION_HANDLERS
from sql import endpoints
from sql.database import Base,engine
from raypipe.config import FASTAPI_DEBUG

"""
include sql
design interface
test @serve.deployment(name="demo", route_prefix="/demo", version="v1")
@serve.ingress(app)
"""


class ORJSONRequest(Request):
    """
    Custom request class which uses `orjson`.
    """

    async def json(self) -> Any:
        if not hasattr(self, "_json"):
            body = await self.body()
            self._json = orjson.loads(body)
        return self._json




class APIRoute(FastAPIRoute):
    """
    Custom route to use ORJSONRequest handler.
    """

    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            request = ORJSONRequest(request.scope, request.receive)
            return await original_route_handler(request)

        return custom_route_handler



def create_app() -> FastAPI:
    routes = [
        APIRoute(
            "/",
            endpoints.index,
            methods=["GET"],
        ),
        APIRoute(
            "/v1/models/{exp_id}",
            endpoints.get_models,
            methods = ["GET"],
        ),
        APIRoute(
            "/v1/model/{model_id}",
            endpoints.get_model,
            methods=["GET"],
        ),
        APIRoute(
            "/v2/model",
            endpoints.add_model,
            methods=["POST"],
        ),
        APIRoute(
            "/v1/algos",
            endpoints.get_algorithms,
            methods=["GET"],
        ),
        APIRoute(
            "/v1/algo",
            endpoints.add_algorithm,
            methods=["POST"],
        ),
        APIRoute(
            "/v1/experiments/{algo_id}",
            endpoints.get_experiments,
            methods=["GET"],
        ),
        APIRoute(
            "/v1/experiment/{exp_id}",
            endpoints.get_experiment,
            methods=["GET"],
        ),
        APIRoute(
            "/v2/experiment",
            endpoints.add_experiment,
            methods=["POST"],
        )
    ]

    routes += [
    ]

    Base.metadata.create_all(bind=engine)

    app = FastAPI(
        debug=FASTAPI_DEBUG,
        routes=routes,  # type: ignore
        default_response_class=ORJSONResponse,
        exception_handlers=_EXCEPTION_HANDLERS,  # type: ignore
    )

    return app
