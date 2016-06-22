#!/usr/bin/env python
# -*- coding: utf-8 -*-

import importlib
import sys

from takemehome.util.color_print import cprint

def main(process_name, process_args):
  cprint.p('Importing module {}...'.format(process_name))
  process_module = importlib.import_module('takemehome.processes.{}'.format(process_name))
  process_class = getattr(process_module, process_name)
  if process_class:
    try:
      process_class.main(*process_args)
    except Exception, e:
      print process_class.usage()

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print 'Usage: invocation_routine <process_name> <process_args>'
    exit()
  main(sys.argv[1], sys.argv[2:])
