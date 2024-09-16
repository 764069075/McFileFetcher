from utils.sessionUtils import initSession
from utils.modUtils import moddownloadline
from utils.configUtils import config
from os import makedirs
from os.path import join
from asyncio import gather


def readydirs(fileinfos):
    categories = set([row[1] for row in fileinfos if len(row) > 1])
    for category in categories:
        makedirs(join(config['MOD_SAVE_DIR'], category+'s'),exist_ok=True)


async def download(fileinfos:list):
    readydirs(fileinfos)
    session = initSession()
    tasks = []

    for gamename,category,slug,gameVersionId,gameFlavorId in fileinfos:
        gameFlavorId = gameFlavorId.lower()
        gamename = gamename.lower()
        category = category.lower()
        gameVersionId = gameVersionId.lower()
        match gamename:
            case 'minecraft':
                match category:
                    case 'mod':
                        tasks.append(moddownloadline(gamename,category,slug,gameVersionId,gameFlavorId,session))
                    case 'shaderpack':
                        tasks.append(moddownloadline(gamename,category,slug,gameVersionId,gameFlavorId,session))
                    case 'resourcepack':
                        tasks.append(moddownloadline(gamename,category,slug,gameVersionId,gameFlavorId,session))
                    case 'modpack':
                        tasks.append(moddownloadline(gamename,category,slug,gameVersionId,gameFlavorId,session))
                    case 'datapack':
                        tasks.append(moddownloadline(gamename,category,slug,gameVersionId,gameFlavorId,session))
                    case 'addon':
                        tasks.append(moddownloadline(gamename,category,slug,gameVersionId,gameFlavorId,session))
                    case 'world':
                        tasks.append(moddownloadline(gamename,category,slug,gameVersionId,gameFlavorId,session))
                    case 'bukkitplugin':
                        tasks.append(moddownloadline(gamename,category,slug,gameVersionId,gameFlavorId,session))
                    case 'customization':
                        tasks.append(moddownloadline(gamename,category,slug,gameVersionId,gameFlavorId,session))
                    case _:
                        pass
            case _:
                pass
    
    results = await gather(*tasks)
    await session.close()
    return results