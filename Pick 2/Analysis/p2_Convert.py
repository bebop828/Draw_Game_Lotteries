#######################################################
############## PICK 2 with FIREBALL ###################
################## Convert File #######################
#######################################################


#######################################################
# last update- 2025/05/04 
# pdf file is gathered from-
# https://floridalottery.com/games/draw-games/pick-2
#######################################################

#imports
import pdfplumber
import csv

# Paths to input PDF and output CSV
pdf_path = 'PDF/p2.pdf' 
csv_path = 'CSV/pick2.csv'

# Extract tables from PDF and write to CSV
with pdfplumber.open(pdf_path) as pdf, open(csv_path, "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            for row in table:
                writer.writerow(row)