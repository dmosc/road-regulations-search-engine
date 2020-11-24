import os
import logging
import pymongo
import json
from copy import copy

from flask import Flask  # pylint: disable=import-error
from flask import request  # pylint: disable=import-error
from flask import jsonify  # pylint: disable=import-error
from parser import parse_all_documents
from bson import json_util
from connector import get_article_by_number
from connector import get_articles_by_tfidf_value


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
db = pymongo.MongoClient('mongodb://localhost:27017/')


@app.route('/parse', endpoint='parser', methods=['POST'])
def trigger_parsing():
    try:
        parse_all_documents()
    except Exception as e:
        logging.error(e)
        return {"error": {"message": "Internal Parser Error"}}, 500
    return "Sucessful Operation", 200


@app.route('/articles/byKeywords', methods=['POST'])
def get_keywords():
    json_request = request.get_json()
    if "keywords" not in json_request:
        error = {"error": {"message": "keywords request body is missing"}}
        logging.error(error)
        return error, 400
    else:
        return json.loads(json_util.dumps(get_articles_by_tfidf_value(json_request['keywords'])))


@app.route('/articles/<id>', methods=['GET'])
def get_article_by_number_in_memory(id):
    """Returns the article that matches the ID value
    accoring to the apiSpec.yaml file"""
    article = db['search-engine']['articles'].find_one({'id': id})
    if article is not None:
        return json.loads(json_util.dumps(article))
    else:
        error = {"error": {"message": "Article not found with submitted ID"}}, 404
        logging.error(error)
        return error


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8082)
