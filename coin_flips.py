# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨`

# This function returns an array of all possible outcomes from flipping a coin N times.
# Input type: Integer
# H stands for Heads and T stands for tails
# Represent the two outcomes of each flip as "H" or "T"
flips = []


def coin_flips(n):
    if n == 1:
        flips[-n] = 'T'
        ''.join(flips)
        flips[-n] = 'H'
        ''.join(flips)
    else:
        flips[-n] = 'T'
        coin_flips(n-1)
        flips[-n] = 'H'
        coin_flips(n-1)


print(coin_flips(2))
# => ["HH", "HT", "TH", "TT"]
