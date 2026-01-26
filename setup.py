#!/usr/bin/env python
"""Setup script for torrent-dl."""

from setuptools import setup, find_packages

# Read long description from README
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='torrent-dl',
    version='0.1.0',
    author='Animesh Kundu',
    author_email='anik.edu@gmail.com',
    description='Python library to watch and download torrents at the same time',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/animeshkundu/torrent-dl',
    license='MIT',
    packages=find_packages(exclude=['tests', 'tests.*']),
    python_requires='>=3.8',
    install_requires=[
        'altasetting>=0.1.1',
        'babelfish>=0.6.0',
        'blessings>=1.7',
        'colorama>=0.4.4',
        'guessit>=3.4.0',
        'lockfile>=0.12.2',
        'netifaces>=0.11.0',
        'Ojota>=3.1.2',
        'pyaml>=21.10.1',
        'python-daemon>=2.3.0',
        'python-dateutil>=2.8.2',
        'PyYAML>=6.0',
        'qtfaststart>=1.8',
        'rebulk>=3.1.0',
        'six>=1.16.0',
    ],
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-cov>=4.0.0',
            'pytest-mock>=3.10.0',
            'ruff>=0.1.0',
            'black>=23.0.0',
            'bandit>=1.7.0',
            'mypy>=1.0.0',
        ],
    },
    entry_points={
        'console_scripts': [
            'torrent-dl=Pyflix.__init__:main',
        ],
    },
    package_data={
        'Pyflix': [
            'torrent/*.py',
            'utils/*.py',
            'utils/settings.yaml',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Multimedia :: Video',
    ],
)
