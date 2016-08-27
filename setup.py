from setuptools import setup, find_packages

version = '0.0.0'

config = {
    'name': 'myproject',
    'description': 'My Project',
    'version': version,
    'keywords': 'python dev sdiazb',
    'author': 'Sergio Diaz Bautista',
    'author_email': 's.diazbautista@gmail.com',
    'url': 'https://github.com/sdiazb/python_project_skeleton',
    'download_url': 'https://github.com/sdiazb/python_project_skeleton/tarball/' + version,
    'license': 'MIT',
    'classifiers': [
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    'install_requires': [],
    'extras_require': {
        'test': ['nose', 'coverage']
    },
    'packages': find_packages(exclude=['docs', 'tests*']),
    'scripts': []
}

setup(**config)
