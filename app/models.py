from dataclasses import dataclass


@dataclass
class ContactSubmission:
    name: str
    email: str
    phone: str
    created_at: str
