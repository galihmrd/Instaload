import requests
import secrets

def download_post_from_link(url):
    api = f"https://galihmrd.my.id/api?url={url}"
    req = requests.get(api).json()
    download_url = req.get("data")["url"]
    if len(download_url) > 1:
        for dl_url in download_url:
            random_hash = str(secrets.token_hex(nbytes=16))
            get_content = requests.get(dl_url)
            mime = get_content.headers.get("Content-Type")
            ext = mime.split("/")[0]
            with open(f"/sdcard/TikMedia/{random_hash}.{ext}", "wb") as file:
                file.write(get_content.content)
    else:
        random_hash = str(secrets.token_hex(nbytes=16))
        get_content = requests.get(download_url[0])
        mime = get_content.headers.get("Content-Type")
        ext = mime.split("/")[0]
        with open(f"/sdcard/TikMedia/{random_hash}.{ext}", "wb") as file:
            file.write(get_content.content)
