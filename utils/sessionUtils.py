from aiohttp import ClientSession, TCPConnector, DummyCookieJar
from utils.configUtils import config


def initSession():
    conn = TCPConnector(limit_per_host= 0, limit= 0, use_dns_cache= True, ttl_dns_cache= None, enable_cleanup_closed= True, force_close= False)
    jar = DummyCookieJar()
    if config["PROXY"]:
        return ClientSession(proxy= config["PROXY"], cookie_jar= jar, trust_env= True, connector= conn)
    else:
        return ClientSession(cookie_jar=jar, trust_env=True, connector=conn)
