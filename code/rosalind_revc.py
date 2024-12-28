'''
https://rosalind.info/problems/revc/
'''

def complement(sym):
    if sym == 'A':
        return 'T'
    elif sym == 'C':
        return 'G'
    elif sym == 'G':
        return 'C'
    elif sym == 'T':
        return 'A'
    return ''

if __name__ == "__main__":
    with open("data/rosalind_revc.txt","r") as f:
        dna = f.read().rstrip()
        dna_complemented = [complement(sym) for sym in dna[-1::-1]]
        print(''.join(dna_complemented))

