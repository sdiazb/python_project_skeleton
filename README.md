# Python Project Skeleton

[![Build Status](https://travis-ci.org/sdiazb/python_project_skeleton.svg?branch=master)](https://travis-ci.org/sdiazb/python_project_skeleton)
[![Code Climate](https://codeclimate.com/github/sdiazb/python_project_skeleton/badges/gpa.svg)](https://codeclimate.com/github/sdiazb/python_project_skeleton)
[![Code Health](https://landscape.io/github/sdiazb/python_project_skeleton/master/landscape.svg?style=flat)](https://landscape.io/github/sdiazb/python_project_skeleton/master)
[![codecov](https://codecov.io/gh/sdiazb/python_project_skeleton/branch/master/graph/badge.svg)](https://codecov.io/gh/sdiazb/python_project_skeleton)

This repository contains a basic skeleton for python projects, so
new projects can be started quickly following best practices.

## Code Quality Standards

This project contains integration with the following tools in
order to provide code quality metrics:

- Code Climate
- Landscape
- Codecov

The skeleton is shipped with several tools with similar functionalities
so when forking, you can use your favourite one.

## CI

Config files to integrate the skeleton with CI services are also
provided. The supported CI services are:

- Travis CI

## Test

This skeleton is shipped with a dummy module. Tests for this
dummy module are also provided using unittest and mock. The
full test suite is launched with nose.

```
nosetests
```

To fully automate testing in this skeleton, tox is used. To launch
tox you can use:

```
tox
```

Or:

```
python setup.py test
```

## Packaging

To create a distribution, this skeleton is prepared to create
a wheel as follows:

```
python setup.py bdist_wheel
```

Or simply, you can create a source distribution of the skeleton
in zip format by typing:

```
python setup.py sdist --format zip
```

## Installing

To install a previously generated wheel:

```
pip install myproject.whl
```

## Acknowledgments

This skeleton uses a
[gitignore](https://github.com/github/gitignore/blob/master/Python.gitignore)
file from github repository.
Regarding changelog, it follows the
[Keep a Changelog](http://keepachangelog.com/en/0.3.0/) recommendations.

## License

This repository is released under the [MIT License](http://www.opensource.org/licenses/MIT).
