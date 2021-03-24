from setuptools import setup, find_packages
import os

def open_file(fname):
    """helper function to open a local file"""
    return open(os.path.join(os.path.dirname(__file__), fname))


setup(
    name='beaker37',
    version='0.1',
    author='Jens Krause',
    author_email='jxkrause@posteo.de',
    packages=find_packages(),
    #url='https://github.com/bonartm/moviesearch',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.8',
    ],
    description='Beaker 37 is a Python library for recommending movies',
    long_description=open_file('README.md').read(),
    # end-user dependencies for your library
    install_requires=[
        'pandas', 
        'scikit-learn', 
        'fuzzywuzzy', 
        'python-Levenshtein',
        'numpy',
        'sqlalchemy',
    ],
    # include additional data
    package_data= {
        'beaker37': ['models/*.csv', 'models/*.p']
    }
)
