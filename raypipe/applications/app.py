from fastapi.routing import APIRoute as FastAPIRoute
from fastapi import FastAPI, Request, Response
from typing import Callable,Any
from fastapi.responses import ORJSONResponse
from fastapi import Request
import orjson

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
        # Model ready
        APIRoute(
            "/v2/models/{model_name}/ready",
            endpoints.model_ready,
        ),
        APIRoute(
            "/v2/models/{model_name}/versions/{model_version}/ready",
            endpoints.model_ready,
        ),
        # Model infer
        APIRoute(
            "/v2/models/{model_name}/infer",
            endpoints.infer,
            methods=["POST"],
        ),
        APIRoute(
            "/v2/models/{model_name}/versions/{model_version}/infer",
            endpoints.infer,
            methods=["POST"],
        ),
        # Model metadata
        APIRoute(
            "/v2/models/{model_name}",
            endpoints.model_metadata,
        ),
        APIRoute(
            "/v2/models/{model_name}/versions/{model_version}",
            endpoints.model_metadata,
        ),
        # Liveness and readiness
        APIRoute("/v2/health/live", endpoints.live),
        APIRoute("/v2/health/ready", endpoints.ready),
        # Server metadata
        APIRoute(
            "/v2",
            endpoints.metadata,
        ),
    ]

    routes += [
        # Model Repository API
        APIRoute(
            "/v2/repository/index",
            model_repository_endpoints.index,
            methods=["POST"],
        ),
        APIRoute(
            "/v2/repository/models/{model_name}/load",
            model_repository_endpoints.load,
            methods=["POST"],
        ),
        APIRoute(
            "/v2/repository/models/{model_name}/unload",
            model_repository_endpoints.unload,
            methods=["POST"],
        ),
    ]

    app = FastAPI(
        debug=FASTAPI_DEBUG,
        routes=routes,  # type: ignore
        default_response_class=ORJSONResponse,
        exception_handlers=_EXCEPTION_HANDLERS,  # type: ignore
    )

    return app
