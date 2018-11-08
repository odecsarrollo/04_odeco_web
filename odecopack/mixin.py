from django.contrib import messages

from odecopack import settings
import requests


class RecaptchaMixin(object):
    def revisar_recaptcha(self):
        recaptcha_response = self.request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        if result['success']:
            self.request.recaptcha_is_valid = True
        else:
            self.request.recaptcha_is_valid = False
            messages.error(self.request, 'Invalid reCAPTCHA. Please try again.')
