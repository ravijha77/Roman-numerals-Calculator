import unittest
import roman

class Testing(unittest.TestCase):

	#Testing all the addition functionalities of the code
    def test_simple_addition(self):
        a = 'II'
        b = 'IV'
        c = 'VI'
        self.assertEqual(c, roman.add(a, b))
        d = 'VII'
        self.assertNotEqual(d, roman.add(a, b))
        e = 'IIII'
        self.assertNotEqual(e, roman.add(a, b))

    #Testing all simple Substraction functionalities of the code
    def test_simple_substraction(self):
        a = 'XII'
        b = 'IV'
        c = 'VIII'
        self.assertEqual(c, roman.sub(a, b))
        d = 'VII'
        self.assertNotEqual(d, roman.sub(a, b))

    #Testing all simple Multplication functionalities of the code
    def test_simple_multiplication(self):
        a = 'II'
        b = 'V'
        c = 'X'
        self.assertEqual(c, roman.mult(a, b))
        d = 'IX'
        self.assertNotEqual(d, roman.mult(a, b))

    #Testing all the simple Division rules of the code
    def test_simple_division(self):
        a = 'XXIV'
        b = 'IV'
        c = 'VI'
        self.assertEqual(c, roman.div(a, b))
        d = 'C'
        self.assertNotEqual(d, roman.div(a, b))
    
    #Testing the Addition Symmetry of the code
    def test_addition_symmetry(self):
        a = 'II'
        b = 'IV'
        self.assertEqual(roman.add(b, a), roman.add(a, b))
    
    #Testing Addition Symmetry Property in the code
    def test_addition_associativity(self):
        a = 'X'
        b = 'V'
        c = 'C'
        self.assertEqual(roman.add(a, roman.add(b, c)), roman.add(roman.add(a, b), c))
    
    #Testing Addition Multiplication Duo of the code
    def test_multiplication_by_addition(self):
        a = 'VI'
        b = 'XL'
        c = 'V'
        self.assertEqual(roman.add(roman.mult(a, b), roman.mult(c, b)), roman.mult(roman.add(a, c), b))
    
    #Testing the Integer To Roman Conversion
    def test_integer_to_roman(self):
        a = 4
        b = 'IV'
        c = 'IIII'		
        self.assertEqual(b, roman.integer_to_roman(a))
        self.assertNotEqual(c, roman.integer_to_roman(a))
    
    #Testing the Roman to Integer Conversion
    def test_roman_to_integer(self):
        a = 'XL'
        c = 40		
        self.assertEqual(c, roman.roman_to_integer(a))

    #Testing the Authencity of the Roman Literal provided
    def test_correct_roman(self):
    	a = 'XXXX'
    	b = 'XL'
    	self.assertTrue(roman.check_correct_roman(b))
    	self.assertFalse(roman.check_correct_roman(a))

if __name__ == '__main__':
    unittest.main()
