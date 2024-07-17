from django.test import TestCase
from django.conf import settings
from django.contrib.auth.password_validation import validate_password

class Casesforproject(TestCase):
    def test_secret_key(self):
        # self.assertTrue(1==1)
        val=settings.SECRET_KEY
        try:
            is_strong=validate_password(val)
        except Exception as e:
            msg=f"Bad Secret Key {e.messages}"
            self.fail(msg)