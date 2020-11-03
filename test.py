from io import BytesIO

import requests
from PIL import Image

url = 'https://imgebed.oss-cn-zhangjiakou.aliyuncs.com/img/saber.jpg'


response = requests.get(url)
image = Image.open(BytesIO(response.content))
image.show()
