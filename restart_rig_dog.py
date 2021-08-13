import asyncio
from logger import Logger
from kasa import *
import time
from local_constants import RIG_D_AND_BEAST_HOST_NAME

logger = Logger()

def restart_rig_dog():
    logger.log("Attempting to restart RIG-DOG")
    
    try:
        strip = SmartStrip(RIG_D_AND_BEAST_HOST_NAME)
        asyncio.run(strip.update())

        asyncio.run(turn_off_rig_dog(strip))
        time.sleep(10)
        asyncio.run(turn_on_rig_dog(strip))
    except Exception as e:
        logger.log("EXCEPTION: " + str(e))

    logger.log("RIG-DOG successfully restarted.")

async def turn_off_rig_dog(strip: SmartStrip):
    task1 = asyncio.create_task(strip.children[0].turn_off())
    task2 = asyncio.create_task(strip.children[1].turn_off())
    await task1
    await task2

async def turn_on_rig_dog(strip: SmartStrip):
    task1 = asyncio.create_task(strip.children[0].turn_on())
    task2 = asyncio.create_task(strip.children[1].turn_on())
    await task1
    await task2

restart_rig_dog()
