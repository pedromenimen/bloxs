from app.controllers.transaction_controllers import (
    transaction_deposit,
    transaction_withdraw,
    check_transactions
)
from flask import Blueprint

bp_transaction = Blueprint("transaction", __name__, url_prefix="/api/transaction")


bp_transaction.patch("/deposit/")(transaction_deposit)
bp_transaction.patch("/withdraw/")(transaction_withdraw)
bp_transaction.get("/check-transactions/")(check_transactions)