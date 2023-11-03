#ui of the software 

import tkinter as tk
import os
import shutil
import subprocess
from tkinter import filedialog,messagebox
from PIL import Image, ImageTk
import webbrowser
import ttkbootstrap as ttk
from extractor import extract
import img_to_pdf as i2p

# # theme=return_theme()
# selected_theme="morph"
result=''

def change_theme(event):
    selected_theme = event.widget.get()
    thm=f"Theme:{selected_theme}"
    ttk.Style().theme_use(selected_theme)

def show_list(event):
    event.widget.state(["readonly"])
    event.widget.state(["!readonly"])

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf"), ("Word files", "*.docx"), ("Excel files", "*.xlsx"), ("PowerPoint files", "*.pptx"), ("Word files ","*.word")])


    try:
        extract(file_path)
    except Exception as e:
        result = 'Incorrect file type is opened !!!'
        print(result)
    else:
        result = f"File opened: {file_path}"
        print(result)
        # Update the label text with the result
        label_text.set(result)
        # Show the label
        label.place(x=240,y=200,relheight=0.11,relwidth=0.51,anchor="center")
        label_opened_file.place(x=200,y=160,anchor='center')
        edit_button.place(x=240,y=280,anchor='center',relheight=0.11,relwidth=0.41)
        save_button.place(x=240,y=340,relheight=0.11,relwidth=0.41,anchor="center")
        
    
    

def open_github():
    webbrowser.open('GITHUB LINK')

#displaying images 
def display_images(folder, master):
    
    # Create a new window as a child of master
    window = tk.Toplevel(master)
    window.title("Image Viewer")
    window.geometry('600x600')
    style = ttk.Style(theme="darkly")
    # Create a frame to hold the images and the scroll bar
    frame = ttk.Frame(window)
    frame.pack(fill="both", expand=True)
    # Create a canvas to display the images
    canvas = tk.Canvas(frame, bg="black")
    canvas.pack(side="left", fill="both", expand=True)
    # Create a scroll bar to scroll through the images
    scroll = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scroll.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scroll.set)
    # Create another frame to hold the image widgets
    image_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=image_frame, anchor="nw")
    # Get the list of image files from the folder
    image_files = [f for f in os.listdir(folder) if f.endswith((".jpg", ".png", ".gif"))]
    # Loop through the image files and create image widgets
    for i, file in enumerate(image_files):
        # Load the image using PIL
        image = Image.open(os.path.join(folder, file))
        # Resize the image to fit the window
        width, height = image.size
        ratio = min(400 / width, 300 / height)
        width = int(width * ratio)
        height = int(height * ratio)
        image = image.resize((width, height))
        # Convert the image to Tkinter format
        photo = ImageTk.PhotoImage(image)
        # Create a label to display the image
        label = ttk.Label(image_frame, image=photo)
        label.image = photo # keep a reference to avoid garbage collection
        label.grid(row=i, column=0, padx=10, pady=10)
        # Create a button to save the image
        save_button = ttk.Button(image_frame, text="Save", style="success.Outline.TButton",
                                 command=lambda f=file: save_image(f, folder))
        save_button.grid(row=i, column=1, padx=10, pady=10)
        # Create a button to discard the image
        discard_button = ttk.Button(image_frame, text="Discard", style="danger.Outline.TButton",
                                    command=lambda l=label, f=file: discard_image(l, f, folder))
        discard_button.grid(row=i, column=2, padx=10, pady=10)
    # Update the canvas scroll region
    window.update()
    canvas.config(scrollregion=canvas.bbox("all"))
    

# Define a helper function to save the image to another directory
def save_image(file, source_dir):
    # Specify the target directory where you want to save the images
    target_dir = "saved_images"
    # Create the target directory if it does not exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    # Copy the file from source directory to target directory
    os.system(f"copy {os.path.join(source_dir, file)} {os.path.join(target_dir, file)}")
    

# Define a helper function to discard the image from the display and delete it from the folder
def discard_image(label, file, folder):
    # Destroy the label widget
    label.destroy()
    # Delete the file from the folder
    os.remove(os.path.join(folder, file))
    
def display_message():
    messagebox.showinfo("Image Slicer-help",'''
    Step 1) click on open file
            ,after opening the file the path of the file would be showned.
    Step 2)Then automatically the images would be cropped from the pdf.
    Step 3)then click on edit iamges and select which images you want to save and which you want to discard .
    Step 4)After editing all the images click on open pdf button to see the pdf .''')
                        
