from utils.configUtils import config
from utils.csvUtils import readcsv,resultcsv
from time import time
from os import system
from utils.modUtils import moddownload
from utils.sessionUtils import initSession
from asyncio import run


async def main():
    fileinfos,length = readcsv(config['WAIT_TO_DOWN_FILE_NAME'])
    system('timeout /t 2')
    starttime = time()
    session = initSession()
    results = await moddownload(fileinfos,session)
    waste = time()-starttime
    success = sum([i.count('成功') for i in results])
    await session.close()
    print(f'下载结束，耗时：{waste:.2f}s 成功：{success}失败：{length-success}')
    resultcsv(config['DOWN_STATE_FILE_NAME'],results,waste,success,length,fileinfos)
    system('pause')

if __name__ == '__main__':
    run(main())