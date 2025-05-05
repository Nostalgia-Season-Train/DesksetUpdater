# ==== 下载 ====
def download(url):
    # 下载更新包
    from urllib.request import urlretrieve

    def progress_hook(block_num, block_size, total_size):
        percent = (block_num * block_size) / total_size * 100
        print(f'{percent:.1f}', flush=True)

    urlretrieve(url, 'Deskset.zip', progress_hook)


# ==== 安装 ====
def Install(zipfile_name: str) -> None:
    # 解压更新包
    from zipfile import ZipFile
    from os import mkdir

    with ZipFile(f'./{zipfile_name}', 'r') as file:
        mkdir('./Deskset')
        file.extractall('./Deskset')

    # 新版替换旧版文件、文件夹
    from pathlib import Path
    from os import remove, rename
    from shutil import rmtree

    # 清理上次更新残留文件
    if Path('./Deskset-Old').is_file():
        remove('./Deskset-Old')

    rename('./Deskset.exe', './Deskset-Old')  # Deskset.exe 运行时可以改名

    # 删除旧文件
    if Path('./DesksetBack.py').is_file():
        remove('./DesksetBack.py')
    rmtree('./site-packages', ignore_errors=True)
    rmtree('./lib', ignore_errors=True)
    rmtree('./i18n', ignore_errors=True)

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
parser.add_argument('-file', required=True, help='更新包名称')
args = parser.parse_args()

file = args.file


# ==== 主函数 ====
if __name__ == '__main__':
    print('Begin Install', flush=True)
    Install(file)
    print('Finish Install', flush=True)
