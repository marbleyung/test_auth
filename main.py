import asyncio
import random

from telethon import TelegramClient, utils
from telethon.tl.types import User
from environs import Env
from telethon.tl.functions.messages import ToggleDialogPinRequest


env = Env()
env.read_env(r'.env')
USERNAME = env('USERNAME')
API_ID = env('API_ID')
API_HASH = env('API_HASH')
PHONE = env('PHONE')
client = TelegramClient(USERNAME, API_ID, API_HASH)


async def main():
    #Move groups to archieve
    async for dialog in client.iter_dialogs(archived=False):
        entity = await client.get_entity(dialog)
        if isinstance(entity, User):
            pass
        else:
            await client.edit_folder(entity=entity, folder=1)

    #Pin archieved
    async for dialog in client.iter_dialogs(archived=True):
        entity = await client.get_entity(dialog)
        if isinstance(entity, User):
            pass
        else:
            input_peer = utils.get_input_peer(entity)
            await client(ToggleDialogPinRequest(input_peer, pinned=True))
        n = random.randint(1, 3)
        await asyncio.sleep(n)

with client:
    client.loop.run_until_complete(main())
