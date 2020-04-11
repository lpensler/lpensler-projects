"""
Leah Pensler
Protein Synthesis Final Project
COMP-112-01
05/03/17
"""


def import_DNA (path):
    try:
        f = open(path, 'r')
        sequence = ''
        for line in f:
            sequence += line
        f.close()
        return sequence
    except FileNotFoundError:
        return -1




def verify_DNA(sequence): #this is where the DNA sequence is input from the path
    for x in sequence:
        if x != 'A' and x != 'T' and x != 'C' and  x!= 'G':
            return False 
    return True 
    

def RNA_complement(sequence): #this is where the DNA sequence is turned into the RNA Complement
    if verify_DNA(sequence) == True:
        acc = ''
        i = 0
        while i < len(sequence):
            if sequence[i] =='A':
                acc += ('U') 
            if sequence[i] == 'T':
                acc += ('A')
            if sequence[i] == 'C':
                acc += ('G')
            if sequence[i]== 'G':
                acc += ('C')
            i+=1
        return acc
        
       

def find_start_codon(sequence): #This is where it inputs the RNA sequence to find the start codon, or the first place after where AUG appears in the sequence  
    i = 0
    while i<len(sequence) - 3 :
        if sequence[i:i+3] == 'AUG':
            return i+3 
        i += 1
    return -1

    

#below is the dictionary for the amino acids translated from the RNA sequence 
        
aminoacids = { 'UUU' : 'Phenylalanine' , 'UUC' : 'Phenylalanine', 'UUA' : 'Leucine' , 'UUG': 'Leucine' , 
               'CUU': 'Leucine' , 'CUC': 'Leucine' , 'CUA':'Leucine' , 'CUG':'Leucine' , 'AUU':'Isoleucine', 
               'AUC':'Isoleucine', 'AUA':'Isoleucine', 'AUG':'Methionine', 'GUU':'Valine', 'GUC':'Valine', 'GUA':'Valine',
               'GUG':'Valine', 'UCU':'Serine', 'UCC': 'Serine', 'UCA':'Serine', 'UCG':'Serine', 'CCU':'Proline','CCC':'Proline',
               'CCA':'Proline', 'CCG':'Proline', 'ACU':'Threonine', 'ACC':'Threonine', 'ACA':'Threonine', 'ACG':'Threonine',
               'GCU':'Alanine' , 'GCC':'Alanine' , 'GCA':'Alanine', 'GCG':'Alanine' , 'UAU':'Tyrosine', 'UAC':'Tyrosine',
               'UAA':'Stop', 'UAG':'Stop', 'CAU':'Histidine' , 'CAC':'Histidine', 'CAA':'Glutamine', 'CAG':'Glutamine',
               'AAU':'Asparagine', 'AAC':'Asparagine', 'AAA':'Lysine', 'AAG':'Lysine', 'GAU':'Aspartic acid' ,
               'GAC': 'Aspartic acid', 'GAA':'Glutamic acid', 'GAG':'Glutamic Acid', 'UGU':'Cysteine', 'UGC':'Cysteine',
               'UGA':'Stop','UGG':'Tryptophan','CGU':'Arginine', 'CGC':'Arginine', 'CGA':'Arginine', 'CGG':'Arginine',
               'AGU':'Serine', 'AGC':'Serine', 'AGA':'Arginine', 'AGG':'Arginine', 'GGU':'Glycine','GGC':'Glycine','GGA':'Glycine',
               'GGG':'Glycine'
               }

def build_protein(sequence, i): #Here the RNA sequence and the value after the start codon are the two arguments to find the sequence of amino acids 
    acc = ''
    while i < len (sequence):
        code = sequence[i:i+3]
        if sequence[i:i+3] in aminoacids:
            acid = aminoacids[code]
            if acid == 'Stop':
                return acc[:-1]
            acc = acc + aminoacids[sequence[i:i+3]] + ', '
        i += 3
    return acc[:-1]




            
def DNA_to_protein(path): #this combines all the functions to return a string of amino acids in the sequence  
    sequence = import_DNA(path)
    if(sequence == -1): #this is to check if FileNotFoundError
         print ('Please enter a valid File')
    elif(verify_DNA(sequence) == True):
        x = find_start_codon(RNA_complement(sequence))
        if x != -1:
            new_sequence = RNA_complement(sequence)
            return 'Amino acids: ' + build_protein(new_sequence, x) 
        if x == -1:
            print ('This DNA sequence does not have a start codon. Please enter a DNA sequence with a start codon and try again') #This is if the DNA sequence is valid but has no start codon
    elif(verify_DNA(sequence) == False):
        print ('DNA sequence invalid. Please enter a valid DNA sequence and try again') # this will return if the file doesn't contain a valid DNA sequence 

         

