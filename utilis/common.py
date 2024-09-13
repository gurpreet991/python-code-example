from enum import Enum
from typing import Any
from fastapi import Response


class Messages(Enum):
    # Success
    EMAIL_SENT = {"Email sent successfully", True, 200}

    @staticmethod
    def not_exists(module: str):
        return f"{module} does not exists", False, 400


def customResponse(
    response: Response,
    msg=None,
    status: bool = True,
    code: int = 200,
    data: dict | list | Any | None = None,
    **kwargs,
):
    if int(code / 100) != 2:
        status = False
    if msg:
        if isinstance(msg, Messages):
            msg = msg.value
        if isinstance(msg, str):
            msg = msg
        if isinstance(msg, tuple):
            msg, status, code = msg
    response_data = {"status": status, "msg": msg, "data": data}
    response_data = {k: v for k, v in response_data.items() if v is not None}
    response_data = response_data | kwargs
    response.status_code = code
    if int(code / 100) != 2:
        print(f""""{response_data}""")
    return response_data
