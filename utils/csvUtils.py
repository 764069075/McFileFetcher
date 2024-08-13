from csv import writer,reader
from os.path import exists,abspath
from os import startfile,system


def readcsv(waitToDownFileName):
    print(f'开始读取 {waitToDownFileName}')
    if exists(waitToDownFileName):
        with open(waitToDownFileName, 'r') as f:
            fileinfos = list(reader(f))
        if len(fileinfos) > 1:
            length = len(fileinfos) - 1
            print(f'\033[32m已读取 {length} 个文件，即将开始下载\033[0m')
            return fileinfos[1:],length
        else:
            print('未能从csv读取到数据')
    else:
        print(f'未发现文件：{waitToDownFileName}')
    return createcsv(waitToDownFileName)


def createcsv(waitToDownFileName):
    print(f'正在创建并打开文件：{waitToDownFileName}')

    with open(waitToDownFileName, 'w', newline='') as f:
        w = writer(f)
        w.writerow(['英文名(例：jei)', '版本(例：1.18.2/1.16.5/1.12.2)', '文件环境(例：NeoForge/Forge/Fabric)'])

    startfile(abspath(waitToDownFileName))
    print(f'程序已暂停，请前往 {waitToDownFileName} 文件中按照格式填写文件信息（区分大小写）。')
    system('pause')
    return readcsv(waitToDownFileName)


def resultcsv(downStateFileName,results,waste,success,length,fileinfos):
    
    with open(downStateFileName,'w',newline='')as f:
        w = writer(f)
        w.writerow(['英文名', '版本', '文件环境', '下载结果', '对应文件名/Id'])
        w.writerows([i+k for i,k in zip(fileinfos,results)])
        w.writerow([f'下载耗时：{waste:.2f}秒 成功：{success} 失败：{length-success}'])
    
    print(f'所有文件下载信息已导出到同目录文件：{downStateFileName}\033[0m')
    startfile(abspath(downStateFileName))