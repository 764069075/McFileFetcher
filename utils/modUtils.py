from aiohttp.client_exceptions import ClientConnectorError
from time import strftime,localtime
from os import makedirs
from os.path import join
from asyncio import sleep,gather
from aiofiles import open as aopen
from utils.configUtils import config


# mod下载流水线函数
async def moddownloadline(fileinfo:list,session,gamename:str = 'Minecraft',category:str = 'mods'):
    slug,gameVersionId,gameFlavorId = fileinfo

    async def getModId(sortField:str = 'Relevancy'):
        print('\033[36m{} {}[{}] : \033[32m已创建协程 {} {} {} \033[36m'.format(strftime(config['TIME_FORMATE'],localtime()),gamename,category,slug,gameVersionId,gameFlavorId))
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
                async with session.get( config['SEARCH_MOD_ID_BASE_URL'], params=params, proxy=config['PROXY'] ) as response:
                    js = await response.json()
                    assert js['pagination']['totalCount'] > 0,"未找到这个mod"
                    return str(js['data'][0]['id'])
            except ClientConnectorError:
                print(f'{strftime(config["TIME_FORMATE"],localtime())} {gamename}[{category}] : 下载时断开 {slug} {gameVersionId} {gameFlavorId} 重连中...次数{i+1}')
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
        }
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
            async with aopen(join(config['MOD_SAVE_DIR'],fileName),'wb')as w:
                async for chunk in response.content.iter_chunked(config['CHUNK_SIZE']):
                    await w.write(chunk)
        print(f'{strftime(config["TIME_FORMATE"],localtime())} {gamename}[{category}] : \033[32m下载完成 \033[36m{fileName} \033[33m{slug}\033[36m')
        return True
    

    try:
        modid = await getModId()
        fileid,filename = await getModDownUrl(modid)
        await downWriteFile(fileid,filename)
    except IndexError as e:
        print(f'{strftime(config["TIME_FORMATE"],localtime())} {gamename}[{category}] : \033[31m下载失败 {slug} {gameVersionId} {gameFlavorId}（没有该版本）\033[36m')
        return [f'失败（没有该版本）',modid]
    except Exception as e:
        print(f'{strftime(config["TIME_FORMATE"],localtime())} {gamename}[{category}] : \033[31m下载失败 {slug} {gameVersionId} {gameFlavorId}（{e}）\033[36m')
        return [f'失败（{e}）',modid]
    else:
        return ['成功',filename]

# 配置每条流水线
async def moddownload(fileinfos:list,session):
    makedirs(config['MOD_SAVE_DIR'],exist_ok=1)
    tasks = [moddownloadline(fileinfo,session) for fileinfo in fileinfos]
    return await gather(*tasks)