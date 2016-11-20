from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import os
import workday
import re

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get('LINE_CHANNEL_ACCESS_TOKEN')) # token
handler = WebhookHandler(os.environ.get('LINE_CHANNEL_SECRET')) # secret

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    pattern = re.compile("^\d{4}-\d{1,2}-\d{1,2}, \d*$")
    if pattern.fullmatch(text) == None:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Please enter start date and number of days in the correct format\n\n For example: 2016-11-31, 20")
            )
        return

    start_date, days = text.split(',')

    end_date = workday.workday_helper(start_date, int(days))
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=end_date.strftime("%Y-%m-%d"))
        )


if __name__ == "__main__":
    app.run()
