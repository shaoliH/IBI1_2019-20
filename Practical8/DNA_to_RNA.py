seq = 'ATGCGACTACGATCGAGGGCCAT'

RNA_seq = ""
Transcription_dic = {"A": "U", "C": "G", "G": "C", "T": "A"}

for i in seq:
    RNA_seq += Transcription_dic[i]

print(RNA_seq)