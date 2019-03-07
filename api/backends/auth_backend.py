import abc


class AuthBackend(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def authenticate_user(self, username, password):
        pass


class AutoAuthBackend(AuthBackend):
    def authenticate_user(self, username, password):
        return True


ApiAuth = AutoAuthBackend()  # type: AuthBackend
