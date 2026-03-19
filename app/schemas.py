from pydantic import BaseModel, ConfigDict, EmailStr, Field


class ContactSubmissionCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    name: str = Field(..., min_length=2, max_length=120)
    email: EmailStr
    phone: str = Field(..., min_length=7, max_length=40)


class ContactSubmissionResponse(BaseModel):
    message: str
    warning: str | None = None
