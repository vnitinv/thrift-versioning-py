import re
import sys
import os

def get_version(file_name):
    file_name =  file_name.split(r'/')[-1]
    obj = re.search(r'(\d)(\d)(\d)',file_name)
    if obj:
        return '.'.join(obj.groups())

def add_sys_path(file_name):
    sys.path.append(os.path.join(os.getcwd(), '{0}/gen-py'.
        format(get_version(file_name))))


