from exponent_server_sdk import DeviceNotRegisteredError
from exponent_server_sdk import PushClient
from exponent_server_sdk import PushMessage
from exponent_server_sdk import PushResponseError
from exponent_server_sdk import PushServerError
from requests.exceptions import ConnectionError
from requests.exceptions import HTTPError
from backend.models import PushTokens


# Basic arguments. You should extend this function with the push features you
# want to use, or simply pass in a `PushMessage` object.
def send_push_message(token, title, message, extra=None):
    response = PushClient().publish(PushMessage(to=token, body=message, data=extra))
    try:
        response.validate_response()
    except DeviceNotRegisteredError:
        # Mark the push token as inactive
        PushTokens.objects.get(token=token).update(active=False)
    return response
