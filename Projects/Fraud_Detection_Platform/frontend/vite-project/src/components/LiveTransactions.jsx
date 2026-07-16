import { useEffect, useState } from "react";
import { getLiveTransactions } from "../api/fraudApi";

function LiveTransactions() {
    const [transactions, setTransactions] = useState([]);

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

    function riskColor(score) {
        if (score >= 86) return "critical";
        if (score >= 70) return "high";
        if (score >= 40) return "medium";
        return "low";
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
                        </tr>
                    </thead>
                    <tbody>

                    {transactions.map((txn)=>(
                        <tr key={txn.transaction_id}>
                            <td>{txn.timestamp}</td>
                            <td>
                                <div>{txn.customer_name}</div>
                                <small>{txn.customer_id}</small>
                            </td>
                            <td>{txn.merchant}</td>
                            <td>£{Number(txn.amount).toFixed(2)}</td>
                            <td>{txn.country}</td>
                            <td>{txn.device}</td>
                            <td><span className={`risk ${riskColor(txn.risk_score)}`}>{txn.risk_score}</span></td>
                            <td>{txn.status}</td>
                        </tr>
                    ))}
                    </tbody>
                </table>
            </div>
        </div>
    )
}

export default LiveTransactions;