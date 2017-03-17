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
        if self.tree.xpath('/bandstructure/@character')[0]=='true':
            self.character=True
        else:
            self.character=False
        if self.character:
            self.pts=self.tree.xpath('/bandstructure/species[1]/atom[1]/band[1]/point/@distance')
            self.bands=len(self.tree.xpath('/bandstructure/species[1]/atom[1]/band'))
        else:
            self.pts = self.tree.xpath('/bandstructure/band[1]/point/@distance')
            self.bands =len(self.tree.xpath('/bandstructure/band'))

    def getband(self, bandnr):
        y = [float(xe)*27.211 for xe in self.tree.xpath("/bandstructure/band[%i]/point/@eval"%(bandnr))]
        return self.pts, y

    def getbands(self, bandmin, bandmax):
        if not self.character:
            y=[]
            for i in range(bandmin,bandmax):
                if (i==bandmin):
                    x=self.getband(i)[0]
                y.append(self.getband(i)[1])
            windowlow=min(y[0])
            windowhigh=max(y[-1])
        else:
            raise ValueError('Subroutine not defined if character is true!')
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

    def get_character_bands(self):
        if self.character:
            out=[]
            bands=self.tree.xpath('/bandstructure/species[1]/atom[1]/band')
            for band in bands:
                for xe in band.xpath("./point/@eval"):
                    out.append(float(xe)*27.211)
        else:
            raise ValueError('Subroutine not defined if character is false!')
        return self.pts, out

    def get_bandcharacter(self,species,atom,l):
        if self.character:
            out_bands=[]
            bands=self.tree.xpath('/bandstructure/species[@speciesnr="%s"]/atom[@atomnr="%s"]/band'%(species, atom))
            for band in bands:
                for pts in band.xpath('./point'):
                    out_bands.append(pts.xpath('./bc[@l="%s"]/@character'%l)[0])
        else:
            raise ValueError('Subroutine not defined if character is false!')
        return out_bands

    def atoml(self,species, atom, l):
        pts, bands=self.get_character_bands()
        characters=self.get_bandcharacter(species,atom, l)
        pts_out=[]
        for i in range(self.bands):
            for j in range(len(self.pts)):
                pts_out.append(pts[j])
        return pts_out, bands, characters
    
    def atom(self, species, atom):
        pts,bands=self.get_character_bands()
        out_bands=[]

        pts_out=[]
        for i in range(self.bands):
            for j in range(len(self.pts)):
                pts_out.append(pts[j])       
        __bands=self.tree.xpath('/bandstructure/species[@speciesnr="%s"]/atom[@atomnr="%s"]/band'%(species, atom))
        for band in __bands:
            for pts in band.xpath('./point'):
                out_bands.append(pts.xpath('./@sum'))
        return pts_out, bands, out_bands  
            

