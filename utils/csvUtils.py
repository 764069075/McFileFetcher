from csv import writer,reader
from os.path import exists,abspath
from os import startfile,system
from utils.configUtils import config


def readcsv(waitToDownFileName):
    print(f'\033[36m开始读取 {waitToDownFileName}')
    if exists(waitToDownFileName):
        with open(waitToDownFileName, 'r') as f:
            fileinfos = [row[:len(config['DOWN_FILE_HEADER'])] for row in reader(f) if ''.join(map(str,row)).strip() and '游戏名' not in row[0]]
        if len(fileinfos) > 0:
            length = len(fileinfos)
            print(f'\033[32m已读取 {length} 个文件信息，即将开始下载')
            return fileinfos,length
        else:
            print('未能从csv读取到数据')
    else:
        print(f'未发现文件 {waitToDownFileName}')
    return createcsv(waitToDownFileName)


def createcsv(waitToDownFileName):
    print(f'\033[36m正在创建并打开文件 {waitToDownFileName}')

    with open(waitToDownFileName, 'w', newline='') as f:
        w = writer(f)
        w.writerow(config['DOWN_FILE_HEADER'])

    startfile(abspath(waitToDownFileName))
    print(f'\033[32m程序已暂停，请前往 {waitToDownFileName} 文件中按照格式填写文件信息（区分大小写）。\033[0m')
    system('pause')
    return readcsv(waitToDownFileName)


def resultcsv(downStateFileName,results,waste,success,length,fileinfos):
    for i in range(config['RELOAD_TIMES']):
        try:
            with open(downStateFileName,'w',newline='')as f:
                w = writer(f)
                w.writerow(config['DOWN_STATE_FILE_HEADER'])
                w.writerows([i+k for i,k in zip(fileinfos,results)])
                w.writerow([f'完成耗时 {waste:.2f}秒 成功 {success} 失败 {length-success}'])
        except PermissionError:
            print(f'\033[31m导出失败：\033[36m在导出文件 {downStateFileName} 时，发现该文件未关闭。\033[33m按任意键重新导出\033[0m')
            system('pause')
            continue
        except Exception as e:
            print(f'\033[31m导出失败：\033[36m在导出文件 {downStateFileName} 时，发现未知错误（{e}）。\033[33m按任意键重新导出\033[0m')
            system('pause')
            continue
    
    print(f'\033[36m所有文件下载信息已导出到文件 \033[33m{downStateFileName}\033[0m')
    startfile(abspath(downStateFileName))