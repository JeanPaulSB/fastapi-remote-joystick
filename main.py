from fastapi import FastAPI, WebSocket,BackgroundTasks
from fastapi.responses import HTMLResponse
from mavsdk import System
from contextlib import asynccontextmanager
import asyncio




@asynccontextmanager
async def lifespan(app: FastAPI):

    """
    drone = System()
    loop = asyncio.get_event_loop()

    
    print("Connecting to drone...")
    await drone.connect(system_address="udp://:14540")

   

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break

    async for health in drone.telemetry.health():
        if health.is_global_position_ok and health.is_home_position_ok:
            print("-- Global position state is good enough for flying.")
            break

    print("-- Arming")
    await drone.action.arm()

    print("-- Taking off")
    await drone.action.takeoff()
    await asyncio.sleep(10)
    app.state.roll = 0.8
    app.state.yaw = 0.1
    app.state.pitch = 0.0
    app.state.thrust = 0.7
    loop.create_task(handle_controls(drone))
    print("-- wait")
    await asyncio.sleep(1)
    print("-- Starting manual control")
    await drone.manual_control.start_position_control()
    await asyncio.sleep(5)

    await drone.action.land()
    print("-- end")
    """
   

    yield


async def handle_controls(drone):
    while True:
        print("doing da work")
        await drone.manual_control.set_manual_control_input(app.state.pitch,app.state.roll,app.state.thrust,app.state.yaw)

app = FastAPI(lifespan=lifespan)





@app.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")

if __name__ == '__main__':
    print("vamooos")