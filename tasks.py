import os

from invoke import task


@task
def setup(c):  # 初回git clone直後に実行で、開発環境構築
    cmd1 = "python -m venv ."
    cmd2 = "pip install -r requirements.txt"
    cmd = f"{cmd1} && {cmd2}"
    result = c.run(cmd)


@task
def install(c):
    cmd = "pip install -r requirements.txt"
    result = c.run(cmd)


@task
def build(c):
    exeName = 'test--auto-update-pyinstaller-exe'
    if os.name == 'nt':
        print('build task on Windows')
    else:
        print('build task on Mac or Linux or on unexpected os')
        print('pyinstallerはwindows環境下でしかexeファイル化できません!')
        exit()
    cmd = f"pyinstaller main.py --onefile --noconsole --name {exeName} --version-file version.txt"
    result = c.run(cmd)
