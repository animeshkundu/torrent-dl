#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='torrent-dl',
    version='0.0.1',
    author='Animesh Kundu',
    description='Python library to watch and download torrents at the same time',
    author_email='anik.edu@gmail.com',
    packages=['Pyflix'],
    scripts=[],
    url='https://github.com/animeshkundu/torrent-dl',
    license='LICENSE.txt',
    long_description=open('README.md').read(),
    install_requires=[
	'babelfish>=0.6.0',
	'blessed>=1.19.0',
	'colorama>=0.4.0',
	'docutils>=0.16',
	'guessit>=3.0.0',
	'lockfile==0.12.2',
	'netifaces==0.10.5',
	'pyaml>=21.0.0',
	'python-daemon>=2.3.0',
	'python-dateutil>=2.8.0',
	'PyYAML>=5.3.0',
	'qtfaststart==1.8',
	'rebulk>=3.0.0',
	'six>=1.15.0'
    ],
    entry_points={
        'console_scripts': ['torrent-dl = Pyflix.__init__:main']
    },
    package_data={
        'Pyflix': [ 'torrent/*.py',
                    'utils/*.py'],
    },
)
