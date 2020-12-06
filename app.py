
import os
from notion.client import NotionClient
from flask import Flask
from flask import request


app = Flask(__name__)


def createNotionTask(token, collectionURL, title, note):
    # notion
    client = NotionClient(token)
    cv = client.get_collection_view(collectionURL)
    row = cv.collection.add_row()
    row.title = title
	row.note = note


@app.route('/create_todo', methods=['GET'])
def create_todo():
    title = request.args.get('title')
	note = request.args.get('note')
    token_v2 = os.environ.get("TOKEN")
    url = os.environ.get("URL")
    createNotionTask(token_v2, url, title, note)
    return f'added {todo} to Notion'


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
