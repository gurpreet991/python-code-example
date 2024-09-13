import os
from openai import OpenAI

from config import get_settings

client = OpenAI(api_key=get_settings().OPEN_AI_KEY)


def create_thread():
    try:
        thread = client.beta.threads.create()
        return thread.id
    except Exception as e:
        print(f"error in create_thread :- {e}")


def create_file(file):
    file = client.files.create(
        file=open(file, "rb"),
        purpose='assistants'
    )
    return file


def send_message_to_thread(thread, role, text):
    try:
        print("generate message")
        message = client.beta.threads.messages.create(
            thread_id=thread, role=role, content=text)
        print("generate message successfully")
        return message
    except Exception as e:
        print(f"error in send_message_to_thread :- {e}")


def run_thread(thread, assisstant_id):
    try:
        print("run thread start")
        run = client.beta.threads.runs.create(
            thread_id=thread,
            assistant_id=assisstant_id)
        status = None
        while status != "completed":
            run_list = client.beta.threads.runs.retrieve(
                thread_id=thread, run_id=run.id)
            print(f"{run_list.status}\r", end="")
            status = run_list.status
            print(f"{status}")
        messages = client.beta.threads.messages.list(
            thread_id=thread)
        print("run thread done")
        return messages
    except Exception as e:
        print(f"error in run_thread :- {e}")


def create_overview_and_title(assisstant_id, text):
    try:
        thread_id = create_thread()
        message = send_message_to_thread(
            thread_id, "user", text)
        result = run_thread(thread_id, assisstant_id)
        return thread_id, result
    except Exception as e:
        print(f"error in create_overview_and_title :- {e}")
