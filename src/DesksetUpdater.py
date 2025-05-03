# ==== 下载 ====
def download(url):
    # 下载更新包
    from urllib.request import urlretrieve

    def progress_hook(block_num, block_size, total_size):
        percent = (block_num * block_size) / total_size * 100
        print(f'{percent:.1f}', flush=True)

    urlretrieve(url, 'Deskset.zip', progress_hook)


# ==== 安装 ====
def Install():
    # 解压更新包
    from zipfile import ZipFile
    from os import mkdir

    with ZipFile('./Deskset.zip', 'r') as file:
        mkdir('./Deskset')
        file.extractall('./Deskset')

    # 删除旧文件
    from pathlib import Path
    from os import remove, rename
    from shutil import rmtree

    # 检查上次更新残留文件
    if Path('./Deskset-Old').is_file():
        remove('./Deskset-Old')

    rename('./Deskset.exe', './Deskset-Old')  # Deskset.exe 运行时可以改名

    remove('./DesksetBack.py')
    rmtree('./site-packages')
    rmtree('./lib')
    rmtree('./i18n')

    # 复制新文件
    from shutil import copy, copytree

    copy('./Deskset/DesksetBack.py', './DesksetBack.py')
    copytree('./Deskset/site-packages', './site-packages')
    copytree('./Deskset/lib', './lib')
    copytree('./Deskset/i18n', './i18n')

    copy('./Deskset/Deskset.exe', './Deskset.exe')

    # 清除解压目录、更新包
    rmtree('./Deskset')
    remove('./Deskset.zip')


# ==== 获取参数 ====
from argparse import ArgumentParser

parser = ArgumentParser(description='数字桌搭更新器命令行参数')
parser.add_argument('-url', required=True, help='下载地址')
args = parser.parse_args()

url = args.url


# ==== 主函数 ====
if __name__ == '__main__':
    print('begin update', flush=True)
    print('Phase 1: Download', flush=True)
    download(url)
    print('Phase 2: Install', flush=True)
    Install()
    print('finish update', flush=True)
