import pandas as pd

ideal_antigen = []
# Final antigen will be the ouput showing regions with B epitopes and MHC II epitopes


df1 = pd.read_excel('result.xlsx', sheet_name='bcelltool')
bepi = df1['Score'].tolist()
position = df1['Position'].tolist()
# Fetches scores into list bepi, fetches amino acid position


# can also index sheet by name or fetch all sheets
df2 = pd.read_excel('result.xlsx', sheet_name='tepitool')
mhc = df2['Peptide start'].tolist()
# Fetches position of MHC II peptide start points

num_peptide = len(bepi)
max_num = num_peptide - 40
bpeptide = []
# Will be used to calculate B cell epitope scores for antigens of 41 amino acids

score = 0
for x in position:
    score = 0
    if x <= max_num:
        for y in range(x, x+40):
            score += bepi[y]
        bpeptide.append(score/41)

bantigen = []
# Will be peptides with good scores

for a in bpeptide:
    if a > 0.6:
        bantigen.append(bpeptide.index(a))
# defines peptide start points with good B cell eptiopes


for z in mhc:
    for x in bantigen:
        for a in range(x, x+25):
            if z == a:
                ideal_antigen.append(x)
# Selects MHC II antigens from B antigens

print(str(ideal_antigen))
# Prints the start points of peptides with B and MHC II epitopes
