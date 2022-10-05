# 11723 - 집합

import sys


N = int(sys.stdin.readline())

s = []


def add(val):
    global s
    if val not in s:
        s.append(val)
    
def remove(val):
    global s
    if val in s:
        s.remove(val)
    
def check(val):
    global s
    if val in s:
        print(1)
    else:
        print(0)
        
def toggle(val):
    global s
    if val not in s:
        s.append(val)
    else:
        s.remove(val)
        
def all():
    global s
    s = [i+1 for i in range(20)]
    
def empty():
    global s
    s = []

count = 0
while count < N:
    sentence = sys.stdin.readline().strip()
    count += 1
    if sentence == 'all':
        all()
        continue
    elif sentence == 'empty':
        empty()
        continue
    
    fun, val = sentence.split()
    val = int(val)
    
    if fun == 'add':
        add(val)
    elif fun == 'remove':
        remove(val)
    elif fun == 'check':
        check(val)
    elif fun == 'toggle':
        toggle(val)

