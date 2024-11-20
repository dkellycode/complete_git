import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image


def converter():
    """Basic conversion tool for images."""
    target_image_paths = fd.askopenfilenames()
    piccount = 1
    convert_type = input("Enter the desired format (e.g., JPEG, PNG): ").replace("jpg","jpeg")
    for img_path in target_image_paths:
        target_img = Image.open(img_path)
        img_name = img_path.split('/')[-1]
        print(f'{img_name} is being converted to {convert_type.upper()}\n')
        
        # Convert to RGB mode if saving as JPEG
        if convert_type.upper() in ['JPEG', 'JPG']:
            target_img = target_img.convert('RGB')
        else:
            target_img = target_img.convert('RGBA')
            
        target_img.save(f'/Users/d3ops/Documents/converted_{img_name}.{convert_type.lower()}', convert_type.upper())
        piccount += 1
 

def basicesizer():
    """Basic resizing tool for square images."""
    target_img_paths = (fd.askopenfilenames())

    new_pxl_val  = int(input("Enter the new pixel value: "))
    save_format = str(input("Enter the desired format (e.g., JPEG, PNG): ")).replace("jpg","jpeg")

    for img_path in target_img_paths:
        target_img = Image.open(img_path)
        img_name = img_path.split('/')[-1]
        imgwidth = target_img.size[0]
        imgheight = target_img.size[1]
        print(f'img_width = {imgwidth}')
        print(f'img_height = {imgheight}')

        if imgheight == imgwidth:
            target_img.resize((new_pxl_val, new_pxl_val)).save(f'/Users/d3ops/Documents/resized_{img_name}.{save_format.lower()}', f'{save_format.upper()}')
            print(f'{img_name} is being resized to {save_format.upper()}\n')
        else:
            print(f'{img_name} is not square, please use advanced image rescaler\n')



def advancedsizer():
    """Advanced resizing tool for non-square images."""
    target_img_paths = (fd.askopenfilenames())

    new_pxl_val = int(input("Enter the maximum pixel value for the longest axis: "))
    save_format = str(input("Enter the desired format (e.g., JPEG, PNG): ")).replace("jpg","jpeg")

    for img_path in target_img_paths:
        target_img = Image.open(img_path)
        img_name = img_path.split('/')[-1].split('.')[0]
        imgwidth = target_img.size[0]
        imgheight = target_img.size[1]
        print(f'{img_name} img_width = {imgwidth}')
        print(f'{img_name} img_height = {imgheight}')

        if imgheight == imgwidth: 
            if save_format.upper() == 'JPEG' or save_format.upper() == 'JPG':
                target_img = target_img.convert('RGB')
            print(f'{img_name} is being resized to {save_format.upper()}\n')
            target_img.resize((new_pxl_val, new_pxl_val)).save(f'/Users/d3ops/Documents/resized_{img_name}.{save_format.lower()}', f'{save_format.upper()}')
        else:
            newratio = new_pxl_val/max(imgheight, imgwidth)
            resize_img = target_img.resize((int(imgwidth * newratio), int(imgheight * newratio)), Image.Resampling.LANCZOS).convert("RGBA")
            new_image = Image.new("RGBA", (new_pxl_val, new_pxl_val), (0, 0, 0, 0))
            x = (new_pxl_val - resize_img.width) // 2
            y = (new_pxl_val - resize_img.height) // 2
            new_image.paste(resize_img, (x, y))
            if save_format.upper() == 'JPEG' or save_format.upper() == 'JPG':
                new_image = new_image.convert('RGB')
            print(f'{img_name} is being resized to {save_format.upper()}\n')
            new_image.save(f'/Users/d3ops/Documents/resized_{img_name}.'+f'{save_format.lower()}', f'{save_format.upper()}')


def main():
    root = tk.Tk()
    root.title("Image Resizer Tool")
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    window_width = 300
    window_height = 200
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    label = tk.Label(root, text="Select a function to run:")
    label.pack(pady=10)

    def run_basic():
        root.destroy()
        basicesizer()

    def run_advanced():
        root.destroy()
        advancedsizer()

    def run_converter():
        root.destroy()
        converter()

    basic_button = tk.Button(root, text="Converter", command=run_converter, background="#ff6600")
    basic_button.pack(pady=5)

    basic_button = tk.Button(root, text="Basic Resizer", command=run_basic, background="#ff6600")
    basic_button.pack(pady=5)

    advanced_button = tk.Button(root, text="Advanced Resizer", command=run_advanced)
    advanced_button.pack(pady=5)

    root.mainloop()

main()
