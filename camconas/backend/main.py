# from _typeshed import Self
# from flask_mar
# chrome.exe --user-data-dir="C://Chrome dev session" --disable-web-security
from collections import OrderedDict
import operator
from flask import Flask, request
from flask_restful import Api, Resource
from flask import jsonify
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import time
from datetime import datetime
import pandas as pd
from flask_cors import CORS, cross_origin
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
api = Api(app)
ma = Marshmallow(app)
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "ipl"
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
MySQL = MySQL(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/ipl'
db = SQLAlchemy(app)

# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE,OPTIONS')
    return response


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin',
                         'http://localhost:8080')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response


class IplMatchDetails(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    city = db.Column(db.String(100))
    date = db.Column(db.DateTime)
    player_of_match = db.Column(db.String(100))
    venue = db.Column(db.String(100))
    neutral_venue = db.Column(db.String(50))
    team1 = db.Column(db.String(100))
    team2 = db.Column(db.String(100))
    toss_winner = db.Column(db.String(100))
    toss_decision = db.Column(db.String(50))
    winner = db.Column(db.String(100))
    result = db.Column(db.String(20))
    result_margin = db.Column(db.String(50))
    eliminator = db.Column(db.String(25))
    method = db.Column(db.String(25))
    umpire1 = db.Column(db.String(100))
    umpire2 = db.Column(db.String(100))

    def __init__(self, city, date, player_of_match, venue, neutral_venue, team1,
                 team2, toss_winner, toss_decision, winner, result, result_margin,
                 eliminator, method, umpire1, umpire2
                 ):
        self.city = city
        self.date = date
        self.player_of_match = player_of_match
        self.venue = venue
        self.neutral_venue = neutral_venue
        self.team1 = team1
        self.team2 = team2
        self.toss_winner = toss_winner
        self.toss_decision = toss_decision
        self.winner = winner
        self.result = result
        self.result_margin = result_margin
        self.eliminator = eliminator
        self.method = method
        self.umpire1 = umpire1
        self.umpire2 = umpire2


class MatchDetailSchema(ma.Schema):
    class Meta:
        fields = ('id', 'city', 'date', 'player_of_match', 'venue', 'neutral_venue', 'team1',
                  'team2', 'toss_winner', 'toss_decision', 'winner', 'result', 'result_margin',
                  'eliminator', 'method', 'umpire1', 'umpire2'
                  )


Team_TeamDetailsSchema = MatchDetailSchema(many=False)
Teams_TeamDetailsSchema = MatchDetailSchema(many=True)

# cur = MySQL.connection.cursor()
# cur.execute('''SELECT * FROM ipl.ipl_match_details''')
# rv = cur.fetchall()

# Get All Match Details


@app.route('/match_list', methods=['GET', 'POST'])
def get_products():
    all_match_details = IplMatchDetails.query.all()
    result = Teams_TeamDetailsSchema.dump(all_match_details)
    return jsonify(result)


@app.route('/latest_match_winner', methods=['GET'])
def get_productsss():
    all_match_details = IplMatchDetails.query.all()
    last_10_matches = []
    result = Teams_TeamDetailsSchema.dump(all_match_details)

    for value in result:
        last_10_matches.append(value['date'])
        last_10_matches.sort(key=lambda x: time.mktime(
            time.strptime(x, "%Y-%m-%d")), reverse=True)

    # out = result.keys()[result.values().index(last_10_matches[0])]
    # print(last_10_matches[0])
    for j in result:
        if j['date'] == last_10_matches[0]:
            last_match = j
            # print(j)
    return jsonify(last_match)

# Get Single Match Details


@app.route('/home/<id>/', methods=['GET'])
def get_product(id):
    single_match_details = IplMatchDetails.query.get(id)
    result = Team_TeamDetailsSchema.dump(single_match_details)
    # print((result['city']))

    return jsonify(result)

# Update a Match Details


# @app.route("/")
@cross_origin()
@app.route('/match_list/<id>', methods=['PUT'])
def update_product(id):
    update_match = IplMatchDetails.query.get(int(id))

    # print("valueee", request.json['date'])
    if request.json['id']:
        id = request.json['id']
    if request.json['city']:
        city = request.json['city']
    if request.json['date'] != '':
        date = request.json['date']
    if request.json['player_of_match']:
        player_of_match = request.json['player_of_match']
    if request.json['venue']:
        venue = request.json['venue']
    if request.json['neutral_venue']:
        neutral_venue = request.json['neutral_venue']
    if request.json['team1']:
        team1 = request.json['team1']
    if request.json['team2']:
        team2 = request.json['team2']
    # if request.json['toss_winner']:
    #     toss_winner = request.json['toss_winner']
    # if request.json['toss_decision']:
    #     toss_decision = request.json['toss_decision']
    # if request.json['winner']:
    #     winner = request.json['winner']
    # if request.json['result']:
    #     result = request.json['result']
    # if request.json['result_margin']:
    #     result_margin = request.json['result_margin']
    # if request.json['eliminator']:
    #     eliminator = request.json['eliminator']
    # if request.json['method']:
    #     method = request.json['method']
    # if request.json['umpire1']:
    #     umpire1 = request.json['umpire1']
    # if request.json['umpire2']:
    #     umpire2 = request.json['umpire2']
    # id = request.json['id']
    # city = request.json['city']
    # date = request.json['date']
    # player_of_match = request.json['player_of_match']
    # venue = request.json['venue']
    # neutral_venue = request.json['neutral_venue']
    # team1 = request.json['team1']
    # team2 = request.json['team2']
    # toss_winner = request.json['toss_winner']
    # toss_decision = request.json['toss_decision']
    # winner = request.json['winner']
    # result = request.json['result']
    # result_margin = request.json['result_margin']
    # eliminator = request.json['eliminator']
    # method = request.json['method']
    # umpire1 = request.json['umpire1']
    # umpire2 = request.json['umpire2']
    if id:
        update_match.id = id
    if city:
        update_match.city = city
    if date:
        update_match.date = date
    if player_of_match:
        update_match.player_of_match = player_of_match
    if venue:
        update_match.venue = venue
    if neutral_venue:
        update_match.neutral_venue = neutral_venue
    if team1:
        update_match.team1 = team1
    if team2:
        update_match.team2 = team2
    # if toss_winner:
    #     update_match.toss_winner = toss_winner
    # if toss_decision:
    #     update_match.toss_decision = toss_decision
    # if winner:
    #     update_match.winner = winner
    # if result:
    #     update_match.result = result
    # if result_margin:
    #     update_match.result_margin = result_margin
    # if eliminator:
    #     update_match.eliminator = eliminator
    # if method:
    #     update_match.method = method
    # if umpire1:
    #     update_match.umpire1 = umpire1
    # if umpire2:
    #     update_match.umpire2 = umpire2
    # if id:
    #     update_match.id = id

    # update_match.id = id
    # update_match.city = city
    # update_match.date = date
    # update_match.player_of_match = player_of_match
    # update_match.venue = venue
    # update_match.neutral_venue = neutral_venue
    # update_match.team1 = team1
    # update_match.team2 = team2
    # update_match.toss_winner = toss_winner
    # update_match.toss_decision = toss_decision
    # update_match.winner = winner
    # update_match.result = result
    # update_match.result_margin = result_margin
    # update_match.eliminator = eliminator
    # update_match.method = method
    # update_match.umpire1 = umpire1
    # update_match.umpire2 = umpire2

    db.session.commit()
    return Team_TeamDetailsSchema.jsonify(update_match)


# class home(Resource):
#     def get(self, pk):
#         team_detail = IplMatchDetails.query.all()
#         # team_detail = IplMatchDetails.query.get(pk)
#         print(pk)

#         all_team_detail = Teams_TeamDetailsSchema.dump(team_detail)
#         return jsonify(all_team_detail)

#     def post(self, pk):
#         team_detail = IplMatchDetails.query.get(pk)
#         print(team_detail)
#         return jsonify(team_detail)


# api.add_resource(home, "/home/<int:pk>/")
# api.add_resource(home, "/home/<int:pk>")
if __name__ == "__main__":
    app.run(debug=True)
