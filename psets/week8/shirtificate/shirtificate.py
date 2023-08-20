from fpdf import FPDF
name = input("Name: ")
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_font("helvetica", size = 50)
pdf.add_page()
pdf.cell(30, 10, "CS50 Shirtificate")
pdf.image("shirtificate.png",x=0.2,y=70)
pdf.cell(-10, 230, f"{name} took CS50")
pdf.output("shirtificate.pdf")