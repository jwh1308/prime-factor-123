from unittest import TestCase

from prime_factor import PrimeFactor


class TestPrimeFactor(TestCase):
    def test_prime_factor(self):
        prime_factor = PrimeFactor()
        self.assertEqual(prime_factor.of(1), [])
