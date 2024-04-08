# Join a base URL with another URL in Python

from urllib.parse import urljoin

base_url = 'https://bobbyhadz.com'

path = 'images/static/cat.jpg'

# ✅ Join a base URL with another URL

result = urljoin(base_url, path)

# 👇️ https://bobbyhadz.com/images/static/cat.jpg
print(result)

# ---------------------------------------

# ✅ Join URL path components when constructing a URL

# 👇️ /global/images/static/dog.png
print(urljoin('/global/images/', 'static/dog.png'))