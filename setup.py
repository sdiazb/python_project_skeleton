from setuptools import setup, find_packages

version = '0.0.0'
github_url = 'https://github.com/sdiazb/python_project_skeleton'

config = {
    'name': 'myproject',
    'description': 'My Project',
    'version': version,
    'keywords': 'python dev sdiazb',
    'author': 'Sergio Diaz Bautista',
    'author_email': 's.diazbautista@gmail.com',
    'url': github_url,
    'download_url': github_url + '/tarball/' + version,
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
