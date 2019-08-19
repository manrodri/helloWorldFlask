from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='hello, world!',
    version='0.1.0',
    description='a hello world app in Flask',
    long_description=readme,
    author='Manuel Rodriguez',
    author_email='manuel@example.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[]
)

