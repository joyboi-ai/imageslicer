from PIL import Image
import os
import fnmatch

def get_Path(folder_path):
    image_formats = ['*.jpg', '*.jpeg', '*.png', '*.gif', '*.bmp']
    image_paths = []

    for format in image_formats:
        for root, dir, files in os.walk(folder_path):
            for file in fnmatch.filter(files, format):
                image_paths.append(os.path.join(root, file))

    return image_paths

def img2pdf(image_files:list[str],pdf_file:str)->None:
    if not image_files:
        print("No image files provided")
        return
    image_obj = [Image.open(image).convert("RGB") for image in image_files]
    image_obj[0].save(pdf_file, save_all=True, append_images=image_obj[1:])


# print(get_Path('temp_img'))
# print(type(get_Path('temp_img')))
img2pdf(get_Path('temp_img'),'image_slicer.pdf')