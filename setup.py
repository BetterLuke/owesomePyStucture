from setuptools import setup, find_packages

setup(
    name="coolproject",
    version="0.1",
    description="Create a element project stucture",
    anthor="luke",
    author_email="luke.bei.2015@gmail.com",
    packages=['samples'],
    install_requires=[
        'click',
    ],
    zip_safe=False)