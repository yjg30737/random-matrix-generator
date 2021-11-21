from setuptools import setup, find_packages

setup(
    name='random-matrix-generator',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='Random small dot covered matrix generator',
    url='https://github.com/yjg30737/random-matrix-generator.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)