def welcome():
    print('\033[36m')
    print('''
        欢迎使用 McFileFetcher MC文件一键下载工具

                  github 开源地址：

      https://github.com/764069075/McFileFetcher

                官方使用手册Wiki地址：

https://github.com/764069075/McFileFetcher/wiki/tutorial
''')
    print('\033[0m')
welcome()

from utils.pauseUtils import waitforkey
waitforkey()

from utils import printUtils
from utils.configUtils import config
from utils.csvUtils import readcsv,resultcsv
from time import time
from utils.downloadUtils import download
from asyncio import run, sleep

async def main():   
    fileinfos,length = readcsv(config['WAIT_TO_DOWN_FILE_NAME'])
    print('3妙后开始下载')
    await sleep(3)
    starttime = time()
    results = await download(fileinfos)
    waste = time()-starttime
    success = sum(['成功' in i[0] for i in results])
    failure = length-success
    print(f'下载结束，耗时：{waste:.2f}s 成功：{success} 失败：{failure}\033[0m')
    if failure == length:
        print('\033[33m【提示】全部失败了? 可以检查配置文件中代理是否正确配置，或者前往官方文档查看解决方案（https://github.com/764069075/McFileFetcher/wiki/tutorial）\033[0m')
    resultcsv(config['DOWN_STATE_FILE_NAME'],results,waste,success,length,fileinfos)
    waitforkey()

if __name__ == '__main__':
    run(main())
