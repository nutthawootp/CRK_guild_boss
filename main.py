import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk  # Using ImageTk for displaying images
import pytesseract


# ฟังก์ชั่นสำหรับเปิดไฟล์รูปภาพ
def open_image():
    global image_path
    # image_path = tk.filedialog.askopenfilename(title="Select an image", filetypes=[("Image files", "*.jpg *.png *.jpeg")])
    app.sourceFile = tk.filedialog.askopenfilename(
        parent=app,
        initialdir="/",
        title="Select an image",
        filetypes=[("Image files", "*.jpg *.png *.jpeg")],
    )
    image_path = app.sourceFile
    if image_path:
        image = Image.open(image_path)
        image.show()


# Function to update the image placeholder
def update_image_placeholder():
    if image_path:
        image = Image.open(image_path)
        image = image.resize((200, 200))  # Adjust size as needed
        photo = ImageTk.PhotoImage(image)
        image_label.configure(image=photo)
        image_label.image = photo  # Keep a reference for garbage collection


# ฟังก์ชั่นสำหรับ Extract ข้อความ
def extract_text():
    if image_path:
        text = pytesseract.image_to_string(Image.open(image_path))
        text_entry.delete(0, tk.END)
        text_entry.insert(0, text)


# ฟังก์ชั่นสำหรับ copy ข้อความ
def copy_text():
    text = text_entry.get()
    app.clipboard_append(text)


# หน้าต่าง GUI
app = tk.Tk()
app.title("Extract ข้อความและตัวเลข จากรูปภาพ")
app.geometry("800x500+0+0")


# ปุ่มเปิดไฟล์รูปภาพ
open_image_button = tk.Button(app, text="Open Image", command=open_image)
# Bind open_image_button to update the image placeholder
open_image_button.configure(command=lambda: [open_image(), update_image_placeholder()])
open_image_button.pack()

# Image placeholder label
image_label = tk.Label(app, width=200, height=200, borderwidth=1, relief="solid")
image_label.pack()


# ช่องข้อความ
text_entry = tk.Entry(app, width=150)
text_entry.pack()

# ปุ่ม Extract ข้อความ
extract_text_button = tk.Button(app, text="Extract Text", command=extract_text)
extract_text_button.pack()

# ปุ่ม copy ข้อความ
copy_text_button = tk.Button(app, text="Copy Text", command=copy_text)
copy_text_button.pack()

# รันโปรแกรม
app.mainloop()
