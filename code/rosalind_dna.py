"""
https://rosalind.info/problems/dna/
"""

neucleotides = ['A','C','G','T']

def neucleotides_count(dna):
    for neucleotide in neucleotides:
        print (dna.count(neucleotide),end=" ")
    print("\n")

if __name__ == "__main__":
    with open("data/rosalind_dna.txt","r") as f:
        dna = f.read().rstrip()
        neucleotides_count(dna)

