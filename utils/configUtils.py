from os import startfile,system
from tomlkit import dump,loads,load
from os.path import exists,abspath


configFileName = 'config.toml'
defaultConfig = '''
##### 配置文件 #####

######################################
# 文件损坏或内容错误不记得改回
# 直接删除本文件，重新运行程序即可
# CurseForge服务器被墙严重
# 所以本人只实现了走代理一种下载方式
# 所以有代理地址的盆友
# 需要根据自己的代理地址修改下方代理地址
# 没有的盆友本程序暂未提供此下载功能
# 不过如果盆友你有相关编程兴趣爱好
# 本程序已经尽作者可能的做了模块化开发
# 欢迎随时提供相关功能代码改进丰富本程序
######################################

### 基础常量
# 代理地址
PROXY = "http://localhost:7897"
# 文件流大小/byte(越大下载越快，但是占用内存高)
CHUNK_SIZE = 1024
# 模组保存目录
MOD_SAVE_DIR = "downloaded_mods"
# 中断重连次数
RELOAD_TIMES = 3
# 每次重连间隔/s
RELOAD_INTERVAL = 1
# 时间显示格式
TIME_FORMATE = "%H:%M:%S"
# 输出文本前缀(未实现)
PRINT_PREFIX = ""
# 输出文本后缀(未实现)
PRINT_SUFFIX = ""
# 待下载文件信息表名称
WAIT_TO_DOWN_FILE_NAME = "待下载文件.csv"
# 文件下载结果表名称
DOWN_STATE_FILE_NAME = "文件下载结果表.csv"
# 查询排序方式(见下方排序表)
SORT_FIELD = "Relevancy"

### 接口链接常量(请勿轻易修改)
# 查询MODID接口
SEARCH_MOD_ID_BASE_URL = "https://www.curseforge.com/api/v1/mods/search"
# 查询MOD版本文件接口
SEARCH_MOD_FILE_BASE_URL = "https://www.curseforge.com/api/v1/mods"
# MOD下载接口
DOWNLOAD_BASE_URL = "https://mediafilez.forgecdn.net/files"

### 字典映射表(请勿轻易修改)
# 游戏表
[gameIds]
'Minecraft' = 432

# 类别表
[categories]
'mods' = 6

# 排序表
[sortFields]
'Relevancy' = 1
'Popularity' = 2
'Latest update' = 3
'Creation Date' = 4
'Total Downloads' = 5
'A-Z' = 6

# mod环境表
[gameFlavorIds]
'Forge' = 1
'Fabric' = 4
'NeoForge' = 6

# 游戏版本表
# 需要下载其他版本的盆友
# 需要在此添加相关版本id
[gameVersionIds]
'1.21' = 11457
'1.20.6' = 11198
'1.20.4' = 10407
'1.18.2' = 9008
'1.16.5' = 8203
'1.12.2' = 6756
'''

def saveconfig():
    print('正在生成默认配置文件...')
    with open(configFileName,'w',encoding='utf8') as f:
        dump(loads(defaultConfig.strip()),f)
    startfile(abspath(configFileName))
    print('已生成默认配置文件。程序已暂停，您现在可以修改配置信息。')
    system('pause')
    return loadconfig()

def loadconfig():
    if exists(configFileName):
        print('正在读取配置文件...')
        with open(configFileName,'r',encoding='utf8')as f:
            config =  load(f)
        print('\033[32m配置载入成功!\033[0m')
        return config
    else:
        return saveconfig()

config = loadconfig()