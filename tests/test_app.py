import sqlite3

import pytest
from fastapi.testclient import TestClient

import app.routes.contact as contact_routes
from app.config import settings
from app.email_service import EmailDeliveryError
from app.main import app


@pytest.fixture
def test_db(tmp_path, monkeypatch):
    db_path = tmp_path / "advisor_site_test.db"
    monkeypatch.setattr(settings, "database_path", db_path)
    return db_path


@pytest.fixture
def client(test_db):
    with TestClient(app) as test_client:
        yield test_client


def _submission_count(db_path):
    with sqlite3.connect(db_path) as connection:
        result = connection.execute("SELECT COUNT(*) FROM contact_submissions")
        return result.fetchone()[0]


def test_home_page_renders(client):
    response = client.get("/")

    assert response.status_code == 200
    assert "Financial Adviser" in response.text
    assert "About Me" in response.text
    assert "Testimonials" in response.text
    assert "Investment Specialty" in response.text
    assert "Contact" in response.text


def test_contact_submission_is_saved(client, test_db):
    response = client.post(
        "/api/contact",
        json={
            "name": "Test User",
            "email": "test@example.com",
            "phone": "555-123-4567",
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "message": "Thanks for reaching out. We received your inquiry.",
        "warning": None,
    }
    assert _submission_count(test_db) == 1


def test_contact_submission_returns_warning_when_email_fails(client, test_db, monkeypatch):
    def fail_email(_submission):
        raise EmailDeliveryError("boom")

    monkeypatch.setattr(contact_routes, "send_contact_notification", fail_email)

    response = client.post(
        "/api/contact",
        json={
            "name": "Warn User",
            "email": "warn@example.com",
            "phone": "555-999-0000",
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "message": "Thanks for reaching out. We received your inquiry.",
        "warning": "Your inquiry was saved, but the notification email could not be sent.",
    }
    assert _submission_count(test_db) == 1


def test_contact_submission_validation_errors(client):
    response = client.post(
        "/api/contact",
        json={"name": "", "email": "bad", "phone": ""},
    )

    assert response.status_code == 422
