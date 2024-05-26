from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle

def create_receipt(user_data):
    # Create a PDF file
    pdf_file = "Payment_Receipt.pdf"
    pdf = SimpleDocTemplate(pdf_file, pagesize=letter)

    # Create a sample stylesheet
    styles = getSampleStyleSheet()

    # Add custom styles with unique names
    styles.add(ParagraphStyle(name='CustomTitle', fontSize=24, alignment=TA_CENTER, spaceAfter=20))
    styles.add(ParagraphStyle(name='CustomHeading', fontSize=18, spaceAfter=10))
    styles.add(ParagraphStyle(name='CustomBodyText', fontSize=12, spaceAfter=8))

    # Create a list to hold the elements to be added to the PDF
    elements = []

    # Add title
    title = Paragraph("Payment Receipt", styles['CustomTitle'])
    elements.append(title)

    # Add user details
    user_details = f"""
    <b>Name:</b> {user_data['name']}<br/>
    <b>Email:</b> {user_data['email']}<br/>
    <b>Amount Paid:</b> Rs.{user_data['amount']}<br/>
    <b>Date:</b> {user_data['date']}
    """
    user_paragraph = Paragraph(user_details, styles['CustomBodyText'])
    elements.append(user_paragraph)

    # Add a table with the payment details
    data = [
        ["Item", "Description", "Amount"],
        ["Tuition", "Tuition fee for the semester", "Rs.5400"],
        ["Books", "Textbooks for courses", "Rs.560"],
        ["Lab Fees", "Fees for lab usage", "Rs.350"],
        ["Total", "", "Rs.6310"]
    ]

    table = Table(data, colWidths=[100, 300, 100])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)

    # Add a thank you note
    thank_you_note = Paragraph("Thank you for your payment!", styles['CustomHeading'])
    elements.append(thank_you_note)

    # Build the PDF
    pdf.build(elements)
    print(f"PDF created: {pdf_file}")

# User data
user_data = {
    'name': 'Sreemoyee Dutta',
    'email': 'sreemoyee.dutta@xyz.com',
    'amount': '6310',
    'date': '2024-05-26'
}

# Create the receipt
create_receipt(user_data)
