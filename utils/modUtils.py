from aiohttp.client_exceptions import ClientConnectorError,ContentTypeError
from time import strftime,localtime
from os.path import join
from asyncio import sleep
from aiofiles import open as aopen
from utils.configUtils import config


# mod下载流水线函数
async def moddownloadline(gamename,category,slug,gameVersionId,gameFlavorId,session,sortField = config['SORT_FIELD']):

    async def getModId():
        print('\033[36m{} {}[{}] : \033[32m已创建程协 \033[36m{} {} \033[33m{} \033[0m'.format(strftime(config['TIME_FORMATE'],localtime()),gamename,category,slug,gameVersionId,gameFlavorId))
        params = {
            "gameId": config['gameIds'].get(gamename),
            "index": 0,
            "classId": config['categories'].get(category),
            "filterText": slug,
            "pageSize": 1,
            "sortField": config['sortFields'].get(sortField)
        }
        for i in range(config['RELOAD_TIMES']):
            try:
                async with session.get( config['SEARCH_MOD_ID_BASE_URL'], params=params, proxy= config['PROXY'] ) as response:
                    js = await response.json()
                    assert js['pagination']['totalCount'] > 0,f"未找到这个{category}"
                    return str(js['data'][0]['id'])
            except ClientConnectorError:
                print(f'{strftime(config["TIME_FORMATE"],localtime())} {gamename}[{category}] : \033[33m下载时断开 \033[36m{slug} {gameVersionId} {gameFlavorId} 重连中...次数{i+1}\033[0m')
                await sleep(config['RELOAD_INTERVAL'])
            else:
                break

    async def getModDownUrl(modId:str):
        params = {
            "pageIndex": 0,
            "pageSize": 1,
            "sort": "dateCreated",
            "sortDescending": 1,
            "gameVersionId": config['gameVersionIds'].get(gameVersionId),
            "gameFlavorId": config['gameFlavorIds'].get(gameFlavorId),
            'removeAlphas': config['removeAlphas'],
        }
        if category != 'mod':
            del params['gameFlavorId']
        for i in range(config['RELOAD_TIMES']):
            try:
                async with session.get('/'.join([config['SEARCH_MOD_FILE_BASE_URL'],modId,'files']),params=params,proxy=config['PROXY'])as response:
                    js = await response.json()
                    return str(js['data'][0]['id']),js['data'][0]['fileName']
            except ClientConnectorError as e:
                print(f'获取版本链接时断开 重连中...次数{i+1}')
                await sleep(config['RELOAD_INTERVAL'])
            else:
                break

    async def downWriteFile(fileId:str,fileName:str):
        url = '/'.join([config['DOWNLOAD_BASE_URL'],fileId[:-3],fileId[-3:].lstrip('0'),fileName.replace('+','%2B')])
        async with session.get(url,proxy=config['PROXY']) as response:
            assert response.status == 200, '服务器下载接口返回码异常'
            async with aopen(join(config['MOD_SAVE_DIR'] ,category+'s' ,fileName),'wb')as w:
                async for chunk in response.content.iter_chunked(config['CHUNK_SIZE']):
                    await w.write(chunk)
        print(f'\033[36m{strftime(config["TIME_FORMATE"],localtime())} {gamename}[{category}] : \033[32m下载完成 \033[36m{fileName} \033[33m{slug}\033[36m')
        return True
    

    try:
        modid = await getModId()
        fileid,filename = await getModDownUrl(modid)
        await downWriteFile(fileid,filename)
    except IndexError as e:
        print(f'\033[36m{strftime(config["TIME_FORMATE"],localtime())} {gamename}[{category}] : \033[31m下载失败 \033[36m{slug} {gameVersionId} {gameFlavorId}\033[31m（没有该版本）\033[36m')
        return [f'失败（没有该版本）',modid]
    except ContentTypeError as e:
        print(f'\033[36m{strftime(config["TIME_FORMATE"],localtime())} {gamename}[{category}] : \033[31m下载失败 \033[36m{slug} {gameVersionId} {gameFlavorId}\033[31m（代理配置无效）\033[36m')
        return [f'失败（代理配置无效/该节点被墙，请尝试修改代理地址或者更换为其他国家节点）',slug]
    except Exception as e:
        print(f'\033[36m{strftime(config["TIME_FORMATE"],localtime())} {gamename}[{category}] : \033[31m下载失败 \033[36m{slug} {gameVersionId} {gameFlavorId}\033[31m（{type(e).__name__}:{e}）\033[36m')
        return [f'失败（{e}）',modid]
    else:
        return ['成功',filename]