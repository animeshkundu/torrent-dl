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
	'altasetting==0.1.1',
	'babelfish==0.5.5',
	'blessings==1.6',
	'colorama==0.3.7',
	'docutils==0.12',
	'guessit==2.1.0',
	'lockfile==0.12.2',
	'netifaces==0.10.5',
	'Ojota==3.1.2',
	'pyaml==16.9.0',
	'python-daemon==2.1.1',
	'python-dateutil==2.5.3',
	'PyYAML==3.12',
	'qtfaststart==1.8',
	'rebulk==0.7.6',
	'six==1.10.0'
    ],
    entry_points={
        'console_scripts': ['torrent-dl = Pyflix.__init__:main']
    },
    package_data={
        'Pyflix': [ 'torrent/*.py',
                    'utils/*.py'],
    },
)
