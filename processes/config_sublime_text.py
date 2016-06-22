#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import subprocess
import sys

from takemehome.util.color_print import cprint

class config_sublime_text(object):
  DEFAULT_ST_CONFIG_GIT_ADDR = 'git@github.com:lwxted/subl_config.git'
  DEFAULT_ST_CONFIG_LOCAL_PATH = os.path.join(os.environ['HOME'], 'Library/Application Support/Sublime Text 3')

  @staticmethod
  def main(git_addr=None, local_path=None):
    cprint.p('Cloning Sublime Text 3 config from git repo...')
    git_addr = git_addr if git_addr is not None else config_sublime_text.DEFAULT_ST_CONFIG_GIT_ADDR
    local_path = local_path if local_path is not None else config_sublime_text.DEFAULT_ST_CONFIG_LOCAL_PATH
    if os.path.isdir(os.path.join(local_path, '.git')):
      os.chdir(local_path)
      if subprocess.check_output(['git', 'status', '--porcelain']):
        cprint.warn('Your Sublime Text config repo may have uncommitted changes.')
        s = raw_input('Do you wish to discard your current repo? [y/n] ')
        if s != 'y' and s != 'Y':
          return

    os.chdir(os.environ['HOME'])
    cprint.p('Killing all current Sublime Text instances...')
    subprocess.call(['killall', 'Sublime Text'])
    shutil.rmtree(local_path)
    cprint.status(subprocess.call(['git', 'clone', '--recursive', git_addr, local_path]))

    @staticmethod
    def usage():
      return """Usage: config_sublime_text.py <git_addr> <local_path>
Default git_addr: git@github.com:lwxted/subl_config.git
Default local_path: ~/Library/Application Support/Sublime Text 3"""
