from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='MuseBoxPy',
      version=version,
      description="Raspberry Pi Music Player",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='music raspberrypi arudino cranberry',
      author='Daniel Schwabacher',
      author_email='danielschwabacher@gmail.com',
      url='github.com/danielschwabacher/museboxpy',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points={
        'console_scripts': [
            'musebox = museboxpy.cmd:hello',
        ]
      }
)
