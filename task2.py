# -*- coding: utf-8 -*-
"""Task2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eTNwIlIOpHREAM-kquADQ1f_rOHs8Fzl
"""

import requests

# Fetch the posts from jsonplaceholder.typicode.com
response = requests.get('https://jsonplaceholder.typicode.com/posts')

# Print the last 15 posts
for post in response.json()[-15:]:
    print(post)