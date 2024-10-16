from flask import Flask, jsonify, request, g
import jwt
from db.dbconnection import DbConnection
from controller import auth_controller
from status_code.status import http_statuses
from model.decorator import checkSession
from controller.feture_controller import fetch_user
from flask_cors import CORS
app = Flask(__name__)

CORS(app)

# Open a new database connection before each request
@app.before_request
def before_request():
    g.conn = DbConnection()
    g.cursor = g.conn.get_cursor()
    

# Close the database connection after each request
@app.teardown_request
def teardown_request(exception):
    
    if g.conn is not None:
        g.conn.close_connection()

@app.route('/')
@checkSession.check_session
def home():
    return jsonify({
        "text": "Welcome to Flask API",
        "status": 200
    })

@app.route('/all_user')
@checkSession.check_session
def  all_user():
    cursor = g.cursor
    return fetch_user(cursor=cursor)


@app.route('/user/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    
    cursor = g.cursor
    if cursor is not None:
        print("gg")
        response = jsonify(auth_controller.log_in(cursor=cursor, email=username, password=password))
        return response
    return jsonify(**http_statuses[500])

@app.route('/user/signup', methods=['POST'])
def signup():
    name = request.json.get('name')
    email = request.json.get('email')
    password = request.json.get('password')
    role = request.json.get('role')
    
    cursor = g.cursor
    if cursor is not None:
        response = jsonify(auth_controller.sign_up(cursor=cursor, name=name, email=email, password=password, role=role))
        return response

    return jsonify(**http_statuses[409])

@app.errorhandler(400)
def handle_bad_request(error):
    return jsonify({"error": "Bad request"}), 400

