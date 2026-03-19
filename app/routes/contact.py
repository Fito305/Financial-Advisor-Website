from __future__ import annotations

from datetime import datetime, timezone

import logging

from fastapi import APIRouter

from app.database import get_connection
from app.email_service import EmailDeliveryError, send_contact_notification
from app.models import ContactSubmission
from app.schemas import ContactSubmissionCreate, ContactSubmissionResponse


router = APIRouter(prefix="/api/contact", tags=["contact"])
logger = logging.getLogger(__name__)


@router.post("", response_model=ContactSubmissionResponse)
def submit_contact_form(payload: ContactSubmissionCreate) -> ContactSubmissionResponse:
    created_at = datetime.now(timezone.utc).isoformat()
    submission = ContactSubmission(
        name=payload.name,
        email=str(payload.email),
        phone=payload.phone,
        created_at=created_at,
    )

    with get_connection() as connection:
        connection.execute(
            """
            INSERT INTO contact_submissions (name, email, phone, created_at)
            VALUES (?, ?, ?, ?)
            """,
            (submission.name, submission.email, submission.phone, submission.created_at),
        )

    try:
        send_contact_notification(submission)
    except EmailDeliveryError as error:
        logger.warning("Contact submission saved but email delivery failed: %s", error)
        return ContactSubmissionResponse(
            message="Thanks for reaching out. We received your inquiry.",
            warning="Your inquiry was saved, but the notification email could not be sent.",
        )

    return ContactSubmissionResponse(
        message="Thanks for reaching out. We received your inquiry."
    )
