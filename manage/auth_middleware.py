from http.client import UNAUTHORIZED
from typing import Callable, Awaitable, Optional

from aiohttp import web, hdrs, BasicAuth


@web.middleware
class BasicAuthMiddleware:
    def __init__(self, user: str, password: str, realm: str = "Calipso API"):
        self.user = user
        self.password = password
        self.realm = realm

    @staticmethod
    def decode_auth_header(request: web.Request) -> Optional[BasicAuth]:
        auth_header = request.headers.get(hdrs.AUTHORIZATION)
        if not auth_header:
            return None

        return BasicAuth.decode(auth_header=auth_header)

    def check_credentials(self, user: str, password: str) -> bool:
        return user == self.user and password == self.password

    def authenticate(self, request: web.Request) -> bool:
        try:
            auth = self.decode_auth_header(request)
        except ValueError:
            return False

        return auth and self.check_credentials(user=auth.login, password=auth.password)

    def challenge(self) -> web.Response:
        return web.Response(
            status=UNAUTHORIZED,
            headers={
                hdrs.WWW_AUTHENTICATE: 'Basic realm="{}"'.format(self.realm),
            }
        )

    async def __call__(self, request: web.Request, handler: Callable[..., Awaitable[web.Response]], *args, **kwargs):
        return await handler(request) if self.authenticate(request) else self.challenge()
