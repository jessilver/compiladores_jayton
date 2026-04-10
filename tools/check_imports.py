#!/usr/bin/env python3
import sys, traceback, os

def try_import(name):
    try:
        __import__(name, fromlist=['*'])
        print(f"Imported {name} OK")
        return True
    except Exception:
        print(f"Failed to import {name}:")
        traceback.print_exc()
        return False

print('cwd:', os.getcwd())
print('sys.path[0]:', sys.path[0])
print('sys.path (first 6):', sys.path[:6])

try_import('antlr4')
try_import('generated.ExprLexer')
try_import('ExprLexer')
try_import('generated.ExprParser')
try_import('ExprParser')
