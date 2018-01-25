#encoding: utf-8

import commands
import os

def _mk_git(path):
    os.chdir(path)
    ret = commands.getstatusoutput('git init .')
    print ret[-1]