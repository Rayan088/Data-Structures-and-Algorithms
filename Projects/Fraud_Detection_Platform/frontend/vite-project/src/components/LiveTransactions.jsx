import { useEffect, useState } from "react";
import { getLiveTransactions } from "../api/fraudApi";
import SlidePanel from "./SlidePanel";

function LiveTransactions() {
    const [transactions, setTransactions] = useState([]);
    const [selectedTxn, setSelectedTxn] = useState(null);

    useEffect(() => {
        async function loadData() {
            try {
                const response = await getLiveTransactions();

                setTransactions(response);

            } catch (error) {
                console.log("Failed to load live transactions", error);
            }
        }

        loadData();

        const interval = setInterval(loadData, 2000);

        return () => clearInterval(interval);

    }, []);

    function riskColor (score) {
        if (score >= 75) return "critical";
        if (score >= 65) return "high";
        if (score >= 40) return "medium";
        return "low";
    }

    function statusColor (status) {
        switch(status) {
            case "APPROVED":
                return "approved-text";
            case "REVIEW":
                return "review-text";
            case "FLAGGED":
                return "flagged-text";
            case "BLOCKED":
                return "blocked-text";
            default:
                return "";
        }
    }

    return (
        <div className="live-container">
            <div className="live-header">
                <h3>LIVE TRANSACTIONS</h3>
            </div>

            <div className="table-container">
                <table className="transaction-table">
                    <thead>
                        <tr>
                            <th>Timestamp</th>
                            <th>Customer</th>
                            <th>Merchant</th>
                            <th>Amount</th>
                            <th>Country</th>
                            <th>Device</th>
                            <th>Risk Score</th>
                            <th>Status</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody>

                    {transactions.map((txn)=>(
                        <tr key={txn.transaction_id}>
                            <td>{new Date(txn.timestamp).toLocaleDateString()}</td>
                            <td>
                                <div className="customer-name">{txn.customer_name}</div>
                                <small>{txn.customer_id}</small>
                            </td>
                            <td>{txn.merchant}</td>
                            <td>£{Number(txn.amount).toFixed(2)}</td>
                            <td>{txn.country}</td>
                            <td>{txn.device}</td>
                            <td><span className={`risk ${riskColor(txn.risk_score)}`}>{txn.risk_score}</span></td>
                            <td><span className={statusColor(txn.status)}>{txn.status}</span></td>
                            <td><button className="inspect-button" onClick={() => setSelectedTxn(txn)}>Inspect</button></td>
                        </tr>
                    ))}
                    </tbody>
                </table>
            </div>

            <SlidePanel transaction={selectedTxn} onClose={() => setSelectedTxn(null)} />
        </div>
    )
}

export default LiveTransactions;