from aiofiles import open as aopen
from hashlib import md5


# 文件校验函数
async def getfilemd5(filePath):
    async with aopen(filePath, 'rb') as f:
        filebytes = await f.read()
    return md5(filebytes).hexdigest()