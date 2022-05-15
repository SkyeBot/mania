from quart import Quart
from ass import views

app = Quart(__name__)
app.register_blueprint(views)

if __name__ == "__main__":
    app.run(debug=True)