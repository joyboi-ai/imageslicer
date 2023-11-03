# def extract(file):
#     import fitz # PyMuPDF
#     import file_Extention as fe
#     pdf_document = file
#     # print(fe.file_Extention(pdf_document))
#     pdf_document = fitz.open(pdf_document)

#     for page_num in range(pdf_document.page_count):
#         page = pdf_document[page_num]
#         image_list = page.get_images(full=True)

#         for img_index, img in enumerate(image_list):
#             xref = img[0]
#             base_image = pdf_document.extract_image(xref)
#             image_data = base_image["image"]

#             with open(f"image{img_index}.png", "wb") as image_file:
#                 image_file.write(image_data)


import os as os
def extract(file):
    import fitz # PyMuPDF
    import file_Extention as fe
    pdf_document = file
    loc="temp_img"  # specify your directory here
    # print(fe.file_Extention(pdf_document))
    pdf_document = fitz.open(pdf_document)

    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        image_list = page.get_images(full=True)

        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_data = base_image["image"]

            with open(f"{loc}/image{img_index}.png", "wb") as image_file:
                image_file.write(image_data)


def count_images(directory):
    # List all files in the directory
    files = os.listdir(directory)
    
    # Filter the list to only include .jpg, .jpeg, .png, and .gif files
    image_files = [file for file in files if file.endswith(('.jpg', '.jpeg', '.png', '.gif','.docx'))]
    
    # Return the number of image files
    return len(image_files)