#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

class project_config(object):
  def __init__(self, remotes, relative_path):
    self.remotes = remotes
    self.relative_path = relative_path

  @classmethod
  def load_from_project_json(cls, file_path):
    d = json.load(open(file_path, 'r'))
    if 'remotes' not in d or 'relative_path' not in d:
      raise Exception('remotes and relative_path not found in specified json configuration file.')
    return cls(d['remotes'], d['relative_path'])
