#!/usr/bin/env python
import sys
from distutils.core import setup, Extension
import commands
import re
import os

if sys.version_info < (2, 3):
  raise Error, "Python 2.3 or later is required"

include_dirs = []
library_dirs = ['/usr/local/lib']

if sys.platform == 'linux2':
  os.environ['PATH'] += ":/usr/local/bin:$home/bin:.:..:../.."

  tcinc = commands.getoutput('tcucodec conf -i 2>/dev/null')
  m = re.search(r'-I([/\w]+)', tcinc)
  if m:
    for path in m.groups():
      include_dirs.append(path)
    include_dirs = sorted(set(include_dirs), key=include_dirs.index)

  tclib = commands.getoutput('tcucodec conf -l 2>/dev/null')
  m = re.search(r'-L([/\w]+)', tclib)
  if m:
    for path in m.groups():
      library_dirs.append(path)
    library_dirs = sorted(set(library_dirs), key=library_dirs.index)

if sys.platform == 'darwin':
  # darwin ports
  include_dirs.append('/opt/local/include')
  library_dirs.append('/opt/local/lib')
  # fink
  include_dirs.append('/sw/include')
  library_dirs.append('/sw/lib')

ext = Extension('pytc',
                libraries = ['tokyocabinet'],
                sources = ['pytc.c'],
                include_dirs = include_dirs,
                library_dirs = library_dirs,
               )

setup(name = 'pytc',
      version = '0.8',
      description = 'Tokyo Cabinet Python bindings',
      long_description = '''
        Tokyo Cabinet Python bindings
      ''',
      license='BSD',
      author = 'Tasuku SUENAGA',
      author_email = 'gunyarakun@sourceforge.jp',
      ext_modules = [ext]
     )
