#Pecahan.py
def gcd(a,b):
    """ Calculate the greatest common divisor of
    two positive integers """
    while b > 0:
        rem = a%b
        a = b
        b = rem
    return a
def lcm(a,b):
    """ Calculate the lowest common multiple of two positive integers."""
    return (a*b)//gcd(a,b) # // ensures an int is returned

class Pecahan:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __str__(self):
        if self.denom == 1:
            return str(self.numer)
        return f"{self.numer}/{self.denom}"
    
    def __repr__(self):
        """ Used in interpreter's response """
        return f"Pecahan({self.numer},{self.denom})"

    def __add__(self, param):
        """ Add two Pecahans. Allows int as a parameter"""
        if type(param) == int:  # convert int to Pecahan
            param = Pecahan(param)
        if type(param) == Pecahan:
            # find a common denominator (lcm)
            the_lcm = lcm(self.denom, param.denom)
            # multiply each by the lcm, then add
            numerator_sum = (the_lcm * self.numer // self.denom) + \
                            (the_lcm * param.numer // param.denom)
            return Pecahan(numerator_sum, the_lcm)
        else:
            print('wrong type')  # problem: some type we cannot handle
            raise(TypeError)

    def __sub__(self, param):
        """ Subtract two Pecahans"""
        # subtraction is the same but with '-' instead of '+'
        if type(param) == Pecahan:
            the_lcm = lcm(self.denom, param.denom)
            numerator_diff = (the_lcm * self.numer // self.denom) - \
                             (the_lcm * param.numer // param.denom)
            return Pecahan(numerator_diff, the_lcm)
        else:
            print('wrong type')
            raise(TypeError)

    def reduce(self):
        """ Return the reduced Pecahan """
        # find the gcd and then divide numerator and denominator by gcd
        the_gcd = gcd(self.numer, self.denom)
        return Pecahan(self.numer // the_gcd, self.denom // the_gcd)

    def __eq__(self, param):
        """ Compare two Pecahans for equality, return Boolean"""
        # reduce both; then check that numerators and denominators are equal
        reduced_self = self.reduce()
        reduced_param = param.reduce()
        return reduced_self.numer == reduced_param.numer and \
               reduced_self.denom == reduced_param.denom

    def __radd__(self, param):
        """ Add two Pecahans, with arguments reversed """
        # mapping is reversed: if "1 + x", x maps to self, and 1 maps to param
        # mapping is already reversed so self will be Pecahan; call __add__
        return self.__add__(param)
    
    def __mul__(self, param):
        if isinstance(param, int):
            return Pecahan(self.numer * param, self.denom)  # Integer multiplication 
        elif isinstance(param, Pecahan):
            return Pecahan(self.numer * param.numer, self.denom * param.denom)  # Multiply both numerator and denominator
        
    def __rmul__(self, other):  # Same concept as r add ( left operand does not support operation, so we reverse it)
        if isinstance(other, int):
            return Pecahan(self.numer * other, self.denom)
        else:
            raise TypeError("Unsupported operand type")
    
    def __truediv__(self,param):
        if not isinstance(param, Pecahan):  # Convert integer to fraction to prepare for division
            param = Pecahan(param,1)
        return Pecahan(self.numer*param.denom, self.denom*param.numer)  # Multiply by reciprocal
    
    def __gt__(self,param):
        the_lcm = lcm(self.denom, param.denom)  # Make the fractions have the same denominator then compare them
        return (the_lcm*self.numer // self.denom) > (the_lcm*param.numer // param.denom)
    
    def __ge__(self,param):
        the_lcm = lcm(self.denom, param.denom)
        return (the_lcm*self.numer // self.denom) >= (the_lcm*param.numer // param.denom)
    
    def __getitem__(self,index):  # Check for index 1 and 2 and return numerator and denominator
        if index == 1:
            return self.numer
        if index == 2:
            return self.denom
        else:
            raise ValueError("index out of range")
    
def main():
    p1 = Pecahan(3,5)
    p2 = Pecahan(1,20)
    print( Pecahan(8,1) ) # 8
    print( p1*p2 ) # 3/100
    print( p1/p2 ) # 60/5
    print( p1*3 ) # 9/5
    print( 3*p1 ) # 9/5
    print( p1[1] ) # 3
    print( p1[2] ) # 5
    print( p1 > p2 ) # True
    print( p2 > p1 ) # False
    print( Pecahan(1,2) >= Pecahan(3,6) ) # True
    print( Pecahan(50,101)[2] ) # 101
    print( Pecahan(2,5) > Pecahan(4,5) ) # False
    print( Pecahan(3,7) >= Pecahan(1,7)*3 ) # True
    print( Pecahan(3,7)/3 == Pecahan(1,7) ) # True
    print( Pecahan(9,20)*Pecahan(20,9) ) # 180/180
    print( (Pecahan(9,20)*Pecahan(20,9)).reduce() ) # 1
    print( Pecahan(29,100003).reduce() ) # 29/100003
    print( Pecahan(2,3).__repr__() ) # Pecahan(2,3)
    #print( p1[0] ) # will generate exception ValueError

if __name__ == '__main__':
    main()