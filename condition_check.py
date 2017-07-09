#!/usr/local/bin/python3

import os.path

def check():
    '''
    执行 show_arena.py 前, 先检查所需要的各个文件是否存在
    '''
    files = ['arena.html', 'template.html', 'css/stylesheet.css', 'show_arena.py']
    for file in files:
        if not os.path.exists(file):
            return False
    return True


if check():
    print("OK")
else:
    print("Sorry, some check failed...")
