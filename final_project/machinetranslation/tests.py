import unittest
from translator import english_To_French, french_To_English

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishToFrench('oui'), 'Bonjour')
        self.assertNotEqual(englishToFrench('Hello'), '')

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertNotEqual(frenchToEnglish('yes'), 'Hello')
        self.assertNotEqual(frenchToEnglish('Bonjour'), '')

unittest.main()