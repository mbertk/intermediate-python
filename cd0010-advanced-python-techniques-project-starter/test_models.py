import unittest
from models import NearEarthObject, CloseApproach


class MyTestCase(unittest.TestCase):
    def test_NearEarthObject1(self):
        neo = NearEarthObject("somewhere far", False, name="Neo", diameter=2.5)
        self.assertEqual(neo.name, "Neo"), f"Expected: Neo, got: {neo.name}"
        self.assertEqual(neo.designation, "somewhere far"), f"Expected: somewhere far, got: {neo.designation}"
        self.assertEqual(neo.hazardous, False), f"Expected: False, got: {neo.hazardous}"
        self.assertEqual(neo.diameter, 2.5), f"Expected: 2.5, got: {neo.diameter}"

    def test_NearEarthObject2(self):
        neo = NearEarthObject("somewhere far", False)
        self.assertEqual(neo.name, None), f"Expected: None, got: {neo.name}"
        self.assertEqual(neo.designation, "somewhere far"), f"Expected: somewhere far, got: {neo.designation}"
        self.assertEqual(neo.hazardous, "Neo"), f"Expected: False, got: {neo.hazardous}"
        self.assertEqual(neo.diameter, float('nan')), f"Expected: float('nan'), got: {neo.diameter}"






if __name__ == '__main__':
    unittest.main()
