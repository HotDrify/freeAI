from setuptools import setup, find_packages

with open("README.md", "r", encoding = "utf-8") as fh:
    README = fh.read()
   
setup(
  name = "freeAI",
  version = "1.1",
  description = "this is a python package to use the completely free chatGPT and more models.",
  long_description = README,
  url = "https://github.com/HotDrify/freeAI",
  author = "HotDrify",
  license = "Apache License 2.0",
  keywords = [
    "chatBot",
    "freeAI",
    "freeGPT",
    "freeChatGPT",
    "gptfree",
    "freeAPI",
    "python",
    "api",
  ],
  python_requires = ">=3.8",
  classifiers = [
    "Programming Language :: Python :: 3",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache License 2.0",
  ],
  packages=find_packages(),
  install_requires=[
    "requests",
    "fake-useragent",
  ]
)
