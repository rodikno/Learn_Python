import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + '.jpg'
    urllib.request.urlretrieve(url, full_name)

download_web_image('http://cdn.fishki.net/upload/post/201409/06/1301804/i2dpv50ftpg.jpg')
