#!/usr/bin/env python
# -*- coding: utf-8 -*-

from colorama import init, Back, Fore, Style
init()

class cprint(object):

  @staticmethod
  def ok(s):
    print '{} OK {} {}'.format(
      Fore.WHITE + Back.GREEN + Style.BRIGHT,
      Style.RESET_ALL,
      s)

  @staticmethod
  def warn(s):
    print '{} WARN {} {}'.format(
      Fore.WHITE + Back.YELLOW + Style.BRIGHT,
      Style.RESET_ALL,
      s)

  @staticmethod
  def fail(s):
    print '{} FAIL {} {}'.format(
      Fore.WHITE + Back.RED + Style.BRIGHT,
      Style.RESET_ALL,
      s)

  @staticmethod
  def p(s):
    print s

  @staticmethod
  def status(sc):
    if sc == 0:
      cprint.ok('')
    else:
      cprint.fail('')
