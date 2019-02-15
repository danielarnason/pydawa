from setuptools import setup, find_packages

setup(
    name='pydawa',
    version='0.3.0',
    packages=find_packages(),
    license='MIT',
    description='API wrapper til DAWA',
    long_description=open('README.md').read(),
    install_requires=['requests'],
    url='http://github.com/danielarnason/pydawa',
    author='Daníel Örn Árnason',
    author_email='danielarnason85@gmail.com'
)