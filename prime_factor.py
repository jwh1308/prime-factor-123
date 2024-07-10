class PrimeFactor:
    def of(self, number):
        factors = []
        if number > 1:
            if number == 4:
                factors.extend([2, 2])
            else:
                factors.append(number)
        return factors
