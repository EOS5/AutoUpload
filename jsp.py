import fitz  # PyMuPDF

# Create a new PDF document
doc = fitz.open()
page = doc.new_page(width=612, height=792)  # Letter size (612x792)

# Define the rectangle (100-point wide strip near the top-left)
rect = fitz.Rect(300, 70, 550, 200)

# Draw the rectangle (Red border, semi-transparent fill)
page.draw_rect(rect, color=(1, 0, 0), fill=(1, 0, 0, 0.3), width=2)

# Save the file
doc.save("rectangle_visual.pdf")
doc.close()

print("PDF created: rectangle_visual.pdf")