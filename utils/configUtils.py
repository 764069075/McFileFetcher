from os import startfile,system
from tomlkit import dump,loads,load
from os.path import exists,abspath


configFileName = 'config.toml'
defaultConfig = '''
##### 配置文件 #####

######################################
# 文件损坏或内容错误不记得改回
# 直接删除本文件，重新运行程序即可
# 如果盆友你有相关编程兴趣爱好
# 本程序已经尽作者可能的做了模块化开发
# 欢迎随时提供相关功能代码改进丰富本程序
######################################

### 基础常量
# 代理地址(不启用设置为:"",启用需输入字符串地址,例:"http://localhost:7890")
# 国内必须配置代理
# 国外配置可选
PROXY = ""
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
# 待下载文件信息表存放路径与名称
WAIT_TO_DOWN_FILE_NAME = "待下载文件表.csv"
# 文件下载结果表存放路径与名称
DOWN_STATE_FILE_NAME = "文件下载结果表.csv"
# 查询排序方式(见下方排序表)
SORT_FIELD = "Relevancy"
# 查询排除测试版(true/false)
removeAlphas = "false"

# 输出文本前缀(未实现)
PRINT_PREFIX = ""
# 输出文本后缀(未实现)
PRINT_SUFFIX = ""


### 接口链接常量(请勿轻易修改)
# 查询MODID接口
SEARCH_MOD_ID_BASE_URL = "https://www.curseforge.com/api/v1/mods/search"
# 查询MOD版本文件接口
SEARCH_MOD_FILE_BASE_URL = "https://www.curseforge.com/api/v1/mods"
# MOD下载接口
DOWNLOAD_BASE_URL = "https://mediafilez.forgecdn.net/files"


### 字典映射表(请勿轻易修改)
# 需要下载其他版本的盆友
# 需要在对应栏目添加相关版本和id
# 游戏表
[gameIds]
'Minecraft' = 432
'The Sims 4' = 78062

# 类别表
[categories]
'Shaders' = 6552
'mods' = 6
'Modpacks' = 4471
'Customization' = 4546
'Data Packs' = 6945
'Addons' = 4559
'Bukkit Plugins' = 5
'Resource Packs' = 12
'Worlds' = 17

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
[gameVersionIds]
'1.21.1' = 11779
'1.21' = 11457
'1.20.6' = 11198
'1.20.4' = 10407
'1.20.2' = 10236
'1.20.1' = 9990
'1.20' = 9971
'1.19.4' = 9776
'1.19.3' = 9550
'1.19.2' = 9366
'1.18.2' = 9008
'1.18.1' = 8857
'1.18' = 8830
'1.17.1' = 8516
'1.16.5' = 8203
'1.16.4' = 8134
'1.16.3' = 8056
'1.12.2' = 6756
'1.12.1' = 6711
'1.12' = 6580
'1.11.2' = 6452
'1.11' = 6317
'1.10.2' = 6170
'1.10' = 6144
'1.9.4' = 6084
'1.9' = 5946
'1.8.9' = 5806
'1.8.8' = 5703
'1.8' = 4455
'''

def saveconfig():
    print('正在生成默认配置文件...')
    with open(configFileName,'w',encoding='utf8') as f:
        dump(loads(defaultConfig.strip()),f)
    startfile(abspath(configFileName))
    print('\033[32m已生成默认配置文件。程序已暂停，您现在可以修改配置信息。\033[0m')
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