#!/usr/bin/python3

from setuptools import setup, find_packages

setup(
    name='Библиотека книг',
    version='1.0.2',
    packages=find_packages("none"),
    scripts=["bin/coers_library_add.py"],
    url='https://github.com/Marina-Alp/coers_library_py',
    license='Apache-2.0',
    author='Алпацкая Марина Федоровна',
    author_email='marzepan20@gmail.com',
    description='Пакет с инструментами для работы с книгами , библиотеками и читательскими списками',
    include_package_data=True,
    install_requires=[],
)