#!/usr/bin/python

import xml.etree.cElementTree as ET
import sys
import numpy as np
from math import *
import os

def parse_info(name):
    root = ET.parse(name)
#    if root.find('groundstate').get('status')=='finished':
#        self.finished=True
#    else:
#        self.finished=False
    i=0
    excitingRun=[]
    for node in root.find('groundstate').find('scl').iter('iter'):
        excitingRun.append(node.attrib)
        excitingRun[i]['energies']=node.find('energies').attrib
        excitingRun[i]['charges']=node.find('charges').attrib
        atom_nr=0
        atomic_charge=[]
        species=[]
        for atoms in node.find('charges').iter('atom'):
            if atom_nr==0 : species_old=atoms.get('species')
            atom_nr=atom_nr+1
            if atoms.get('species') == species_old:
                species.append({'muffin-tin':atoms.get('muffin-tin')})
            else:
                species_old=atoms.get('species')
                atomic_charge.append(species)
                species=[{'muffin-tin':atoms.get('muffin-tin')}]
            atomic_charge.append(species)
            excitingRun[i]['charges']['atomic']=atomic_charge
        excitingRun[i]['timing']=node.find('timing').attrib
        if node.find('moments') is not None:
            moments={}
            moments['momtot']=node.find('moments').find('momtot').attrib
            moments['interstitial']=node.find('moments').find('momtot').attrib
            moments['mommttot']=node.find('moments').find('interstitial').attrib
            excitingRun[i]['moments']=moments
            atom_nr=0
            atomic_moment=[]
            species=[]
            for atoms in node.find('moments').iter('atom'):
                if atom_nr==0 : species_old=atoms.get('species')
                atom_nr=atom_nr+1
                if atoms.get('species') == species_old:
                    species.append(atoms.find('mommt').attrib)
                else:
                    species_old=atoms.get('species')
                    atomic_moment.append(species)
                    species=[atoms.find('mommt').attrib]
            atomic_moment.append(species)
            excitingRun[i]['moments']['atomic']=atomic_moment
        i=i+1
    return excitingRun
