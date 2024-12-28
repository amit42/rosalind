'''
https://rosalind.info/problems/rna/
'''

if __name__ == "__main__":
    with open("data/rosalind_rna.txt","r") as f:
        dna = f.read().rstrip()
        rna = dna.replace('T','U')
        print(rna)
