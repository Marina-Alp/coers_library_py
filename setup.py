#!/usr/bin/python3

from setuptools import setup, find_packages

setup(
    name='Библиотека книг',
    version='0.0.1',
    packages=find_packages("none"),
    scripts=["bin/NAME"], # Расположение главного исполняемого файла.????
    url='https://github.com/...', # как сделать
    license='Apache-2.0',
    author='Алпацкая Марина Федоровна',
    author_email='marzepan20@gmail.com',
    description='...', # дописать по окончанию работы
    include_package_data=True,
    install_requires=[
      # дописать если появится
      ],
)