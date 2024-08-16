# McFileFetcher
一键下载工具，旨在自动化下载大众平台CurseForge等其他平台上公开的文件，简化游戏模组以及其他文件的管理和安装过程。通过使用该工具，用户可以高效地获取和安装所有相关的模组或者其他文件，提升整合包制作效率和游戏体验。
<br>
A one-click download tool designed to automate the process of downloading publicly available files from platforms like CurseForge and others. It simplifies the management and installation of game mods and other files. By using this tool, users can efficiently acquire and install all related mods or other files, improving the efficiency of modpack creation and enhancing the gaming experience.
## 构建方式
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
个性化的配置文件
![image](https://github.com/user-attachments/assets/0564b556-163d-4a15-a2e0-4cdb3371079b)
高并发的快速下载
![image](https://github.com/user-attachments/assets/688d5f33-e153-4748-bb1b-4117e1b1ba21)
人性化的信息存留，方便用户后续检查问题
![image](https://github.com/user-attachments/assets/bd156dab-dfa6-4ef7-90ef-fe409d302e09)
