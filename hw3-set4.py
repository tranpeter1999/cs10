#Peter Tran
#1104985
#this program takes an inputted genome string and parses for genomes (start codons: ATG, stop codons: TAG, TAA, TGA)

def checkGenome(genome:str):
	i = 0
	genomesFound = 0
	while i < len(genome)-1:
		codon = genome[i-1:i+2]
		gene = ""
		
		if codon == "ATG": #start codon
			codon = ""
			while codon != "TAG" and codon != "TAA" and codon != "TGA" and codon != "ATG" and i < len(genome)-1:
				gene = gene + codon
				i = i + 3
				codon = genome[i-1:i+2]
				
			if codon == "TAG" or codon == "TAA" or codon == "TGA": #stop codon
				if len(gene) > 0:
					genomesFound = genomesFound + 1
					print(gene)
		else:
			i = i + 1
	
	if genomesFound == 0:
		print("No gene was found")
				
			
			
def main():
	userInput = 0
	while userInput != "-1":
		userInput = input("Enter a genome string (-1 to quit): ")
		
		if userInput == "-1":
			break
			
		checkGenome(userInput)
		print() #create space between inputs
	
	input("Press Enter to quit")
	
if __name__ == "__main__":
	main()
	
##run 1
##Enter a genome string (-1 to quit): TTATGTTTTAAGGATGGGGCGTTAGTT
##TTT
##GGGCGT
##
##Enter a genome string (-1 to quit): TGTGTGTATAT
##No gene was found
##
##Enter a genome string (-1 to quit): TGATGCTCTAAGGATGCGCCGTTGATT
##CTC
##CGCCGT
##
##Enter a genome string (-1 to quit): TGATGCTCTAGAGATGCGCCGTTGAATAT
##CTC
##CGCCGT
##
##Enter a genome string (-1 to quit): TGATGCGTCTAAGAGACTGCTCGCCGGTTGAATAT
##No gene was found
##
##Enter a genome string (-1 to quit): TGATGGCTCCTATGAGAATGGCGCCCGTTTCGAAATAT
##No gene was found
##
##Enter a genome string (-1 to quit): -1
##Press Enter to quit

##run 2
##Enter a genome string (-1 to quit): -1
##Press Enter to quit

##run 3
##Enter a genome string (-1 to quit): ATGCAGTCAGTACGAGCGTGGAGCTGATATGCAATGCTAGTAATTTAG
##CAGTCAGTACGAGCGTGGAGC
##CAATGC
##
##Enter a genome string (-1 to quit): GTTATGGCAATGCGATTATGA
##CGATTA
##
##Enter a genome string (-1 to quit): ATGGATACATAA
##GATACA
##
##Enter a genome string (-1 to quit): -1
##Press Enter to quit

##run 4
##Enter a genome string (-1 to quit): ATGATAA
##No gene was found
##
##Enter a genome string (-1 to quit): -1
##Press Enter to quit

##run 5
##Enter a genome string (-1 to quit): ATGGCGTAAATGTTATAG
##GCG
##TTA
##
##Enter a genome string (-1 to quit): TTATGT
##No gene was found
##
##Enter a genome string (-1 to quit): -1
##Press Enter to quit