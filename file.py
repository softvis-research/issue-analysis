import sys
import re

f = "jqassistant.cypher"

f=open(f,mode='r',encoding='ansi')
s=(f.read())

def convert_func(matchobj):
    m =  matchobj.group(0)

    st=re.sub(r'[^0-9_]','',m)

    return st

ret = re.sub(r'[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z',convert_func, s)   # <<< This is where the magic happens
ret = re.sub(r'[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}Z',convert_func, ret)
print(ret)

fr = open("demofile4.cypher", "w",encoding='ansi')
fr.write(ret)
fr.close()