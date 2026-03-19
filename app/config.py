import os
from pathlib import Path


def load_env_file(env_path: Path) -> None:
    if not env_path.exists():
        return

    for raw_line in env_path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


BASE_DIR = Path(__file__).resolve().parent.parent
load_env_file(BASE_DIR / ".env")


class Settings:
    def __init__(self) -> None:
        self.app_name = os.getenv("APP_NAME", "Advisor Website")
        self.environment = os.getenv("APP_ENV", "development")
        self.database_path = Path(
            os.getenv("DATABASE_PATH", str(BASE_DIR / "data" / "advisor_site.db"))
        )
        self.smtp_host = os.getenv("SMTP_HOST", "")
        self.smtp_port = int(os.getenv("SMTP_PORT", "587"))
        self.smtp_username = os.getenv("SMTP_USERNAME", "")
        self.smtp_password = os.getenv("SMTP_PASSWORD", "")
        self.email_sender = os.getenv("EMAIL_SENDER", "")
        self.email_recipient = os.getenv("EMAIL_RECIPIENT", "")
        self.smtp_use_tls = os.getenv("SMTP_USE_TLS", "true").lower() == "true"

    @property
    def email_enabled(self) -> bool:
        required = [
            self.smtp_host,
            self.smtp_username,
            self.smtp_password,
            self.email_sender,
            self.email_recipient,
        ]
        return all(required)

    @property
    def templates_dir(self) -> Path:
        return BASE_DIR / "templates"

    @property
    def static_dir(self) -> Path:
        return BASE_DIR / "static"


settings = Settings()
