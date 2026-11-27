import os
import smtplib
from pathlib import Path
from email.message import EmailMessage
from email.utils import parseaddr
from typing import Optional

from dotenv import load_dotenv
from fastapi import APIRouter, UploadFile, File, Form, HTTPException

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

router = APIRouter(
    prefix="/email",
    tags=["Email Delivery"]
)


@router.post("/send-pdf")
def send_pdf_email(
    recipients: str = Form(...),
    pdf: UploadFile = File(...),
    teacher_name: Optional[str] = Form(None),
    lecture_title: Optional[str] = Form(None)
):
    sender = os.getenv("SMTP_EMAIL")
    app_password = os.getenv("SMTP_APP_PASSWORD")

    if not sender or not app_password:
        raise HTTPException(
            status_code=500,
            detail="Gmail SMTP credentials are not configured in backend/.env"
        )

    student_emails = list(dict.fromkeys(
        email.strip() for email in recipients.split(",") if email.strip()
    ))

    if not student_emails:
        raise HTTPException(
            status_code=400,
            detail="No recipient email provided"
        )

    for address in student_emails:
        if parseaddr(address)[1] != address or "@" not in address:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid email address: {address}"
            )

    if not pdf.filename or not pdf.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Please upload a PDF file"
        )

    pdf_content = pdf.file.read()

    if not pdf_content.startswith(b"%PDF"):
        raise HTTPException(
            status_code=400,
            detail="Uploaded file is not a valid PDF"
        )

    if len(pdf_content) > 15 * 1024 * 1024:
        raise HTTPException(
            status_code=400,
            detail="PDF size must be below 15 MB"
        )

    subject_title = (lecture_title.strip() if lecture_title and lecture_title.strip() else "Lecture Notes")
    teacher_display = (teacher_name.strip() if teacher_name and teacher_name.strip() else "Teacher")

    message = EmailMessage()
    message["Subject"] = f"ClassNote AI - {subject_title}"
    message["From"] = f"{teacher_display} (via ClassNote AI) <{sender}>"
    message["To"] = student_emails[0]

    # Remaining selected students receive the email in CC (as required by workflow)
    if len(student_emails) > 1:
        message["Cc"] = ", ".join(student_emails[1:])

    message.set_content(
        f"Dear Student,\n\n"
        f"Please find attached the official lecture notes, key concepts, and FAQs for "
        f"\"{subject_title}\", generated and verified using ClassNote AI.\n\n"
        f"Review these notes thoroughly for your examination preparation.\n\n"
        f"Regards,\n"
        f"{teacher_display}\n"
        f"ClassNote AI Educational Platform"
    )

    message.add_attachment(
        pdf_content,
        maintype="application",
        subtype="pdf",
        filename=pdf.filename
    )

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=30) as smtp:
            smtp.login(sender, app_password)
            smtp.send_message(message)

        return {
            "status": "success",
            "message": f"Lecture PDF successfully delivered to {len(student_emails)} students",
            "total_recipients": len(student_emails),
            "primary_recipient": student_emails[0],
            "cc_recipients": student_emails[1:] if len(student_emails) > 1 else [],
            "lecture_title": subject_title,
            "teacher_name": teacher_display
        }

    except smtplib.SMTPAuthenticationError:
        raise HTTPException(
            status_code=401,
            detail="Gmail authentication failed. Please verify SMTP_EMAIL and SMTP_APP_PASSWORD in backend/.env"
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Email delivery failed: {str(e)}"
        )
