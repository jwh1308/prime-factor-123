class PrimeFactor:
    def of(self, number):
        factors = []
        if number > 1:
            if number < 4:
                factors.append(number)
            else:
                while number % 2 == 0:
                    factors.append(2)
                    number //= 2
                while number % 3 == 0:
                    factors.append(3)
                    number //= 3
        return factors
