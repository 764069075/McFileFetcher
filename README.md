<div align="center">
  <img src="https://github.com/user-attachments/assets/8a140455-828d-4898-bdbf-787f22865070" alt="McFileFetcher Logo" width="66%" style="border-radius: 32px">
  <h1>McFileFetcher</h1>
  <p>
    <strong>
      一个快速的CurseForge爬虫工具
    </strong>
  </p>
</div>
<p align="center">
  <a href="https://github.com/vicuna-main/McFileFetcher"><img src="https://img.shields.io/github/stars/vicuna-main/McFileFetcher?style=flat-square" alt="Star" style="border-radius: 4px"></a>
  <a href="https://github.com/vicuna-main/McFileFetcher/blob/main/LICENSE"><img src="https://img.shields.io/github/license/vicuna-main/McFileFetcher?style=flat-square" alt="License" style="border-radius: 4px"></a>
  <a href="https://github.com/vicuna-main/McFileFetcher/releases"><img src="https://img.shields.io/github/downloads/vicuna-main/McFileFetcher/total?style=flat-square" alt="Downloads" style="border-radius: 4px"></a>
  <a href="https://github.com/vicuna-main/McFileFetcher/releases"><img src="https://img.shields.io/github/v/release/vicuna-main/McFileFetcher?style=flat-square" alt="Version" style="border-radius: 4px"></a>
  <a href="https://github.com/vicuna-main/McFileFetcher/actions"><img src="https://img.shields.io/github/actions/workflow/status/vicuna-main/McFileFetcher/build.yml?style=flat-square" alt="Version" style="border-radius: 4px"></a>
</p>
<h3 align="center">
  <a href="https://github.com/vicuna-main/McFileFetcher/wiki/tutorial">Tutorial</a>
  <span> · </span>
  <a href="https://github.com/vicuna-main/McFileFetcher/releases">Download</a>
</h3>

跨平台的，一键爬虫下载工具，旨在自动化下载CurseForge等其他平台上公开的文件，简化游戏模组以及其他文件的管理和安装过程。通过使用该工具，用户可以高效地获取和安装所有相关的模组或者其他文件，提升整合包制作效率和游戏体验。
<br>
A one-click download tool designed to automate the process of downloading publicly available files from platforms like CurseForge and others. It simplifies the management and installation of game mods and other files. By using this tool, users can efficiently acquire and install all related mods or other files, improving the efficiency of modpack creation and enhancing the gaming experience.
<br>
## Star History
<div align="center">
  <img src="https://api.star-history.com/svg?repos=vicuna-main/McFileFetcher&type=Date" alt="McFileFetcher Logo" width="100%" style="border-radius: 32px">
</div>

## 前排提示(Tips)
由于CourseForge内置网络防火墙，并且限定非美国地区的ip请求，**本程序的所有功能仅支持在美国网络下下载**，没有的盆友不用担心，可以使用下方的服务商切换到美国ip地区下载：<br>
[👓NCloud 10元/月👓](https://xn--clouds-o43k.com/#/register?code=vZePW99Y "")
- 使用上方的邀请码链接注册，随机获取返券奖励
- 同时支持Clash/Surge/Shadowrocket/Surfboard/Quantumult X
- 全网超低价，支持UDP转发
- 1TB/月流量
## 下载方式(Download)
- [github下载](https://github.com/vicuna-main/McFileFetcher/releases "下载最新版本")
- [123网盘](https://www.123pan.com/s/MQX9-gn2pd "免登录高速下载所有版本")
## 详细使用教程(Wiki)
- [github](https://github.com/vicuna-main/McFileFetcher/wiki/tutorial)
- [csdn](https://blog.csdn.net/qq_34199015/article/details/142314093)
- [zhihu](https://zhuanlan.zhihu.com/p/720532445)
- [bilibili](https://www.bilibili.com/opus/978058564062937125)
## 构建方式(Building)
### 0.安装 环境 Env
首先，在本地安装uv包管理库：<br>
`pip install uv`<br>
随后，克隆本仓库：<br>
`git clone https://github.com/vicuna-main/McFileFetcher.git`<br>
然后，运行uv安装依赖库：<br>
`uv sync`<br>
最后，激活虚拟环境（Windows）：<br>
`./.venv/Script/activate`<br>
其他平台激活方式：<br>
`source .venv/bin/activate`<br>
### 1.安装 PyInstaller
首先，你需要安装 PyInstaller。你可以通过 pip 安装它：<br>
`pip install pyinstaller`
### 2.准备你的 Python 脚本
确保你的 Python 脚本（例如 your_script.py）在一个独立的文件夹中，并且所有依赖项和资源文件都已正确设置。
### 3.使用 PyInstaller 打包
在命令行中导航到你的 Python 脚本所在的目录，然后运行 PyInstaller 命令。以下是将脚本打包成单个可执行文件的基本命令：<br>
`pyinstaller --onefile your_script.py`
#### 解释参数：
`--onefile`：将所有内容打包成一个单独的可执行文件。<br>
`your_script.py`：你的 Python 脚本文件名。
## 软件截图
美化的彩色输出，丰富的文本提示
![image](https://github.com/user-attachments/assets/fc115170-e22e-413b-a96d-b880b301bb94)
高并发的毫秒级下载
![image](https://github.com/user-attachments/assets/688d5f33-e153-4748-bb1b-4117e1b1ba21)
丰富的个性化配置文件
![image](https://github.com/user-attachments/assets/86c94591-39af-4942-b45a-1ef4c060046e)
![image](https://github.com/user-attachments/assets/d0f86020-726f-4fad-bfd1-622f0cf48c43)
人性化的信息存留，方便用户后续检查问题
![image](https://github.com/user-attachments/assets/bd156dab-dfa6-4ef7-90ef-fe409d302e09)
