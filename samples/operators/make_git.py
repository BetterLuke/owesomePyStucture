#encoding: utf-8

import commands
import os

def _mk_git(path):
    os.chdir(path)
    try:
        ret = commands.getstatusoutput('git init .')
    except Exception as e:
        print "Cannot find git command in your environment."