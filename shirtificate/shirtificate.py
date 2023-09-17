from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image("shirtificate.png", 10, 74, 190)
        self.set_font("helvetica", "", 48)
        self.cell(0, 57, "CS50 Shirtificate", align="C")
        self.ln(20)

def main():
    name = input("Name: ")
    pdf = PDF(orientation="P", format="A4")
    pdf.add_page()
    pdf.set_auto_page_break(auto=False, margin=0)
    pdf.set_font("helvetica", size=24)
    pdf.set_text_color(255,255,255)
    pdf.cell(0, 180, f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()