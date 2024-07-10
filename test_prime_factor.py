from unittest import TestCase

from prime_factor import PrimeFactor


class TestPrimeFactor(TestCase):
    def setUp(self):
        super().setUp()
        self.prime_factor = PrimeFactor()

    def test_prime_factor(self):
        self.assertEqual(self.prime_factor.of(1), [])

    def test_prime_factor_2(self):
        self.assertEqual(self.prime_factor.of(2), [2])

    def test_prime_factor_3(self):
        self.assertEqual(self.prime_factor.of(3), [3])

    def test_prime_factor_4(self):
        self.assertEqual(self.prime_factor.of(4), [2, 2])

    def test_prime_factor_6(self):
        self.assertEqual(self.prime_factor.of(6), [2, 3])

    def test_prime_factor_9(self):
        self.assertEqual(self.prime_factor.of(9), [3, 3])
