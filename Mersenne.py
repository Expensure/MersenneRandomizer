class PRNG_Mersenne:
    def __init__(self):
        # De coefficienten
        self.a = 0x9908b0df
        self.b = 0x9d2c5680
        self.c = 0xEFC60000
        self.f = 0x6c078965
        self.l = 18
        self.m = 397
        self.n = 624
        self.s = 7
        self.t = 15
        self.u = 11
        self.w = 32
        self.r = 31
        self.state = [0] * 624
        self.seed()
        self.index = 625
        self.lower_mask = 0xFFFFFFFF
        self.upper_mask = 0x00000000

    def seed(self, a=0):
        self.state[0] = a
        for i in range(1, self.n):
            temp = (
                    self.f * (self.state[i - 1] ^ (self.state[i - 1] >> (self.w - 2))) + i)
            self.state[i] = self.int_32(temp)

    def twister(self):
        for i in range(0, self.n):
            x = (self.state[i] & self.upper_mask) + \
                (self.state[(i + 1) % self.n] & self.lower_mask)
            xA = x >> 1
            if (x % 2) != 0:
                xA = xA ^ self.a
            self.state[i] = self.state[(i + self.m) % self.n] ^ xA
        self.index = 0

    def gen_random_int(self):
        # Genereert eem random integer getal
        if self.index >= self.n:
            self.twister()

        y = self.state[self.index]
        y = y ^ (y >> self.u)
        y = y ^ ((y << self.s) & self.b)
        y = y ^ ((y << self.t) & self.c)
        y = y ^ (y >> self.l)

        self.index += 1

        return self.int_32(y)

    def int_32(self, number):
        return int(number & 0xFFFFFFFF)

    def random(self):
        return self.gen_random_int() / 4294967296  # 0xFFFFFFFF + 1 regel toepassen

    def randrange(self, a, b):
        # Eigen versie van de vorm van random.py
        n = self.random()
        return int(n / (1 / (b - a)) + a)

    def randint(self, a, b):
        return self.randrange(a, b + 1)


with open('C:/Users/jaspe/Downloads/mersenneTest.txt', 'r+') as f:
    l = [int(x.strip()) for x in f]
rng = PRNG_Mersenne()