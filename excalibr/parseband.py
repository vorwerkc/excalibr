#!/usr/bin/python

from lxml import etree
import sys
import numpy as np
from math import *
import os

class bandstr:
	"""
	Object to store the data contained in the bandstructure.xml file
	of an exciting calculation.
	Args:
		name (string): filename of the bandstructure xml information
	.. attribute :: name
	 	associated filename
	"""
	def __init__(self,name):
		if os.path.isfile(name):
			self.setparameter(name)
		else:
			print("\nScript needs xml file\"",name,"\"to run\n")
			sys.exit()
	def setparameter(self,name):
		self.tree = etree.parse(name)
		self.filename=name
		self.pts = self.tree.xpath('/bandstructure/band[1]/point/@distance')
		self.bands =len(self.tree.xpath('/bandstructure/band'))

	def getband(self, bandnr):
		y = [float(xe)*27.211 for xe in self.tree.xpath("/bandstructure/band[%i]/point/@eval"%(bandnr))]
		return self.pts, y

	def getbands(self, bandmin, bandmax):
		y=[]
		for i in range(bandmin,bandmax):
			if (i==bandmin):
				x=self.getband(i)[0]
			y.append(self.getband(i)[1])
		windowlow=min(y[0])
		windowhigh=max(y[-1])

		return x,y, windowlow, windowhigh

	def getlabels(self):
		nrlabel=len(self.tree.xpath('/bandstructure/vertex'))
		x=[]
		y=[]
		for i in range(0,nrlabel):
			x.append(float(self.tree.xpath('/bandstructure/vertex[%i]/@distance'%(i+1))[0]))
			y.append(str(self.tree.xpath('/bandstructure/vertex[%i]/@label'%(i+1))[0]))
			if (y[i]=='GAMMA'): y[i]='$\Gamma$'
		return x,y
