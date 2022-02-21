from common.make_tx import make_reward_tx, make_unknown_tx
from terra import util_terra
from terra.make_tx import make_gov_stake_tx, make_gov_unstake_tx
from terra.constants import CUR_SPEC

def handle_spec_withdraw(exporter, elem, txinfo):
    wallet_address = txinfo.wallet_address
    txid = txinfo.txid
    amount = 0
   
    for log_idx in elem["logs"]:
        from_contract = log_idx["events_by_type"]["from_contract"]

        try:
            amount_string = from_contract["spec_amount"][0]
            amount += util_terra._float_amount(amount_string, CUR_SPEC)
        except Exception:
            pass

    row = make_reward_tx(txinfo, amount, CUR_SPEC, txid)
    exporter.ingest_row(row)