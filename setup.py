from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

class Tox(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        tox.cmdline(args=args)

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
    'tests_requires': ['tox', 'nose', 'coverage'],
    'extras_require': {},
    'cmdclass': {
        'test': Tox
    },
    'packages': find_packages(exclude=['docs', 'tests*']),
    'scripts': []
}

setup(**config)
