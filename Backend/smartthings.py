#!/usr/bin/python3
import json
import cgi
print("Content-type: text/plain\n")
# dynamic body
print("een python CGI script")
# done
fs=(cgi.FieldStorage())
data={'cpu_temp':fs.getvalue('cpu_temp'), 'gpu_temp':fs.getvalue('gpu_temp')}
with open('data.json', 'w') as f:
    json.dump(data, f)
