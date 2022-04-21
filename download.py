from tqdm import tqdm
from tqdm.tk import tqdm as tqdm_tk
import requests
import sys
import os

exec_mode = "gui"
# tqdm_tkのcallback関数内から、プログラム全体を停止させるためのフラグ
stop_program_flag = False


def download_file(url: str, save_name: str):
    # fire this callback func when tkinter window's cancel button is clicked
    def stop_program():
        global stop_program_flag
        stop_program_flag = True

    # start download file
    res = requests.get(url, stream=True)
    file_size = int(res.headers["Content-Length"])

    # show progress bar
    if exec_mode == "gui":
        progress_bar_tk = tqdm_tk(cancel_callback=stop_program,
                                  total=file_size, unit="B", unit_scale=True)
    progress_bar = tqdm(total=file_size, unit="B", unit_scale=True)

    # save file for each chunk
    with open(save_name, 'wb') as file:
        for chunk in res.iter_content(chunk_size=1024):
            if(stop_program_flag):
                break
            file.write(chunk)
            progress_bar.update(len(chunk))
            progress_bar_tk.update(len(chunk))

    if(stop_program_flag):
        os.remove(save_name)
        sys.exit()

    progress_bar.close()
    progress_bar_tk.close()

    return save_name


def main():
    url = "https://esahubble.org/media/archives/images/original/heic1901a.tif"
    save_name = "heic1901a.jpg"
    created_file = download_file(url, save_name)


if __name__ == '__main__':
    main()
