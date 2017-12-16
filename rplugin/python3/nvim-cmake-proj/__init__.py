# -*- coding: utf-8 -*-

import neovim
import os

from subprocess import  Popen, PIPE

@neovim.plugin
class NvimCMakeProj(object):

    BUILD_DIR = 'vim-cmake-build'
    CMAKE_CMD = 'cmake ..'
    MAKE_CMD = 'make'

    def __init__(self, nvim):
        self.nvim = nvim

    def echo(self, msg):
        self.nvim.command("echo '" + msg + "'")

    def _is_cmake_project(self):
        cur_dir = os.path.abspath(".")
        return os.path.exists(os.path.join(cur_dir, 'CMakeLists.txt'))

    def _has_build_dir(self):
        cur_dir = os.path.abspath(".")
        return os.path.exists(os.path.join(cur_dir, self.BUILD_DIR))

    def _run_cmake(self):
        os.chdir('vim-cmake-build')
        with Popen(self.CMAKE_CMD, stdout=PIPE, shell=True) as proc:
            ret = proc.stdout.read()
            self.echo(ret.decode('utf-8'))
        os.chdir('..')

    @neovim.command('CMakeReload')
    def cmake_reload(self):
        if self._is_cmake_project():
            if not self._has_build_dir():
                os.mkdir(self.BUILD_DIR)
            self._run_cmake()
            return True
        else:
            self.echo('CMakeLists.txt is not exists.')
            return False


    @neovim.command('CMakeBuild')
    def cmake_build(self):
        if self.cmake_reload():
            os.chdir('vim-cmake-build')
            with Popen(self.MAKE_CMD, stdout=PIPE, shell=True) as proc:
                ret = proc.stdout.read()
                self.echo(ret.decode('utf-8'))
            os.chdir('..')

