from fastapi import APIRouter
from starlette.websockets import WebSocket, WebSocketDisconnect

from app.ws.utils import CONNECTION_MANAGER

websocket_router = APIRouter(prefix="/ws/v1")

@websocket_router.websocket("")
async def websocket_endpoint(websocket: WebSocket):
    await CONNECTION_MANAGER.connect(websocket)
    await CONNECTION_MANAGER.send_personal("Connected to /ws/v1", websocket)

    try:
        while True:
            data = await websocket.receive_text()
            # Echo back
            await CONNECTION_MANAGER.send_personal(f"You said: {data}", websocket)

            # Broadcast to all clients
            await CONNECTION_MANAGER.broadcast(f"Broadcast: {data}")

    except WebSocketDisconnect:
        CONNECTION_MANAGER.disconnect(websocket)