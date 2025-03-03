from aiohttp import ClientSession


def initSession():
    return ClientSession(trust_env= True)
