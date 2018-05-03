from codecs import open
from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    readme = f.read()

setup(
    name='jameshash',
    version='0.1.0',
    description='bad hashing thing',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/jmsv/jameshash',
    author='James Vickery',
    author_email='dev@jamesvickery.net',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='hashing function password salt hash',
    packages=['jameshash'],
    project_urls={
        'Source': 'https://github.com/jmsv/jameshash',
        'Bug Reports': 'https://github.com/jmsv/jameshash/issues',
    },
)
