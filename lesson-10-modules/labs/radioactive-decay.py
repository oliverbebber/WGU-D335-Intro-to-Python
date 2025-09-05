# formula to calculate how much radioactive isotope with 
# half-life T will remain after time t is:
# N_{t}=N_{0}e^{\frac{-(\ln 2)t}{T}}

# formula can be rearranged to calculate the half-life of isotope 
# given how much remains after decay:
# T=\frac{-(\ln 2)t}{\ln{\frac{N_{t}}{N_{0}}}}

import math

# An isotope has half-life T.
# Return the amount of a starting mass N0
# of the isotope that remains after time t,
def compute_Nt(N0, t, T):
    # Type your code here.

# Return the half-life of an isotope given that
# a mass N0 decays to Nt after time t
def compute_T(N0, Nt, t):
    # Type your code here.

if __name__ == '__main__':
    choice = input()

    if choice == 'N':  # Calculate amount of material
        # TODO: Read N0, t, and T from one line of input and compute Nt
        
        print(f'Nt = {Nt:.4f}')
    elif choice == 'T':  # Calculate half-life
        # TODO: Read N0, Nt, and t from one line of input and compute T
        
        print(f'T = {T:.4f}')
    else:
        print("invalid choice")

