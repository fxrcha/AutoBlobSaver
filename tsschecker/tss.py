import asyncio

from packaging.version import parse
from pyapple import Client
from utils import Logger


class TSSSaver:
    def __init__(self, config: dict) -> None:
        self.client = Client()
        self.logger = Logger.generate("TSS")
        self.config = config

    async def save_blob(self, target: dict, version: str):
        pass

    async def start(self):
        prev_ver = {}
        now_ver = {}

        for device in self.config["devices"]:

            self.logger.info(f"Device loaded - {device['identifier']}")
            prev_ver[device["identifier"]] = "0.0.0"

        while True:
            for device in self.config["devices"]:
                identifier = device["identifier"]

                self.logger.debug(f"Checking firmwares for {identifier}")
                device_data = await self.client.device(identifier)

                now_ver[identifier] = device_data.firmwares[0].version
                self.logger.debug(
                    f"previous version: {prev_ver[identifier]}, now: {now_ver[identifier]}"
                )

                if parse(prev_ver[identifier]) < parse(now_ver[identifier]):
                    self.logger.info(
                        f"Higher version detected for {identifier} (or first try). Now making SHSH2"
                    )
                    await self.save_blob(device, now_ver[identifier])

            await asyncio.sleep(self.config["time"])
