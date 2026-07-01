from backend.database.models import Wallet as WalletModel
from backend.database.db import db

def update_wallet(user_id, btc_change, usd_change):
    wallet = WalletModel.query.filter_by(user_id=user_id).first()

    wallet.btc_balance += btc_change
    wallet.usd_balance += usd_change

    db.session.commit()