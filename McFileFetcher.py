import utils.printUtils
from utils.configUtils import config
from utils.csvUtils import readcsv,resultcsv
from time import time
from os import system
from utils.downloadUtils import download
from asyncio import run


def welcome():
    print('''\033[36m
 欢迎使用 McFileFetcher MC文件一键下载工具

            github 开源地址：

https://github.com/764069075/McFileFetcher
\033[0m''')


async def main():
    welcome()
    fileinfos,length = readcsv(config['WAIT_TO_DOWN_FILE_NAME'])
    system('timeout /t 3')
    starttime = time()
    results = await download(fileinfos)
    waste = time()-starttime
    success = sum([i.count('成功') for i in results])
    failure = length-success
    print(f'下载结束，耗时：{waste:.2f}s 成功：{success} 失败：{failure}\033[0m')
    if failure == length:
        print('\033[33m【提示】下载全部失败了?可以检查配置文件中代理是否正确配置\033[0m')
    resultcsv(config['DOWN_STATE_FILE_NAME'],results,waste,success,length,fileinfos)
    system('pause')

if __name__ == '__main__':
    run(main())