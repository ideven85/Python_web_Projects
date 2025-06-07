import uuid


def _random_uuid():
    return uuid.uuid4().hex[:6]
