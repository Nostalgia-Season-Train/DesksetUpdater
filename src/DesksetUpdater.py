# ==== 开始更新 ====
print('begin update')


# ==== 获取 URL ====
from argparse import ArgumentParser

parser = ArgumentParser(description='数字桌搭更新器命令行参数')
parser.add_argument('-url', required=True, help='下载地址')
args = parser.parse_args()

url = args.url


# ==== 下载并解压更新包 ====
from urllib.request import urlretrieve
from zipfile import ZipFile
from os import mkdir

urlretrieve(url, 'Deskset.zip')

with ZipFile('./Deskset.zip', 'r') as file:
    mkdir('./Deskset')
    file.extractall('./Deskset')


# ==== 删除旧文件 ===
from os import remove, rename
from shutil import rmtree

rename('./Deskset.exe', './Deskset-Old')  # Deskset.exe 运行时可以改名

remove('./DesksetBack.py')
rmtree('./site-packages')
rmtree('./lib')
rmtree('./i18n')


# ==== 复制新文件 ====
from shutil import copy, copytree

copy('./Deskset/DesksetBack.py', './DesksetBack.py')
copytree('./Deskset/site-packages', './site-packages')
copytree('./Deskset/lib', './lib')
copytree('./Deskset/i18n', './i18n')

copy('./Deskset/Deskset.exe', './Deskset.exe')

# 清除解压目录、更新包
rmtree('./Deskset')
remove('./Deskset.zip')


# ==== 结束更新 ====
print('finish update')
