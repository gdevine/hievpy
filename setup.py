from setuptools import setup

setup(name='hievpy',
      version='0.1',
      description='Python helper methods for interacting with the HIEv application',
      author='gdevine',
      url='https://github.com/gdevine/hievpy',
      packages=['hievpy'],
      install_requires=[
          'requests',
          'pandas',
      ],
      )
