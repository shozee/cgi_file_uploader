#!/usr/bin/env python
import os
import sys
#import commands
import cgi, cgitb

upload_dir="data"

#cgitb.enable()
cgitb.enable(display=0, logdir='logdir')
form  = cgi.FieldStorage()
fileitem = form["photo"]

print("Content-Type: text/html\n\n")

if not fileitem.file: exit(0)

fpath = os.path.join(upload_dir, os.path.basename(fileitem.filename) )
fout  = open(fpath, 'wb')
while 1:
  chunk = fileitem.file.read(100000)
  if not chunk: break
  fout.write (chunk)
fout.close()
os.chmod(fpath,0o707)
