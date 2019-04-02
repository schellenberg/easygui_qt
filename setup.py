#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    'pyautogui', 'pyautogui',# TODO: put package test requirements here
]

setup(
    name='cs20-easygui',
    version='0.9.5',
    description='"Inspired by EasyGUI, designed for PyQt"',
    long_description=readme + '\n\n' + history,
    author='André Roberge',
    author_email='andre.roberge@gmail.com',
    url='https://github.com/schellenberg/easygui_qt',
    packages=[
        'easygui_qt', 'easygui_qt.demos'
    ],
    package_dir={'easygui_qt':
                 'easygui_qt'},
    include_package_data=True,
    install_requires=['sip', 'PyQt5'],
    license="BSD",
    zip_safe=False,
    keywords='easygui_qt',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Education',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
