import urllib.request

try:
    url = "https://raw.githubusercontent.com/jules-sandbox/MIGAS/main/MIGAS.jpeg"
    urllib.request.urlretrieve(url, "img/MIGAS.jpeg")
    print("Downloaded successfully from github")
except Exception as e:
    print(f"Failed to download: {e}")
