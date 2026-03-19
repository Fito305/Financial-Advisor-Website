# Advisor Website

Single-page financial adviser website built with FastAPI, Jinja templates, vanilla JavaScript, and SQLite.

## Setup

1. Create a virtual environment.
2. Install runtime dependencies:

```bash
./.venv/bin/pip install -r requirements.txt
```

3. Copy `.env.example` to `.env` and update values as needed.
4. Start the app with:

```bash
./.venv/bin/uvicorn app.main:app --reload
```

5. Open `http://127.0.0.1:8000`.

## Editable content

Business-facing placeholder content is centralized in `app/content.py`.

## Contact form

The contact form submits to `POST /api/contact`, stores inquiries in SQLite, and attempts to send an email notification when SMTP settings are configured.

If SMTP is not configured, submissions are still saved to SQLite.

If SMTP is configured but delivery fails, submissions are still saved and the API returns a warning message instead of losing the lead.

## Email configuration

Update `.env` with real SMTP values:

- `SMTP_HOST`
- `SMTP_PORT`
- `SMTP_USERNAME`
- `SMTP_PASSWORD`
- `SMTP_USE_TLS`
- `EMAIL_SENDER`
- `EMAIL_RECIPIENT`

Typical setup:

- `EMAIL_SENDER` should be the mailbox or verified sender address your SMTP provider allows.
- `EMAIL_RECIPIENT` should be the inbox where you want new lead notifications delivered.
- If your email provider requires an app password or provider-specific SMTP settings, use those values instead of your normal login password.

## Run tests

Install development dependencies:

```bash
./.venv/bin/pip install -r requirements-dev.txt
```

Run:

```bash
./.venv/bin/pytest
```

## Owner checklist

Complete these steps personally before launch:

1. Create your local environment file:

```bash
cp .env.example .env
```

2. Open `.env` and set these values:
   `SMTP_HOST`, `SMTP_PORT`, `SMTP_USERNAME`, `SMTP_PASSWORD`, `SMTP_USE_TLS`, `EMAIL_SENDER`, `EMAIL_RECIPIENT`.
3. Choose where notification emails should go:
   set `EMAIL_RECIPIENT` to the inbox that should receive new contact-form alerts.
4. Confirm the sender address:
   set `EMAIL_SENDER` to the mailbox or verified sender identity your SMTP provider allows.
5. If your SMTP provider requires an app password or provider-specific credential, create that now and use it instead of your normal email password.
6. Replace the placeholder business content in `app/content.py`:
   business name, hero text, advisor bio, testimonials, specialties, contact details, and Calendly link.
7. If you want real images instead of placeholders, add them under `static/images/` and update the templates/CSS as needed.
8. Start the app locally:

```bash
./.venv/bin/uvicorn app.main:app --reload
```

9. Open `http://127.0.0.1:8000` in your browser and review:
   desktop layout, mobile layout, section scrolling, form behavior, and final copy.
10. Submit the contact form with your real SMTP configuration in place and confirm that:
   the submission is saved and the notification email arrives in the inbox set by `EMAIL_RECIPIENT`.
11. If you change any URLs, branding, or contact details, do one final browser pass before deployment.

## Helpful documentation

Use these official resources to complete the owner steps above.

### Local Python setup

- Python virtual environments:
  https://docs.python.org/3/library/venv.html
- FastAPI running the app manually:
  https://fastapi.tiangolo.com/deployment/manually/
- Uvicorn runtime options:
  https://www.uvicorn.org/settings/

### Calendly

- How to share your scheduling link:
  https://help.calendly.com/hc/en-us/articles/223193448-How-to-share-your-scheduling-link
- How to add Calendly to your website:
  https://help.calendly.com/hc/en-us/articles/4409838727703-Embedding-Calendly-on-your-site

### SMTP provider examples

- Google account app passwords:
  https://support.google.com/accounts/answer/185833
- Microsoft 365 authenticated SMTP:
  https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/authenticated-client-smtp-submission
- Twilio SendGrid SMTP getting started:
  https://www.twilio.com/docs/sendgrid/for-developers/sending-email/getting-started-smtp/

## SMTP provider note

This project currently sends email with Python's built-in SMTP login flow (`smtplib`) using a host, port, username, and password from `.env`.

That works well with providers that still support standard SMTP credentials or app passwords.

If your provider requires OAuth instead of SMTP username/password, the contact form will still save submissions to SQLite, but the email-notification code will need to be updated before notifications can work.

If you plan to use Microsoft 365 / Exchange Online, review the Microsoft SMTP documentation above first and confirm that your mailbox and tenant support the authentication method you want to use.
