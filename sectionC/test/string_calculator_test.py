import unittest
from src import string_calculator as string_calculator



class StringCalculatorTest(unittest.TestCase):
    def test_value(self):
      self.assertEqual(string_calculator.string_calc('3.2'), '3.2', 'string_calc(%s)' % ('3.2'))
    
    def test_factorial(self):
      self.assertEqual(string_calculator.string_calc('factorial 5'), '120', 'string_calc(%s)' % ('factorial 5'))
    
    def test_fibonacci(self):
      self.assertEqual(string_calculator.string_calc('fibonacci 12'), '8', 'string_calc(%s)' % ('fibonacci 12'))
    
    def test_prime(self):
      self.assertEqual(string_calculator.string_calc('prime 10'), '7', 'string_calc(%s)' % ('prime 10'))
      self.assertEqual(string_calculator.string_calc('prime 12'), '11', 'string_calc(%s)' % ('prime 12'))
      self.assertEqual(string_calculator.string_calc('prime 15'), '13', 'string_calc(%s)' % ('prime 15'))
    
    def test_addition(self):
      self.assertEqual(string_calculator.string_calc('+ 12.5 12.6'), '25.1', 'string_calc(%s)' % ('+ 12.5 12.6'))
      self.assertEqual(string_calculator.string_calc('+ 3.22 3.22'), '6.44', 'string_calc(%s)' % ('+ 3.22 3.22'))
      self.assertEqual(string_calculator.string_calc('+ 3.22239 3.22239'), '6.44478', 'string_calc(%s)' % ('+ 3.22239 3.22239'))
      self.assertEqual(string_calculator.string_calc('+ 3.22235 3.22235'), '6.4447', 'string_calc(%s)' % ('+ 3.22235 3.22235'))

    def test_subtraction(self):
      self.assertEqual(string_calculator.string_calc('- 43.7 50'), '-6.3', 'string_calc(%s)' % ('- 43.7 50'))
    
    def test_multiplication(self):
      self.assertEqual(string_calculator.string_calc('* 6 -12'), '-72', 'string_calc(%s)' % ('* 6 -12'))
      self.assertEqual(string_calculator.string_calc('* 6 12'), '72', 'string_calc(%s)' % ('* 6 12'))
      self.assertEqual(string_calculator.string_calc('* 0.1 0.1'), '0.01', 'string_calc(%s)' % ('* 0.1 0.1'))
      self.assertEqual(string_calculator.string_calc('* -0.1 -0.1'), '0.01', 'string_calc(%s)' % ('* -0.1 -0.1'))
      self.assertEqual(string_calculator.string_calc('* 0.1 -0.1'), '-0.01', 'string_calc(%s)' % ('* 0.1 -0.1'))
      self.assertEqual(string_calculator.string_calc('* -0.1 0.1'), '-0.01', 'string_calc(%s)' % ('* -0.1 0.1'))
    
    def test_division(self):
      self.assertEqual(string_calculator.string_calc('/ 20 10'), '2', 'string_calc(%s)' % ('/ 20 10'))
      self.assertEqual(string_calculator.string_calc('/ 5 2'), '2.5', 'string_calc(%s)' % ('/ 5 2'))
      self.assertEqual(string_calculator.string_calc('/ 0.5 2'), '0.25', 'string_calc(%s)' % ('/ 0.5 2'))
      self.assertEqual(string_calculator.string_calc('/ 0.05 2'), '0.025', 'string_calc(%s)' % ('/ 0.05 2'))
      self.assertEqual(string_calculator.string_calc('/ 0.05 0.02'), '2.5', 'string_calc(%s)' % ('/ 0.05 0.02'))
      self.assertEqual(string_calculator.string_calc('/ 0.5 0.2'), '2.5', 'string_calc(%s)' % ('/ 0.5 0.2'))
      self.assertEqual(string_calculator.string_calc('/ 2 10'), '0.2', 'string_calc(%s)' % ('/ 2 10'))
      self.assertEqual(string_calculator.string_calc('/ 0.05 0.2'), '0.25', 'string_calc(%s)' % ('/ 0.05 0.2'))
    
    def test_whitespace_removal(self):
      self.assertEqual(string_calculator.string_calc('\t 3.22  '), '3.22', 'string_calc(%s)' % ('\t 3.22  '))

    def test_nested_expressions(self):
      self.assertEqual(string_calculator.string_calc('/ (factorial (* 2 2 5)) 600'), '4054836680294400', 'string_calc(%s)' % ('/ (factorial (* 2 2 5)) 600'))
      self.assertEqual(string_calculator.string_calc('* (* 2 2 5) 4'), '80', 'string_calc(%s)' % ('* (* 2 2 5) 4'))
      self.assertEqual(string_calculator.string_calc('* (* 2 2 5) 4 3 2'), '480', 'string_calc(%s)' % ('* (* 2 2 5) 4 3 2'))
      self.assertEqual(string_calculator.string_calc('/ (* (* 2 2 5) 4 3 2) 3'), '160', 'string_calc(%s)' % ('/ (* (* 2 2 5) 4 3 2) 3'))
      self.assertEqual(string_calculator.string_calc('* (/ (* (* 2 2 5) 4 3 2) 3) 5'), '800', 'string_calc(%s)' % ('* (/ (* (* 2 2 5) 4 3 2) 3) 5'))
      self.assertEqual(string_calculator.string_calc('* (/ (* (* 2 2 5) 4 3 2) 3) 5 10 2'), '16000', 'string_calc(%s)' % ('* (/ (* (* 2 2 5) 4 3 2) 3) 5 10 2'))
      self.assertEqual(string_calculator.string_calc('/ (* (/ (* (* 2 2 5) 4 3 2) 3) 5 10 2) 2'), '8000', 'string_calc(%s)' % ('/ (* (/ (* (* 2 2 5) 4 3 2) 3) 5 10 2) 2'))
      self.assertEqual(string_calculator.string_calc('prime (* 2 2 5)'), '19', 'string_calc(%s)' % ('prime (* 2 2 5)'))
      self.assertEqual(string_calculator.string_calc('/ (prime (* 2 2 5)) 100'), '0.19', 'string_calc(%s)' % ('/ (prime (* 2 2 5)) 100'))
      self.assertEqual(string_calculator.string_calc('/ (* (/ (* (prime (* 2 2 5) 5) 4 3 2) 3) 5 10 2) 2'), '7600', 'string_calc(%s)' % ('/ (* (/ (* (prime (* 2 2 5) 5) 4 3 2) 3) 5 10 2) 2'))

    def test_overflow(self): # Program does not crash
      self.assertEqual(string_calculator.string_calc('* 1.0142320547350045e+304 1.0142320547350045e+304'), 'inf', 'string_calc(%s)' % ('* 1.0142320547350045e+304 1.0142320547350045e+304'))
      self.assertEqual(string_calculator.string_calc('/ 1.0142320547350045e+304 1.0142320547350045e-304'), 'inf', 'string_calc(%s)' % ('/ 1.0142320547350045e+304 1.0142320547350045e-304'))
    
    def test_unknown_operator(self): # Program does not crash. Appropriate message is returned.
      self.assertEqual(string_calculator.string_calc('& 1 1'), 'Unknown operator!', 'string_calc(%s)' % ('& 1 1'))
      self.assertEqual(string_calculator.string_calc('@ 1 1'), 'Unknown operator!', 'string_calc(%s)' % ('@ 1 1'))

if __name__ == '__main__':
  unittest.main()
