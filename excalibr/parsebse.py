#!/usr/bin/python

from lxml import etree
import sys
import numpy as np
from math import *
import os

class exciton_contr:

    def __init__(self, name):
        if os.path.isfile(name):
            self.file=name
        else:
            print("\nScript requires file", name,"!")
            sys.exit()
    @staticmethod
    def read_bands(file):
        with open(file,'r') as f:
            # total output arrays to use with scatter plot
            x=[]
            y=[]
            z=[]
            for line in f:
                line=line.strip()
                if len(line) != 0:
                    x.append(float(line.split()[0]))
                    y.append(float(line.split()[1]))
                    z.append(float(line.split()[2]))
        return x,y,z
