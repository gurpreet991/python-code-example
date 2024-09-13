import traceback
from fastapi.templating import Jinja2Templates
from config import get_settings
from postmarker.core import PostmarkClient


templates = Jinja2Templates(directory="templates")


def send_email_ses(stream, recipient_email, subject, template_name="base.html", html_content=None,
                   sender_email="", **kwargs
                   ):
    try:
        content_email = kwargs.get("content_email")
        frontent_url = ""
        kwargs["Support"] = ""
        kwargs["preference"] = ""

        MessageStream = stream
        token = get_settings().POSTMARK_LIVE_TOKEN

        context = kwargs
        if not html_content:
            html_content = templates.get_template(
                template_name).render(context)

        sender_email = sender_email if sender_email else get_settings().POSTMARK_TESTING_EMAIL
        MessageStream = stream if content_email else "notifications"
        body = {
            'From': sender_email,  # sender_email,
            'Subject': subject,
            'HtmlBody': html_content,
            'MessageStream': MessageStream
        }
        postmarker_client = PostmarkClient(server_token=token)
        response = postmarker_client.emails.send_batch(
            *[{**body, 'To': recipient} for recipient in recipient_email])
        print(f'Email sent {response[0]} ')
        return response[0].get('MessageID')
    except Exception as e:
        print(traceback.format_exc())
        print(f"Error sending email: {e}")
