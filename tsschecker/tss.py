import asyncio

from aiohttp.client_exceptions import ContentTypeError
from packaging.version import parse
from pyapple import Client
from utils import Logger


class TSSSaver:
    def __init__(self, config: dict) -> None:
        self.client = Client()
        self.logger = Logger.generate("TSS")
        self.config = config

    async def save_blob(self, target, version: str):
        self.logger.info(f"Starting tsschecker for {target['name']}, iOS {version}")

    async def start(self):
        prev_ver = {}
        now_ver = {}

        for device in self.config["devices"]:
            try:
                identifier = device["identifier"]

                device_data = await self.client.device(identifier)
                self.logger.info(f"Device loaded - {device_data.name}")

                device["boardconfig"] = device_data.boardconfig
                device["platform"] = device_data.platform
                device["name"] = device_data.name
                prev_ver[identifier] = "0.0.0"
            except ContentTypeError:
                self.logger.error(
                    f"Unknown identifier detected: {device['identifier']}, please review your config.json"
                )
                exit(0)

        while True:
            for device in self.config["devices"]:
                identifier = device["identifier"]

                self.logger.debug(f"Checking firmwares for {device['name']}")
                device_data = await self.client.device(identifier)

                now_ver[identifier] = device_data.firmwares[0].version
                self.logger.debug(
                    f"previous version: {prev_ver[identifier]}, now: {now_ver[identifier]}"
                )

                if (
                    parse(prev_ver[identifier]) < parse(now_ver[identifier])
                    and device_data.firmwares[0].signed
                ):
                    self.logger.info(
                        f"Higher signed version detected for {device_data.name} (or first try)"
                    )
                    await self.save_blob(device, now_ver[identifier])

            await asyncio.sleep(self.config["time"])
