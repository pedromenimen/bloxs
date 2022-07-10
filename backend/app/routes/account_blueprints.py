from app.controllers.account_controllers import (
    block_account,
    create_account,
    transaction_check_balance,
)
from flask import Blueprint

bp_accounts = Blueprint("accounts", __name__, url_prefix="/api/accounts")


bp_accounts.post("/register/")(create_account)
bp_accounts.get("/check-balance/")(transaction_check_balance)
bp_accounts.patch("/block-account/")(block_account)

