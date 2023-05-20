import os


location = lambda x: os.path.join(os.path.dirname(os.path.realpath(__file__)), x)

print(location('static/'))