from flask import Flask
from main.user_routes import userapi
from main.post_routes import postapi
from main.collection_routes import collectionapi

app = Flask(__name__)

# apply the blueprints to the app
app.register_blueprint(userapi)
app.register_blueprint(postapi)
app.register_blueprint(collectionapi)


