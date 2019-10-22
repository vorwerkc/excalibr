import unittest
import numpy as np
from excalibr import parsedos, parseband, parsegrst

factor = 27.21138


class TestParseDos(unittest.TestCase):
    def test_energies(self):
        dos = parsedos.dos("testfiles/dos.xml")
        shouldbe = np.array([0,1,2])*factor
        self.assertTrue(np.all(dos.energies==shouldbe))

    def test_species(self):
        dos = parsedos.dos("testfiles/dos.xml")
        shouldbe = np.array([18,22,26]).astype(np.float)
        self.assertTrue(np.all(dos.species(1)==shouldbe))

    def test_atom(self):
        dos = parsedos.dos("testfiles/dos.xml")
        shouldbe = np.array([9,11,13]).astype(np.float)
        self.assertTrue(np.all(dos.atom(1,1)==shouldbe))

    def test_angular(self):
        dos = parsedos.dos("testfiles/dos.xml")
        shouldbe = np.array([24,28,32]).astype(np.float)
        self.assertTrue(np.all(dos.angular(1)==shouldbe))

    def test_speciesl(self):
        dos = parsedos.dos("testfiles/dos.xml")
        shouldbe = np.array([12,14,16]).astype(np.float)
        self.assertTrue(np.all(dos.speciesl(1,1)==shouldbe))

    def test_atoml(self):
        dos = parsedos.dos("testfiles/dos.xml")
        shouldbe = np.array([6,7,8]).astype(np.float)
        self.assertTrue(np.all(dos.atoml(1,1,1)==shouldbe))

    def test_specieslm(self):
        dos = parsedos.dos("testfiles/dos.xml")
        shouldbe = np.array([3,4,5]).astype(np.float)
        self.assertTrue(np.all(dos.specieslm(1,0,0)==shouldbe))

    def test_interstitial(self):
        dos = parsedos.dos("testfiles/dos.xml")
        shouldbe = np.array([9,10,11]).astype(np.float)
        self.assertTrue(np.all(dos.interstitial()==shouldbe))

    def test_total(self):
        dos = parsedos.dos("testfiles/dos.xml")
        shouldbe = np.array([101,102,103]).astype(np.float)
        self.assertTrue(np.all(dos.total()==shouldbe))


if __name__ == '__main__':
    unittest.main()
