#!/usr/bin/python

from lxml import etree
import sys
import numpy as np
from math import *
import os
import matplotlib.pyplot as plt

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
            self._setparameter(name)
        else:
            print ("\nScript needs xml file\"",name,"\"to run\n")
            sys.exit()
    def _setparameter(self,name):
        self.tree = etree.parse(name)
        self.filename=name
        self.natoms=len(self.tree.xpath('/dos/partialdos'))
        xa = self.tree.xpath('/dos/totaldos/diagram[@nspin="1"]/point/@e')
        if len(self.tree.xpath('/dos/totaldos/diagram'))==2:
            self.spin=True
        else:
            self.spin=False
        self.energies = np.array([float(xe)*27.21138 for xe in xa]).astype(np.float)
        self.nw=len(self.energies)
    def _getdos(self,array):
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
        return  np.array(pdos).astype(np.float)

    def species(self, species):
        """
            Function to obtain the DOS projected onto a specific species
            Args:
                int:: species
                    species number onto which to project. The speciesnumber is defined
                    in the input.xml. Note that speciesnumber=1 for the first species.
            Returns:
                list :: list with DOS value in $Ha^{-1}\Omega^{-1}$, where $\Omega$ is
                    the volume of the unit cell. The list has length len(dos.energies)
        """
        m_array =self.tree.xpath('/dos/partialdos[@speciesrn="%s"]/diagram'%(species))
        pdos=self._getdos(m_array)
        return np.array(pdos).astype(np.float)

    def atom(self, species, atom):
        """
            Function to obtain the DOS projected onto a specific atom
            Args:
                int:: species
                    species number onto which to project. The number for each species
                    can be found in INFO.OUT. Note that speciesnumber=1 for the first
                    species.
                int :: atom
                    atom number onto which to project. The number can be found in INFO.OUT.
            Returns:
                list :: list with DOS value in $Ha^{-1}\Omega^{-1}$, where $\Omega$ is
                    the volume of the unit cell. The list has length len(dos.energies)
        """
        m_array =self.tree.xpath('/dos/partialdos[@speciesrn="%s"][@atom="%s"]/diagram'%(species,atom))
        pdos=self._getdos(m_array)
        return np.array(pdos).astype(np.float)

    def angular(self,l):
        """
            Function to obtain the DOS projected onto a specific l-channel
            Args:
                int:: l
                l-channel of the projection
            Returns:
                list :: list with DOS value in $Ha^{-1}\Omega^{-1}$, where $\Omega$ is
                    the volume of the unit cell. The list has length len(dos.energies)
        """

        m_array =self.tree.xpath('/dos/partialdos/diagram[@l="%s"]'%(l))
        pdos=self._getdos(m_array)
        return np.array(pdos).astype(np.float)

    def speciesl(self,species,l):
        """
            Function to obtain the DOS projected onto a specific species and l-channel
            Args:
                int:: species
                    species number onto which to project. The number for each species
                    can be found in INFO.OUT. Note that speciesnumber=1 for the first
                    species.
                int :: l
                    l-channel of the projection
            Returns:
                list :: list with DOS value in $Ha^{-1}\Omega^{-1}$, where $\Omega$ is
                    the volume of the unit cell. The list has length len(dos.energies)
        """

        m_array =self.tree.xpath('/dos/partialdos[@speciesrn="%s"]/diagram[@l="%s"]'%(species,l))
        pdos=self._getdos(m_array)
        return np.array(pdos).astype(np.float)

    def atoml(self, species,atom,l):
        """
            Function to obtain the DOS projected onto a specific atom and l-channel
            Args:
                int:: species
                    species number onto which to project. The number for each species
                    can be found in INFO.OUT. Note that speciesnumber=1 for the first
                    species.
                int :: atom
                    atom number onto which to project. The number can be found in INFO.OUT.
                int :: l
                    l-channel of the projection
            Returns:
                list :: list with DOS value in $Ha^{-1}\Omega^{-1}$, where $\Omega$ is
                    the volume of the unit cell. The list has length len(dos.energies)
        """

        m_array =self.tree.xpath('/dos/partialdos[@speciesrn="%s"][@atom="%s"]/diagram[@l="%s"]'%(species,atom,l))
        pdos=self._getdos(m_array)
        return np.array(pdos).astype(np.float)

    def specieslm(self,species,l,m):
        """
            Function to obtain the DOS projected onto a specific species and  lm-channel
            Args:
                int:: species
                    species number onto which to project. The number for each species
                    can be found in INFO.OUT. Note that speciesnumber=1 for the first
                    species.
                int :: l
                    l-channel of the projection
                int :: m
                    m-channel of the projection
            Returns:
                list :: list with DOS value in $Ha^{-1}\Omega^{-1}$, where $\Omega$ is
                    the volume of the unit cell. The list has length len(dos.energies)
        """

        m_array =self.tree.xpath('/dos/partialdos[@speciesrn="%s"]/diagram[@l="%s"][@m="%s"]'%(species,l,m))
        pdos=self._getdos(m_array)
        return np.array(pdos).astype(np.float)

    def interstitial(self):
        """
            Function to obtain the DOS projected onto the interstitial states
            Returns:
                list :: list with DOS value in $Ha^{-1}\Omega^{-1}$, where $\Omega$ is
                    the volume of the unit cell. The list has length len(dos.energies)
        """

        m_array =self.tree.xpath('/dos/interstitialdos/diagram')
        pdos=self._getdos(m_array)
        return np.array(pdos).astype(np.float)
    def total(self):
        """
            Function to obtain total DOS
            Returns:
                list :: list with DOS value in $Ha^{-1}\Omega^{-1}$, where $\Omega$ is
                    the volume of the unit cell. The list has length len(dos.energies)
        """

        m_array=self.tree.xpath('/dos/totaldos/diagram')
        pdos=self._getdos(m_array)
        return np.array(pdos).astype(np.float)

    """ plot functions """

    def plot_total(self, **kwargs):
        """
            Returns matplotlib.pyplot.plot object with total dos as y data.
            Args(optional):
                float :: offset
        """
        offset = kwargs.pop("offset",0)
        energies = [e-offset for e in self.energies]
        dos = self.total()
        return plt.plot(energies, dos, **kwargs)

    def plot_interstitial(self, **kwargs):
        """
            Returns matplotlib.pyplot.plot object with interstitial dos as y data.
            Args(optional):
                float :: offset
        """
        offset = kwargs.pop("offset",0)
        energies = [e-offset for e in self.energies]
        dos = self.interstitial()
        return plt.plot(energies, dos, **kwargs)

    def plot_specieslm(self, species, l, m, **kwargs):
        """
            Returns matplotlib.pyplot.plot object with specieslm dos as y data.
            Args(optional):
                float :: offset
        """
        offset = kwargs.pop("offset",0)
        energies = [e-offset for e in self.energies]
        dos = self.specieslm(species, l, m)
        return plt.plot(energies, dos, **kwargs)

    def plot_speciesl(self, species, l, **kwargs):
        """
            Returns matplotlib.pyplot.plot object with speciesl dos as y data.
            Args(optional):
                float :: offset
        """
        offset = kwargs.pop("offset",0)
        energies = [e-offset for e in self.energies]
        dos = self.speciesl(species, l)
        return plt.plot(energies, dos, **kwargs)

    def plot_angular(self, l, **kwargs):
        """
            Returns matplotlib.pyplot.plot object with angular dos as y data.
            Args(optional):
                float :: offset
        """
        offset = kwargs.pop("offset",0)
        energies = [e-offset for e in self.energies]
        dos = self.angular(l)
        return plt.plot(energies, dos, **kwargs)

    def plot_atom(self, species, atom, **kwargs):
        """
            Returns matplotlib.pyplot.plot object with angular dos as y data.
            Args(optional):
                float :: offset
        """
        offset = kwargs.pop("offset",0)
        energies = [e-offset for e in self.energies]
        dos = self.atom(species, atom)
        return plt.plot(energies, dos, **kwargs)

    def plot_species(self, species, **kwargs):
        """
            Returns matplotlib.pyplot.plot object with species dos as y data.
            Args(optional):
                float :: offset
        """
        offset = kwargs.pop("offset",0)
        energies = [e-offset for e in self.energies]
        dos = self.species(species)
        return plt.plot(energies, dos, **kwargs)
