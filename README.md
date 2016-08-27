# Python Project Skeleton

This repository contains a basic skeleton for python projects, so
new projects can be started quickly following best practices.

## Code Quality Standards
This project contains integration with the following tools in
order to provide code quality metrics:
- Code Climate

## Test

This skeleton is shipped with a dummy module. Tests for this
dummy module are also provided using unittest and mock. The 
full test suite is launched with nose:
```
nosetests
```

## Packaging

To create a distribution, this skeleton is prepared to create
a wheel as follows:
```
python setup.py bdist_wheel
```

## Installing

To install a previously generated wheel:
```
pip install myproject.whl
```

## Acknowledgments

This skeleton uses a [gitignore](https://github.com/github/gitignore/blob/master/Python.gitignore) 
file from github repository.
In terms of changelog, this skeleton follows the [Keep a Changelog](http://keepachangelog.com/en/0.3.0/) recommendations.

## License

This repository is released under the [MIT License](http://www.opensource.org/licenses/MIT).
