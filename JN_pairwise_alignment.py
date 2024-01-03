from Bio import pairwise2
from Bio import SeqIO
from Bio.Align import substitution_matrices

blosum62 = substitution_matrices.load("BLOSUM62")

seq1 = SeqIO.read("seq1.txt", "fasta")
seq2 = SeqIO.read("seq2.txt", "fasta")

alignments = pairwise2.align.globalds(seq1.seq, seq2.seq, blosum62, -10, -0.5)
len(alignments)

print(pairwise2.format_alignment(*alignments[0]))

