########################################
#### Cash4Life Data Convert File #######
########################################


########################################
# file last updated 2025/05/04
# pdf file is gathered from-
# https://floridalottery.com/games/draw-games/cash4life
########################################

#imports 
import pdfplumber 
import csv

# Paths to input PDF and output CSV
pdf_path = r"PDF\c4l_5-3.pdf" #change this input to your file name after site pdf download
csv_path = r"CSV\c4l_5-3.csv" 

# Extract tables from PDF and write to CSV
with pdfplumber.open(pdf_path) as pdf, open(csv_path, "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            for row in table:
                writer.writerow(row)   