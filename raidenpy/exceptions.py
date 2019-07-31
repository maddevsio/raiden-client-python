class ResponseStatusCodeException(Exception):
    """Unseccesfull status code in response header"""

    pass


class PaymentRequiredException(Exception):
    pass


class NotFoundException(Exception):
    pass


class ConflictException(Exception):
    pass


class NotImplementedException(Exception):
    pass


class InternalServerException(Exception):
    pass
