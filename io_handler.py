import argparse
import PyPDF2
from tqdm import tqdm

# Create an argument parser
parser = argparse.ArgumentParser(description='Convert a PDF file to a text file')
parser.add_argument('pdf_path', metavar='PDF_PATH', type=str, help='the path to the PDF file')
args = parser.parse_args()

# Open the PDF file in read-binary mode
with open(args.pdf_path, 'rb') as pdf_file:
    
    # Create a PyPDF2 PdfReader object to read the PDF
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    # Get the number of pages in the PDF
    num_pages = len(pdf_reader.pages)
    
    # Create an empty string to store the text
    text = ''
    
    # Loop through each page in the PDF
    for page_num in tqdm(range(num_pages), desc="Extracting text"):
        
        # Get the page object
        page = pdf_reader.pages[page_num]
        
        # Extract the text from the page and add it to the string
        text += page.extract_text()
        
# Open a text file in write mode and write the extracted text to it
with open('output.txt', 'w', encoding='utf-8') as txt_file:
    txt_file.write(text)
