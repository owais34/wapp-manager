from fastapi import APIRouter
from starlette.websockets import WebSocket

websocket_router = APIRouter(prefix="/ws/v1")

@websocket_router.websocket("")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("Connected to /ws/v1")