
import threading
from fastapi import APIRouter, File, Response, UploadFile, Request

from apis.functions import content_generate_overview_title, mail_sending
from apis.schema import EmailSchema
from config import get_settings
from utilis.common import Messages, customResponse
from fastapi_versionizer.versionizer import api_version


router = APIRouter(tags=["Email"])


@router.post("/email")
@api_version(get_settings().CURRENT_VERSION)
async def create_email(
    request: Request,
    body: EmailSchema,
    response: Response,
):
    try:
        # utilized threading for send emails in bulk
        threading.Thread(target=mail_sending, args=(
            body, request)).start()
        return customResponse(response, msg=Messages.EMAIL_SENT)
    except Exception as e:
        return customResponse(response, msg=str(e), status=False, code=500)


@router.post("/generate-content")
@api_version(get_settings().CURRENT_VERSION)
async def generate_summary(
    response: Response,
    file: UploadFile = File(None),
):
    try:
        data = await content_generate_overview_title(file)
        return customResponse(response, status=True, data=data)
    except Exception as e:
        return customResponse(response, msg=str(e), status=False, code=500)
