from tkinter import messagebox


def main():
    print("hello from main.py")
    messagebox.showinfo("test--auto-update-pyinstaller-exe",
                        "hello from main.py")
    pass


def checkUpdate():

    # バージョンチェック
    if common.system["version"] != str(common.information[0].system_version):

        # ダウンロード
        file_size = 50029115
        res = requests.get(self.url, stream=True)
        pbar = tqdm(total=file_size, unit="B", unit_scale=True)
        with open(self.save_name, 'wb') as file:
            for chunk in res.iter_content(chunk_size=1024):
                file.write(chunk)
                pbar.update(len(chunk))
            pbar.close()


if __name__ == "__main__":
    checkUpdate()
    main()
