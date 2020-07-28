import unittest
import numpy as np
from excalibr import parsedos, parseband, parsegrst

factor = 27.211


class TestParseBand(unittest.TestCase):

    def test_getbands(self):
        bands = parseband.bandstr('testfiles/band.xml')
        x,y,miny,maxy = bands.getbands(1,3)
        shouldbe = np.array([0.0,1.,2.]),np.array([[0.,1.,2.],[3.,4.,5.]])*factor,0.0*factor,5.0*factor

        self.assertTrue(np.all(x==shouldbe[0]))
        self.assertTrue(np.all(y==shouldbe[1]))
        self.assertTrue(np.all(miny==shouldbe[2]))
        self.assertTrue(np.all(maxy==shouldbe[3]))

    def test_getbands_c(self):
        bands = parseband.bandstr('testfiles/band_c.xml')
        x,y,miny,maxy = bands.getbands(1,2)
        shouldbe = np.array([0.0,1.,2.]),np.array([[0.,1.,2.]])*factor,0.0*factor,2.0*factor

        self.assertTrue(np.all(x==shouldbe[0]))
        self.assertTrue(np.all(y==shouldbe[1]))
        self.assertTrue(np.all(miny==shouldbe[2]))
        self.assertTrue(np.all(maxy==shouldbe[3]))

    def test_getlabels(self):
        bands = parseband.bandstr('testfiles/band.xml')
        x, labels = bands.getlabels()
        shouldbe = [np.array([0.,1.,2.]),["$X$","$Y$","$Z$"]]
        self.assertTrue(np.all(x==shouldbe[0]))
        self.assertListEqual(labels, shouldbe[1])

    def test_getlabels_c(self):
        bands = parseband.bandstr('testfiles/band_c.xml')
        x, labels = bands.getlabels()
        shouldbe = [np.array([0.,1.,2.]),["$X$","$Y$","$Z$"]]
        self.assertTrue(np.all(x==shouldbe[0]))
        self.assertListEqual(labels, shouldbe[1])

    def test_atoml(self):
        bands = parseband.bandstr('testfiles/band_c.xml')
        x,y,c = bands.atoml(1,1,0)
        shouldbe = [np.array([0.,1.,2.]),np.array([0.,1.,2.])*factor,np.array([0.,3.,6.])]
        self.assertTrue(np.all(x==shouldbe[0]))
        self.assertTrue(np.all(y==shouldbe[1]))
        self.assertTrue(np.all(c==shouldbe[2]))

    def test_atom(self):
        bands = parseband.bandstr('testfiles/band_c.xml')
        x,y,c = bands.atom(1,1)
        shouldbe = [np.array([0.,1.,2.]),np.array([0.,1.,2.])*factor,np.array([3.,12.,21.])]
        self.assertTrue(np.all(x==shouldbe[0]))
        self.assertTrue(np.all(y==shouldbe[1]))
        self.assertTrue(np.all(c==shouldbe[2]))

    def test_speciesl(self):
        bands = parseband.bandstr('testfiles/band_c.xml')
        x,y,c = bands.speciesl(1,0)
        shouldbe = [np.array([0.,1.,2.]),np.array([0.,1.,2.])*factor,np.array([0.,6.,12.])]
        self.assertTrue(np.all(x==shouldbe[0]))
        self.assertTrue(np.all(y==shouldbe[1]))
        self.assertTrue(np.all(c==shouldbe[2]))

    def test_species(self):
        bands = parseband.bandstr('testfiles/band_c.xml')
        x,y,c = bands.species(1)
        shouldbe = [np.array([0.,1.,2.]),np.array([0.,1.,2.])*factor,np.array([6.,24.,42.])]
        self.assertTrue(np.all(x==shouldbe[0]))
        self.assertTrue(np.all(y==shouldbe[1]))
        self.assertTrue(np.all(c==shouldbe[2]))


if __name__ == '__main__':
    unittest.main()
