from fastapi import FastAPI
from starlette.requests import Request


def initialize_routers(server: FastAPI):
    from app.product.views import product_router
    server.include_router(product_router, prefix="/products", tags=["Product"])


def add_session_maker_middleware(app: FastAPI):

    from app.database import SessionLocal

    @app.middleware("http")
    async def db_session_middleware(request: Request, call_next):
        try:
            request.state.db = SessionLocal()
            response = await call_next(request)
        finally:
            request.state.db.close()
        return response
