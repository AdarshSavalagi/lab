import PyPDF2

def combine_select_pages(pdf_files, page_numbers, output_file):
    writer = PyPDF2.PdfWriter()

    for file in pdf_files:
        with open(file, 'rb') as pdf:
            reader = PyPDF2.PdfReader(pdf)
            for page_num in page_numbers:
                page = reader.pages[page_num - 1]  # Page numbers start from 0
                writer.add_page(page)

    with open(output_file, 'wb') as output:
        writer.write(output)

    print("Combined PDF created successfully.")

# Test the program
pdf_files = ["file1.pdf", "file2.pdf"]
page_numbers = [1, 2]  # Example page numbers
output_file = "combined_pages.pdf"

combine_select_pages(pdf_files, page_numbers, output_file)
