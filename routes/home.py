from flask import Blueprint, jsonify


home_page = Blueprint('home_page', __name__)

@home_page.route('/', methods=['GET'])
def home():
  print("Toto")
  return jsonify(None)
