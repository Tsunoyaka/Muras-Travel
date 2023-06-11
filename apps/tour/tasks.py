from django.core.mail import send_mail
from django.conf import settings
from config.celery import app
from decouple import config

@app.task
def send_report_form(name, phone, tour):
    message = f'Имя: {name}\nТелефон: {phone}\nТур: {tour.title}\nЦена: {tour.price} сом'
    send_mail(
        subject='Кто то заполнил форму отправки!',
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[config('EMAIL')],
        fail_silently=False
    )
