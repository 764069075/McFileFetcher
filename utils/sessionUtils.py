from aiohttp import ClientSession, TCPConnector, DummyCookieJar, ClientTimeout


conn = TCPConnector(limit_per_host= 0, limit= 0, use_dns_cache= True, ttl_dns_cache= None, enable_cleanup_closed= True, force_close= False)
timeout = ClientTimeout(6 , conn)
jar = DummyCookieJar()
session = ClientSession(proxy="", cookie_jar= jar, trust_env= True)
