from config.dotenv import env
from utils.errors_handlers import app
from config.database import database as db
from config.logging import logger
from flask_cors import cross_origin


@app.route('/')
@cross_origin()
def index():
    # return make_response(render_template('index.html', title = env['NAME_APP']), 200)
    return {"ok": True, "message": "Se pudo"}

with app.app_context():
    logger(db.create_all)


if __name__ == '__main__':
    app.run(debug=env['DEBUG'], host=env['HOST'], port=env['PORT'])