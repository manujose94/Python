#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

sys.stdout.write("run\n")

sys.stdout.write(">> ")

for line in iter(sys.stdin.readline, ""):
    if line.strip() != "":
        sys.stdout.write("from python: " + line)
    sys.stdout.write(">> ")
    
sys.stdout.write("\n")
