#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import cgi, cgitb

upload_dir = "data"
cgitb.enable(display=0, logdir='logdir')
form = cgi.FieldStorage()

files2del  = form.getlist('files2del')
if len(files2del)>0 :
  for item in files2del:
    os.remove( os.path.join(upload_dir, os.path.basename(item) ) )

print("Content-Type: text/html")
print()

print('''
<html>
<head>
  <title>uploaded files</title>
</head>
<body>
<p>
''')

print('<form action="list.cgi" method="post">')
print('<table>')

for fname in os.listdir(upload_dir):
  print('<tr><td><input type="checkbox" name="files2del" value="%s" /></td><td><a href="%s">%s</a></td></tr>'%(fname,upload_dir+'/'+fname,fname) )

print('</table><input type="submit" value="delete"/></form>')
if len(files2del)>0 :
  print('just deleted :<br />')
  print('<br />'.join(files2del))

print('''
</p>
</body>
</html>
''')
