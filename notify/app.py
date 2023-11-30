import json
import os


# import requests


def lambda_handler(event, context):
    print("env ", os.environ)
    telegram_bot_client = get_telegram_bot_client()
    google_client = get_google_sheets_client()
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "notify team",
            # "location": ip.text.replace("\n", "")
        }),
    }


def get_telegram_bot_client():
    telegram_bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
    print("tele ", telegram_bot_token)


def get_google_sheets_client():
    google_sheets_token = os.environ["GOOGLE_SHEETS_TOKEN"]
    print("sheets ", google_sheets_token)