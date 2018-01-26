#coding: utf-8
#author: Luke_bei

import click
import os

#telpates
from templates.init import _init_basic_code, _init_readme_code
from templates.requirement import _init_requirement_code
from templates.setup import _init_setup_code
from templates.git import _init_git_code
from templates.project import _init_main_code
from templates.bin import _init_bin_code

#operators
from operators import _mkdir_p, init_code, _mk_git

#logging
import logging
from logging import StreamHandler, DEBUG
#logger
logger = logging.getLogger(__name__)
logger.setLevel(DEBUG)
logger.addHandler(StreamHandler())

@click.command()
@click.option('--name',prompt="Project name",help='Your awesome python project name')
@click.option('--author',prompt="author", help="Author name")
@click.option('--git',prompt="Init git now?", is_flag=True)
def init_project_structure(name, author, git):
    """
        Hey, dude, let me help u make a awesome structure for python project
    """
    dst_path = os.path.join(os.getcwd(), name)
    start_init_info(dst_path)

    #create dst path
    _mkdir_p(dst_path)

    #create project tree
    os.chdir(dst_path)
    init_code("README.md", _init_readme_code)
    init_code("requirements.txt", _init_requirement_code)
    init_code(".gitignore", _init_git_code)
    init_code('setup.py', _init_setup_code)    
    #mkdir
    docs_path = os.path.join(dst_path, 'docs')
    bin_path = os.path.join(dst_path, "bin")
    project_path = os.path.join(dst_path, 'project')
    tests_path = os.path.join(project_path, 'tests')
    lib_path = os.path.join(project_path, 'lib')
    _mkdir_p(docs_path)
    _mkdir_p(bin_path)
    _mkdir_p(project_path)
    _mkdir_p(tests_path)
    _mkdir_p(lib_path)

    os.chdir(project_path)
    init_code("main.py", _init_main_code)

    os.chdir(bin_path)
    init_code("run.sh", _init_bin_code)

    #init git repository, if need
    if git:
        _mk_git(dst_path)
    
    click.secho("Done！", fg='green')

    
# logging info
def warning_path_exist(path):
    """
    send warning msg if path exist
    """
    logger.warning('''\033[31m{Warning}\033[0m
    ==> \033[32m%s\033[0m\n exist
    ==> please change the project name,
    ==> and try again !''' % path)

def start_init_info(path):
    """
    start init msg
    """
    if os.path.isdir(path):
        warning_path_exist(path)
        exit(1)
    else:
        logger.info('''\033[33m{Info}\033[0m
    ==> start init your project [on]
    ==> \033[32m%s\033[0m\n''' % path)

def main():
    init_project_structure()


if __name__ == "__main__":
    main()