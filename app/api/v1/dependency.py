from fastapi import Request

def get_redis(request: Request):
    return request.app.state.redis

def get_rabbit(request: Request):
    return request.app.state.rabbit_client

