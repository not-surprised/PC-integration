from volume_control import *
from brightness_control import *
from bluetooth_test_client import *

async def brightness(client):
    currentBrightness = await client.get_brightness()
    print(currentBrightness)
    await setBrightness(currentBrightness*255/20000)


async def volume(client):
    currentVolume = await client.get_volume()
    print(currentVolume)
    await setVolume(currentVolume*100, "Speakers (Realtek(R) Audio)")


async def main():
    client = NsDummyClient()
    await client.discover_and_connect()
    while True:
        await brightness(client)
        await volume(client)
        await asyncio.sleep(1)


async def test():
    client = NsDummyClient()
    await client.discover_and_connect()
    for i in range(10):
        print(await client.get_brightness())

        await asyncio.sleep(1)

if __name__ == '__main__':
    asyncio.run(main())
