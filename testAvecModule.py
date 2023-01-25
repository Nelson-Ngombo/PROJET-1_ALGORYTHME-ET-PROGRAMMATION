import main as tp
import unittest
import math
class testDuModuleFormGeom(unittest.TestCase):
    

    def test_perimetreRect(self):
        x = tp.rectangle(10,15).perimetre()
        y = 50
        self.assertEqual(x,y)

    def test_aireRect(self):
        x= tp.rectangle(4,5).surface()
        y = 20
        self.assertEqual(x,y)
        


    def test_perimetreCercle(self):
        x = tp.cercle(5).perimetre()
        y = 5*2*math.pi
        self.assertEqual(x,y)

    def test_aireCercle(self):
        x = tp.cercle(4).surface()
        y = 4**2*math.pi
        self.assertEqual(x,y)
        


    def test_perimetreTri(self):
        x = tp.triangle(5,4,4,2).perimetre()
        y = 10
        self.assertEqual(x,y)

    def test_aireTri(self):
        x = tp.triangle(3,10,6,5).surface()
        y = 15
        self.assertEqual(x,y)


    def test_perimetreCarre(self):
        x= tp.carre(10).perimetre()
        y = 40
        self.assertEqual(x,y)

    def test_aireCarre(self):
        x = tp.carre(15).surface()
        y = 225
        self.assertEqual(x,y)


    def test_perimetreTrirect(self):
        x= tp.triangle_rectangle(4,4,6).perimetre()
        y = 14
        self.assertEqual(x,y)

    def test_aireTrirect(self):
        x = tp.triangle_rectangle(5,5,5).surface()
        y = 12.5
        self.assertEqual(x,y)

if __name__ == '__main__':
    unittest.main()
