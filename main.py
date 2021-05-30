from PIL import Image
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import filedialog as fd



#TODO: Create a GUI
root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=600)
canvas.grid(columnspan=3, rowspan=3)

#TODO: BROWSE BUTTON

# def open_file1():
#     file1 = fd.askopenfilename()
#     print(file1)
#
# def open_file_2():
#     file2 = fd.askopenfilename()
#     print(file2)

# def save_file():
#     file = fd.asksaveasfilename(initialdir="C:\\Users\\user\\PycharmProjects\\pythonProject\\watermark",
#                                 defaultextension='.jpg',
#                                 filetypes=[("All Files", ".*")])

# #Browse Orginal Image
# browse_text = tk.StringVar()
# browse_btn = tk.Button(root, textvariable=browse_text, command=open_file1, font="Raleway", bg='#20bebe', fg="white", height=5, width=20)
# browse_text.set("Browse Original Image")
# browse_btn.grid(column=1, row=0)
#
# #Browse Watermark Image
# browse_text = tk.StringVar()
# browse_btn = tk.Button(root, textvariable=browse_text, command=open_file_2, font="Raleway", bg='#20bebe', fg="white", height=2, width=20)
# browse_text.set("Browse Watermark Image")
# browse_btn.grid(column=1, row=1)




def watermark_photo(input_image, output_image, watermark_image, position):
    base_image = Image.open(input_image)
    watermark = Image.open(watermark_image)

    base_image.paste(watermark, position, mask=watermark)
    base_image.show()
    base_image.save(output_image)

if __name__ == '__main__':
    img_original = fd.askopenfilename()
    img_watermark = fd.askopenfilename()

def Output():
    watermark_photo(img_original, 'output.jpg', img_watermark, position=(0, 0))


#Browse Output
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=Output, font="Raleway", bg='#20bebe', fg="white", height=2, width=20)
browse_text.set("Output")
browse_btn.grid(column=1, row=1)


root.mainloop()