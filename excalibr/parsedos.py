#!/usr/bin/python

from lxml import etree
import sys
import numpy as np
from math import *
import os

class dos:
	"""
	Object to store the data contained in the dos.xml file
	of an exciting calculation.
	Args:
		name (string): filename of the dos xml information
	.. attribute :: name
	 	associated filename

	"""
	def __init__(self, name):
		if os.path.isfile(name):
			self.setparameter(name)
		else:
			print ("\nScript needs xml file\"",name,"\"to run\n")
			sys.exit()
	def setparameter(self,name):
			self.tree = etree.parse(name)
			self.filename=name
			self.natoms=len(self.tree.xpath('/dos/partialdos'))
			xa = self.tree.xpath('/dos/totaldos/diagram[@nspin="1"]/point/@e')
			if len(self.tree.xpath('/dos/totaldos/diagram'))==2:
				self.spin=True
			else:
				self.spin=False
			self.energies = [float(xe)*27.21138 for xe in xa]
			self.nw=len(self.energies)
	def getdos(self,array):
		if not self.spin:
			pdos=np.zeros(self.nw)
			for m in array:
				mdos = [float(xe) for xe in m.xpath("./point/@dos")]
				for i in range(0,self.nw):
					pdos[i] = pdos[i] + mdos[i]
		elif self.spin:

			uppdos=np.zeros(self.nw)
			downpdos=np.zeros(self.nw)
			for m in array:
				if m.get("nspin")=='1':
					mdos = [float(xe) for xe in m.xpath("./point/@dos")]
					for i in range(0,self.nw):
						uppdos[i] = uppdos[i] + mdos[i]
				elif m.get("nspin")=='2':
					mdos = [float(xe) for xe in m.xpath("./point/@dos")]
					for i in range(0,self.nw):
						downpdos[i] = downpdos[i] + mdos[i]
			pdos=[uppdos, downpdos]
		return  pdos

	def species(self, species):
		m_array =self.tree.xpath('/dos/partialdos[@speciesrn="%s"]/diagram'%(species))
		pdos=self.getdos(m_array)
		return pdos

	def atom(self, species, atom):
		m_array =self.tree.xpath('/dos/partialdos[@speciesrn="%s"][@atom="%s"]/diagram'%(species,atom))
		pdos=self.getdos(m_array)
		return pdos

	def angular(self,l):
		m_array =self.tree.xpath('/dos/partialdos/diagram[@l="%s"]'%(l))
		pdos=self.getdos(m_array)
		return pdos

	def speciesl(self,species,l):
		m_array =self.tree.xpath('/dos/partialdos[@speciesrn="%s"]/diagram[@l="%s"]'%(species,l))
		pdos=self.getdos(m_array)
		return pdos

	def atoml(self, species,atom,l):
		m_array =self.tree.xpath('/dos/partialdos[@speciesrn="%s"][@atom="%s"]/diagram[@l="%s"]'%(species,atom,l))
		pdos=self.getdos(m_array)
		return pdos
	def interstitial(self):
		m_array =self.tree.xpath('/dos/interstitialdos/diagram')
		pdos=self.getdos(m_array)
		return pdos
	def total(self):
		m_array=self.tree.xpath('/dos/totaldos/diagram')
		pdos=self.getdos(m_array)
		return pdos
