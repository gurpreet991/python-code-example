from io import BytesIO
import re
import traceback

import PyPDF2
from apis.schema import EmailSchema
from config import get_settings
from utilis.openai import create_overview_and_title
from utilis.postmark import send_email_ses


def extract_text_from_pdf(pdf_contents) -> str:
    pdf_file = BytesIO(pdf_contents)
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += page.extract_text()
    return text


async def content_generate_overview_title(file):
    try:
        assistant_id = get_settings().OPEN_ASSISSTANT_ID
        text = ""
        if file:
            pdf_contents = await file.read()
            file = extract_text_from_pdf(pdf_contents)
            text = f"{get_settings().AI_PROMPT} \n{get_settings().AI_LIMIT}\nresopnse only in json".replace(
                "[Content]", f"{file}")

        thread_id, result = create_overview_and_title(
            assistant_id, text)
        announcement_summary = result.data[0].content[0].text.value
        data = {
            "thread_id": thread_id,
            "result": announcement_summary
        }
        return data
    except Exception as e:
        print(f"content_generate_summary_headline exception: {e}")


def mail_sending(email: EmailSchema, request=None):
    support = f"{get_settings().SUPPORT}"
    for recipient in email.recipients:
        message_id = send_email_ses(email.stream,
                                    [recipient], email.subject,
                                    sender_email=support, content_email=True)
