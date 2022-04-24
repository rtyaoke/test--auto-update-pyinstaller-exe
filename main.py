from tkinter import messagebox

import download


def main():
    print("hello from main.py")
    messagebox.showinfo("test--auto-update-pyinstaller-exe",
                        "hello from main.py")
    pass


def checkUpdate():

    # バージョンチェック
    # if common.system["version"] != str(common.information[0].system_version):

    url = "https://github.com/rtyaoke/test--auto-update-pyinstaller-exe/releases/download/v_2022-04-21_13-57/test--auto-update-pyinstaller-exe.exe"
    save_name = "run.exe"
    # url = "https://www.rysys.co.jp/dpex/download/exifr_350.zip"
    # save_name = "exifr_350.zip"
    created_file = download.download_file(url, save_name)
    print(created_file)


if __name__ == "__main__":
    checkUpdate()
    main()
