#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
print(sys.getrefcount(1))
A = ["spam"]
B = A[:]
print("A's copy B:",B)
B[0] = "shrubbery"
print("After change B[0] B:",B)
