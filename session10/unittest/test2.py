import unittest
import test1

class Test(unittest.TestCase):
    
    def test_one(self):
        name = "rama"
        result = test1.test_func(name)
        self.assertEqual(result, 'Rama')

    def test_two(self):
        name = "rama rama"
        result = test1.test_func(name)
        self.assertEqual(result, "Rama Rama")

    def test_more(self):
        name = "rama rama rama"
        result = test1.test_func(name)
        self.assertEqual(result, "Rama Rama Rama")
if __name__ == "__main__":
    unittest.main()