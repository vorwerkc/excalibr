import unittest
import numpy as np
from excalibr import parsedos, parseband, parsegrst
from scipy.constants import physical_constants
from reference import energies, interstitial, angular, species, speciesl, \
        atom, atoml

factor=physical_constants['Hartree energy in eV'][0]

class TestParseDos(unittest.TestCase):
    def test_energies(self):
        dos = parsedos.dos("testfiles/dos_diamond.xml")
        # test whether shapes are identical
        self.assertTrue(np.all(dos.energies.shape == energies.shape))
        # test whether all entries are (almost) the same
        np.testing.assert_almost_equal(dos.energies, energies)
    
    def test_interstitial(self):
        dos = parsedos.dos("testfiles/dos_diamond.xml")
        # test whether shapes are identical
        self.assertTrue(np.all(dos.interstitial().shape == interstitial.shape )) 
        # test whether all entries are (almost) the same
        np.testing.assert_almost_equal(dos.interstitial(), interstitial)

    def test_angular(self):
        dos = parsedos.dos("testfiles/dos_diamond.xml")
        for l in [0,1,2,3]:
            # test whether shapes are identical
            self.assertTrue(np.all(dos.angular(l).shape == angular[l].shape)) 
            # test whether all entries are (almost) the same
            np.testing.assert_almost_equal(dos.angular(l), angular[l])

    def test_species(self):
        dos = parsedos.dos("testfiles/dos_diamond.xml")
        # test whether shapes are identical
        self.assertTrue(np.all(dos.species(1).shape == species.shape )) 
        # test whether all entries are (almost) the same
        np.testing.assert_almost_equal(dos.species(1), species)

    def test_speciesl(self):
        dos = parsedos.dos("testfiles/dos_diamond.xml")
        for l in [0,1,2,3]:
            # test whether shapes are identical
            self.assertTrue(np.all(dos.speciesl(1,l).shape == speciesl[l].shape)) 
            # test whether all entries are (almost) the same
            np.testing.assert_almost_equal(dos.speciesl(1,l), speciesl[l])
    
    def test_atom(self):
        dos = parsedos.dos("testfiles/dos_diamond.xml")
        # test whether shapes are identical
        self.assertTrue(np.all(dos.atom(1,1).shape == atom.shape )) 
        # test whether all entries are (almost) the same
        np.testing.assert_almost_equal(dos.atom(1,1), atom)

    def test_atoml(self):
        dos = parsedos.dos("testfiles/dos_diamond.xml")
        for l in [0,1,2,3]:
            # test whether shapes are identical
            self.assertTrue(np.all(dos.atoml(1,1,l).shape == atoml[l].shape)) 
            # test whether all entries are (almost) the same
            np.testing.assert_almost_equal(dos.atoml(1,1,l), atoml[l])

    def test_specieslm(self):
        dos = parsedos.dos("testfiles/dos.xml")
        shouldbe = np.array([3,4,5]).astype(np.float)
        self.assertTrue(np.all(dos.specieslm(1,0,0)==shouldbe))

    def test_total(self):
        dos = parsedos.dos("testfiles/dos.xml")
        shouldbe = np.array([101,102,103]).astype(np.float)
        self.assertTrue(np.all(dos.total()==shouldbe))


if __name__ == '__main__':
    unittest.main()
