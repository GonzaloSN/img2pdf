from fpdf import FPDF

pdf = FPDF(orientation = 'P', unit = 'mm', format='A4')

imagelist = ["./Assets/img1.png", "./Assets/img2.png"]
for image in imagelist:
    pdf.add_page()
    pdf.image(image, x=0, y=0, w=210, h=297)
pdf.output("output.pdf", "F")