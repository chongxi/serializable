from distutils.core import setup
import os
# from setuptools import find_packages

def package_tree(pkgroot):
    path = os.path.dirname(__file__)
    subdirs = [os.path.relpath(i[0], path).replace(os.path.sep, '.')
               for i in os.walk(os.path.join(path, pkgroot))
               if '__init__.py' in i[2]]
    return subdirs

NAME = 'Serializable'
VERSION = '0.1.0'

setup(
    name=NAME,
    packages=package_tree('serializable'),
    version=VERSION,
    description="Utilities for handling serializable classes.",
    author='Kristian Hartikainen',
    author_email='kristian.hartikainen@gmail.com',)
