from flask import render_template
import connexion
from werkzeug.middleware.proxy_fix import ProxyFix
from config import Config
config_obj = Config.load()

connexion_app = connexion.FlaskApp(__name__, specification_dir="./")
connexion_app.app.config.from_object(config_obj)
# connexion_app.add_api("swagger.yml")
connexion_app.app.wsgi_app = ProxyFix(connexion_app.app.wsgi_app, x_proto=1, x_host=1)

app = connexion_app.app
app.url_map.strict_slashes = False


@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config_obj.LISTEN_PORT, debug=config_obj.DEBUG)