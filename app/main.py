
from fastapi import FastAPI
from app.init import initialize_routers, add_session_maker_middleware

server = FastAPI(docs_url="/", title="Shoppp")


initialize_routers(server=server)

add_session_maker_middleware(app=server)

