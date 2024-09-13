## FastAPI Email and PDF Summary Project **********

This project provides two main functionalities: 

--> Send Emails: An endpoint to send emails using Postmark.

--> Create Title and Summary from PDF: An endpoint to generate a title and summary from a PDF document using OpenAI's API.

## Prerequisites

Before you begin, ensure you have the following:

1. Python 3.11 or higher
2. FastAPI
3. Uvicorn
4. Postmark API key
5. OpenAI API key

## Create and activate a virtual environment: 
python -m venv env

## activate the virtual environment
    Windows: .\.venv\Scripts\activate
    Linux: .\.venv\bin\activate

## Install the required packages:
    pip install -r requirements.txt

## Run the Project
    uvicorn main:app --reload  or uvicorn main:app
    