from app.routes.account_blueprints import bp_accounts
from app.routes.transaction_blueprints import bp_transaction
from app.routes.user_blueprints import bp_users
from app.routes.documentation_blueprint import bp_doc
from flask import Flask


def init_app(app: Flask):
    app.register_blueprint(bp_users)
    app.register_blueprint(bp_accounts)
    app.register_blueprint(bp_transaction)
    app.register_blueprint(bp_doc)
