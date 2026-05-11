import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def enviar_email_smtp(
    smtp_host,
    smtp_port,
    smtp_usuario,
    smtp_senha,
    email_origem,
    email_destino,
    assunto,
    corpo,
):
    msg = MIMEMultipart()
    msg["From"] = email_origem
    msg["To"] = email_destino
    msg["Subject"] = assunto

    msg.attach(MIMEText(corpo, "plain", "utf-8"))

    with smtplib.SMTP(smtp_host, int(smtp_port)) as servidor:
        servidor.starttls()
        servidor.login(smtp_usuario, smtp_senha)
        servidor.send_message(msg)
