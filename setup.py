from os import system
from shutil import rmtree, make_archive

# 清除上次构建
rmtree('./dist', ignore_errors=True)

# nuitka 编译 DesksetUpdater.py
  # --standalone 构建产物不依赖于本地 Python 环境
  # --onefile    构建产物为可执行文件，而不是文件夹
  # --assume-yes-for-downloads 自动确认编译所需工具的下载，不用手动输入 Yes
system('nuitka --standalone --onefile --assume-yes-for-downloads ./src/DesksetUpdater.py --output-dir=./dist --remove-output')

# 打包
make_archive('./DesksetUpdater', 'zip', './dist')
