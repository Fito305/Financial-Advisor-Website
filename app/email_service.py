from __future__ import annotations

from email.message import EmailMessage
import smtplib

from app.config import settings
from app.models import ContactSubmission


class EmailDeliveryError(Exception):
    pass


def send_contact_notification(submission: ContactSubmission) -> bool:
    if not settings.email_enabled:
        return False

    message = EmailMessage()
    message["Subject"] = "New contact submission"
    message["From"] = settings.email_sender
    message["To"] = settings.email_recipient
    message.set_content(
        "\n".join(
            [
                "A new contact form submission was received.",
                "",
                f"Name: {submission.name}",
                f"Email: {submission.email}",
                f"Phone: {submission.phone}",
                f"Submitted At: {submission.created_at}",
            ]
        )
    )

    try:
        with smtplib.SMTP(settings.smtp_host, settings.smtp_port, timeout=10) as server:
            if settings.smtp_use_tls:
                server.starttls()
            server.login(settings.smtp_username, settings.smtp_password)
            server.send_message(message)
    except OSError as error:
        raise EmailDeliveryError("Unable to send contact notification email.") from error

    return True
