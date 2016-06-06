#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import subprocess

from color_print import cprint

class proc_st(object):
  ST_CONFIG_GIT_ADDR = 'git@github.com:lwxted/subl_config.git'

  @staticmethod
  def main():
    cprint.p('Cloning Sublime Text 3 config from git repo...')
    sublime_repo_addr = os.path.join(
      os.environ['HOME'],
      'Library/Application Support/Sublime Text 3')
    if os.path.isdir(os.path.join(sublime_repo_addr, '.git')):
      os.chdir(sublime_repo_addr)
      if subprocess.check_output(['git', 'status', '--porcelain']):
        cprint.warn('Your Sublime Text config repo may have uncommitted changes.')
        s = raw_input('Do you wish to discard your current repo? [y/n] ')
        if s != 'y' and s != 'Y':
          return

    os.chdir(os.environ['HOME'])
    cprint.p('Killing all current Sublime Text instances...')
    subprocess.call(['killall', 'Sublime Text'])
    shutil.rmtree(sublime_repo_addr)
    cprint.status(subprocess.call(['git', 'clone', '--recursive', \
      proc_st.ST_CONFIG_GIT_ADDR, sublime_repo_addr]))

if __name__ == '__main__':
  proc_st.main()
