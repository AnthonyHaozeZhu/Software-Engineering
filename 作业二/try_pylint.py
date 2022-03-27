# -*- coding: UTF-8 -*-
"""
@Project ：作业二 
@File ：try_pylint.py
@Author ：AnthonyZ
@Date ：2022/3/14 16:05
"""
import pylint.lint


pylint_opts = ['--rcfile=PylintConfig.conf', '-ry', './MaxSet.py']

pylint.lint.Run(pylint_opts)