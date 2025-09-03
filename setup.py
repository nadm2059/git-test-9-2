from setuptools import setup

setup(
    name="hello-pkg-demo",        # package name
    version="0.1.0",              # version
    py_modules=["app"],          # your python file (hello.py)
    install_requires=[],           # dependencies if any
    author="Your Name",
    description="A simple Python program that prints Hello -- version 1!",
    license = "MIT",
)
