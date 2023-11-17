import tkinter as tk
from tkinter import ttk, messagebox
import qrcode
import png
from PIL import Image, ImageTk

class QRCodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("URL QR Code Generator")

        # URL Entry
        ttk.Label(root, text="Enter URL:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.url_entry = ttk.Entry(root, width=40)
        self.url_entry.grid(row=0, column=1, padx=10, pady=10)

        # Generate Button
        generate_button = ttk.Button(root, text="Generate QR Code", command=self.generate_qr_code)
        generate_button.grid(row=1, column=0, columnspan=2, pady=10)

        # QR Code Canvas
        ttk.Label(root, text="QR Code:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.qr_canvas = tk.Canvas(root, width=200, height=200)
        self.qr_canvas.grid(row=2, column=1, padx=10, pady=10)

    def generate_qr_code(self):
        # Get URL from the entry
        url = self.url_entry.get()

        if url:
            # Generate QR code
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            qr.add_data(url)
            qr.make(fit=True)

            qr_img = qr.make_image(fill_color="black", back_color="white")

            # Display the QR code on the canvas
            self.display_qr_code(qr_img)
        else:
            # Show an error message if no URL is provided
            messagebox.showerror("Error", "Please enter a URL to generate a QR code.")

    def display_qr_code(self, img):
        # Convert the QR code image to PhotoImage format
        qr_img = ImageTk.PhotoImage(img)

        # Update the canvas with the new QR code image
        self.qr_canvas.config(width=qr_img.width(), height=qr_img.height())
        self.qr_canvas.create_image(0, 0, anchor=tk.NW, image=qr_img)
        self.qr_canvas.image = qr_img

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()
