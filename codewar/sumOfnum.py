import unittest

def get_sum(a, b):
    sumatoria = 0
    if a < b:
        for num in range(a, b + 1):
            sumatoria += num
    else:
        for num in range(b, a + 1):
            sumatoria += num
    return sumatoria

class TestGetSum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(get_sum(1, 2), 3)  # Suma de números positivos consecutivos
        self.assertEqual(get_sum(5, 10), 45)  # Suma ascendente de números positivos

    def test_negative_numbers(self):
        self.assertEqual(get_sum(-1, -5), -15)  # Suma de números negativos consecutivos
        self.assertEqual(get_sum(-5, -1), -15)  # Suma descendente de números negativos

    def test_mixed_numbers(self):
        self.assertEqual(get_sum(-1, 1), 0)  # Suma de números positivos y negativos que se cancelan mutuamente

    def test_single_number(self):
        self.assertEqual(get_sum(5, 5), 5)  # Suma de un solo número

if __name__ == '__main__':
    unittest.main()
