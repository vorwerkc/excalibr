#!/usr/bin/python

import xml.etree.cElementTree as ET
import sys
import scipy.constants as const
import numpy as np
from math import *
import os

def parse_info(name):

    root = ET.parse(name)
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

def parse_input(name):
    root = ET.parse(name)
    excitingInput={}
    #parsing the structure part into dictionary (conventions close to pymatgen)
    elements = []
    positions = []
    vectors=[]
    lockxyz=[]
    for nodes in root.find('structure').getiterator('species'):
        symbol = nodes.get('speciesfile').split('.')[0]
        if len(symbol.split('_'))==2:
            symbol=symbol.split('_')[0]
        element = symbol
        natoms = nodes.getiterator('atom')
        for atom in natoms:
            x, y, z = atom.get('coord').split()
            positions.append([float(x), float(y), float(z)])
            elements.append(element)
            # Obtain lockxyz for each atom
            if atom.get('lockxyz') is not None:
                lxy=[]
                for l in atom.get('lockxyz').split():
                    if l=='True' or l=='true':
                        lxyz.append(True)
                    else:
                        lxyz.append(False)
                lockxyz.append(lxyz)
            else:
                lockxyz.append([False, False, False])
        #check the atomic positions type
        if 'cartesian' in root.find('structure').attrib.keys():
            if root.find('structure').attrib['cartesian']:
                cartesian=True
        else:
            cartesian=False
        # get the scale attribute
        scale_in=root.find('structure').find('crystal').get('scale')
        if scale_in:
            scale=float(scale_in)
        else:
            scale=1.0
        # define conversion factor between Bohr radius and Angstrom
        bohr2ang=const.value('Bohr radius')/const.value('Angstrom star')
        # get the stretch attribute
        stretch_in=root.find('structure').find('crystal').get('stretch')
        if stretch_in:
            stretch=np.array([float(a) for a in stretch_in])
        else:
            stretch=np.array([1.0,1.0,1.0])
        # get basis vectors and scale them accordingly
    basisnode=root.find('structure').find('crystal').iter('basevect')
    for vect in basisnode:
        x, y, z=vect.text.split()
        vectors.append([float(x)*stretch[0],
                        float(y)*stretch[1],
                        float(z)*stretch[2]])
    structure={'lattice':vectors, 'elements':elements, 'positions':positions,
                   'cartesian':cartesian}
    excitingInput['structure']=structure
    # parsing the groundstate part of the xml into dictionary
    for node in root.getiterator('groundstate'):
        groundstate=node.attrib
        excitingInput['groundstate']=groundstate
        for instance in node.getchildren():
            excitingInput['groundstate'][str(instance.tag)]=instance.attrib
    # parsing the properties part of the xml
    properties={}
    if root.find('properties') is not None:
        for instance in root.find('properties').getchildren():
            properties[str(instance.tag)]=instance.attrib
            if instance.tag=='bandstructure':
                path=[]
                kpoints={}
                for node in instance.getiterator('plot1d'):
                    path2=[]
                    for node2 in node.find('path').getiterator('point'):
                        path2.append(node2.get('label'))
                        if str(node2.get('label')) not in kpoints:
                            coords=[float(i) for i in node2.get('coord').split('   ')]
                            kpoints[node2.get('label')]=coords
                    path.append(path2)
                properties['bandstructure']={'path':path, 'kpoints': kpoints}
        excitingInput['properties']=properties
    return excitingInput
