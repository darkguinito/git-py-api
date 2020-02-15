from flask import Blueprint, request, jsonify
from markupsafe import escape
from pygit2 import Repository
import os


repo_page = Blueprint('repo_page', __name__)

repo_list = [
    { 'id': 0,
      'path': "/usr/src/app"
    }
]

# A route to return all of the available entries in our catalog.
@repo_page.route('/api/v1/repos/all', methods=['GET'])
def api_all():    
    return jsonify(repo_list)

@repo_page.route('/api/v1/repos', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    entries = os.listdir(repo_list[id]["path"])
    print(entries)
    repo = Repository(repo_list[id]["path"] + os.sep + '.git')
    print(repo.list_worktrees())
    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for rep in repo_list:
        if rep['id'] == id:
            results.append(rep)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)
