from subprocess import run
from aiofiles import open as aopen
from hashlib import md5
from platform import system

plat = system()

# 文件校验函数
async def getfilemd5(filePath):
    async with aopen(filePath, 'rb') as f:
        filebytes = await f.read()
    return md5(filebytes).hexdigest()

def openfile(filepath):
    try:
        if plat == "Windows":
            run(['start', '', filepath], shell=True)
        elif plat == "Darwin":
            run(['open', filepath])
        else:
            run(['xdg-open', filepath])
    except Exception as e:
        print(f"X 打开文件失败: {str(e)}")