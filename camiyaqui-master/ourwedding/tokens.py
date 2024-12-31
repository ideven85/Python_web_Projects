from datetime import date

from django.conf import settings
from django.utils.crypto import salted_hmac, constant_time_compare
from django.utils.http import int_to_base36, base36_to_int


class LoginTokenGenerator:
    key_salt = "LoginTokenGenerator"
    secret = settings.SECRET_KEY

    def check_token(self, user, token):
        if not (user and token):
            return False

        try:
            ts_b36, _, us_b36 = token.split("-")
        except ValueError:
            return False

        try:
            ts = base36_to_int(ts_b36)
        except ValueError:
            return False

        if not constant_time_compare(self._make_token_with_timestamp(user, ts), token):
            return False

        if (self._num_days(date.today()) - ts) > settings.LOGIN_TOKEN_TIMEOUT_DAYS:
            return False

        return True

    def make_token(self, user):
        return self._make_token_with_timestamp(user, self._num_days(date.today()))

    def _make_token_with_timestamp(self, user, timestamp):
        ts_b36 = int_to_base36(timestamp)
        us_b36 = int_to_base36(user.pk)

        hash_string = salted_hmac(
            self.key_salt, self._make_hash_value(user, timestamp), secret=self.secret
        ).hexdigest()[::4]

        return "%s-%s-%s" % (ts_b36, hash_string, us_b36)

    def _make_hash_value(self, user, timestamp):
        return str(user.pk) + user.email + str(timestamp)

    def _num_days(self, dt):
        return (dt - date(2001, 1, 1)).days


login_token_generator = LoginTokenGenerator()
