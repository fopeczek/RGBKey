import os
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))
PKG_NAME = 'RGBKey'
VERPATH = os.path.join(HERE, PKG_NAME, '_version.py')
exec(open(VERPATH).read())

setup(name=PKG_NAME,
      version=__version__,
      author="Mikolaj Krawczuk",
      include_package_data=True,
      install_requires=[
          "overrides",
          "click"
      ],
        entry_points='''
        [console_scripts]
        rgb_key=RGBKey.cli:main
      '''
      )