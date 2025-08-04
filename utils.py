import uuid
import smtplib
from email.mime.text import MIMEText
from config import Config

def generate_task_id(task_dict):
    """
    Generate a unique task ID in the format 'TASK-N', where N is one greater than the current max.
    """
    items = task_dict.get("Items", [])
    max_id = 0
    for item in items:
        tid = item.get("task_id", "")
        if tid.startswith("TASK-"):
            try:
                num = int(tid.split("-")[1])
                if num > max_id:
                    max_id = num
            except (IndexError, ValueError):
                continue
    return f"TASK-{max_id + 1}"

def send_email_notification(to_email, subject, body):
    """
    Send an email notification using SMTP.
    Assumes SMTP config is set in Config: SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, FROM_EMAIL.
    """
    smtp_server = getattr(Config, 'SMTP_SERVER', None)
    smtp_port = getattr(Config, 'SMTP_PORT', 587)
    smtp_username = getattr(Config, 'SMTP_USERNAME', None)
    smtp_password = getattr(Config, 'SMTP_PASSWORD', None)
    from_email = getattr(Config, 'FROM_EMAIL', smtp_username)

    if not all([smtp_server, smtp_port, smtp_username, smtp_password, from_email, to_email]):
        raise ValueError("SMTP configuration or recipient email missing.")

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(from_email, [to_email], msg.as_string())