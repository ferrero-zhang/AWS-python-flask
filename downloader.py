# -*- coding: utf-8 -*-
# coding=utf-8


import os.path
from urllib import urlretrieve
from datetime import datetime
import shutil
import ConfigParser 

config = ConfigParser .ConfigParser()
config.read('leecher.config')
zimuName = config.get('resource','name').decode('utf-8')
print zimuName
temp_dir = ".download/"
def download(url,zh_name):
    print("downloading from %s" % url)
    ext = url.split('.')[-1]
    name = datetime.now().strftime('%Y%m%d-%H%M%S%f') + zh_name + '.' + ext 
    target_location = os.path.join(temp_dir,name)
    #target_location = os.path.join(temp_dir,zimuName)
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    try:
        local_filename, headers = urlretrieve(url, target_location)
    except:
        local_filename = ''
    return os.path.basename(local_filename)

def clean():
    """
    delete all files under temp directory
    """
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)

if __name__ == '__main__':
    
    print("downloading with urllib" )
    url = 'http://tu.rrsub.com/ftp/2016/0427/6aab634bbf78e5838b29c65baea720cb.zip'  
    download(url)