def delete_folder_content(folder):
    # loop through all the files and subfolders in the folder
    for item in os.listdir(folder):
        # get the full path of the item
        item_path = os.path.join(folder, item)
        # if the item is a file or a symbolic link, delete it
        if os.path.isfile(item_path) or os.path.islink(item_path):
            os.remove(item_path)
        # if the item is a subfolder, delete it and all its contents recursively
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)


def open_pdf():
    path = "files\image_slicer.pdf" # change this to your PDF file path
    subprocess.Popen([path], shell=True) # this will open the PDF file in the default viewer

def both_Functioncalled():
    open_pdf()
    i2p.img2pdf(i2p.get_Path('saved_images'),'files\image_slicer.pdf')



    
window = ttk.Window(themename="darkly")
window.geometry("470x368")
window.minsize(450,420)
window.title("Image slicer")

applogo = Image.open("icons/applogo.jpg")
applogo = ImageTk.PhotoImage(applogo)
window.iconphoto(False, applogo)

# Load an image file for GitHub
github_img = Image.open("icons\github_icon.png")
github_img = github_img.resize((20, 15))  # Resize image
github_img = ImageTk.PhotoImage(github_img)

# Create buttons
icon_aboutus=Image.open("icons\icon.png") #getting user icon 
icon_aboutus=icon_aboutus.resize((20,15))
icon_aboutus = ImageTk.PhotoImage(icon_aboutus)

user = ttk.Button(window, text="About", compound="left",style='info.Outline.TButton',image=icon_aboutus)
user.grid(row=0,column=0)
#open file
open_icon=Image.open("icons\openfile.png") #getting user icon 
open_icon=open_icon.resize((20,15))
open_icon = ImageTk.PhotoImage(open_icon)
open_button = ttk.Button(window, text="Open", command=open_file,compound="left", style='info.Outline.TButton',image=open_icon)
open_button.grid(row=0,column=1)
#edit
edit_icon=Image.open("icons\editicon.png") #getting user icon 
edit_icon=edit_icon.resize((20,15))
edit_icon = ImageTk.PhotoImage(edit_icon)
edit_button = ttk.Button(window, text="Edit", compound="left",style='info.Outline.TButton',image=edit_icon)
edit_button.grid(row=0,column=2)
#help
help_icon=Image.open("icons\qm.png") #getting user icon 
help_icon=help_icon.resize((20,15))
help_icon = ImageTk.PhotoImage(help_icon)
help_button = ttk.Button(window, text="Help", compound="left",style='info.Outline.TButton',image=help_icon,command=display_message)
help_button.grid(row=0,column=3)


#theme button 
themes = ["darkly", "cyborg", "superhero", "morph", "yeti","united","journal"]
selected_theme = tk.StringVar(value=themes[0])
theme_combobox = ttk.Combobox(window, values=themes,textvariable=selected_theme,style='info.Outline.TButton')
theme_combobox.bind("<<ComboboxSelected>>", change_theme)
theme_combobox.bind("<<ComboboxFocusIn>>", show_list)
theme_combobox.grid(column=5,row=0)

# Add GitH  ub button to the right
github_button = ttk.Button(window, text="GitHub", image=github_img, compound="left", command=open_github, style='primary.Outline.TButton',)
github_button.place(x=380,y=0)

#creating a new style for button 
style1 = ttk.Style()
style1.configure('TButton', font=('calibri', 10, 'bold'), borderwidth='4')



label0 = ttk.Label(window,text="Start slicing an image fom Documents by clicking the button below .",font='askthetik',justify='left',)
label0.place(x=0,y=60,)

openfile_button = ttk.Button(window, text="Select File", command=open_file, style='info.Outline.TButton')
openfile_button.place(x=240,y=120,relheight=0.11,relwidth=0.41,anchor="center")


label_opened_file = ttk.Label(window,text="You Opened  the following file path .",font='askthetik',justify='left',)
label_opened_file.place(x=200,y=160,)
label_opened_file.place_forget()


label_text = tk.StringVar()
# Create a label with the same style as the button
label = ttk.Label(window,text=result, textvariable=label_text, style='TButton')
# Initially hide the label
label.place_forget()



#edit pdf button


edit_button = ttk.Button(window, text="Edit images", command=lambda:display_images('temp_img',window))
edit_button.place_forget()

#save button
save_button = ttk.Button(window, text="Open pdf", command=both_Functioncalled, style='success.Outline.TButton')
save_button.place_forget()



window.mainloop()
#removing temporary directories
delete_folder_content('temp_img')
delete_folder_content('saved_images')



