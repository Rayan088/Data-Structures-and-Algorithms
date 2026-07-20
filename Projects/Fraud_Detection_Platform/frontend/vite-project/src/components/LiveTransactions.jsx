import { useEffect, useState } from "react";
import { getLiveTransactions } from "../api/fraudApi";
import SlidePanel from "./SlidePanel";

import gbpFlag from "../assets/united-kingdom-flag.png"
import usaFlag from "../assets/usa-flag.png"
import uaeFlag from "../assets/uae-flag.png"
import franceFlag from "../assets/france-flag.png"
import germanyFlag from "../assets/germany-flag.png"
import spainFlag from "../assets/spain-flag.png"
import brazilFlag from "../assets/brazil-flag.png"

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

        const interval = setInterval(loadData, 2500);

        return () => clearInterval(interval);

    }, []);

    const countryFlags = {
        "United Kingdom": gbpFlag,
        "United States": usaFlag,
        "UAE": uaeFlag,
        "France": franceFlag,
        "Germany": germanyFlag,
        "Spain": spainFlag,
        "Brazil": brazilFlag,
    };

    function getCountryFlag(country) {
        return countryFlags[country]
    }

    function riskColor (score) {
        if (score >= 70) return "critical";
        if (score >= 50) return "high";
        if (score >= 25) return "medium";
        return "low";
    }

    function riskLevelColor (risk_level) {
        if (risk_level === "LOW") return "approved-text"
        if (risk_level === "MEDIUM") return "review-text"
        if (risk_level === "HIGH") return "high-text"
        if (risk_level === "CRITICAL") return "blocked-text"
    }

    function statusColor (status) {
        switch(status) {
            case "APPROVED":
                return "approved-text";
            case "REVIEW":
                return "review-text";
            case "BLOCKED":
                return "blocked-text";
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
                                <small>CUS-{txn.customer_id}</small>
                            </td>
                            <td>{txn.merchant}</td>
                            <td>£{Number(txn.amount).toFixed(2)}</td>
                            <td>
                                <div className="country-cell">
                                    <img className="country-flag" src={getCountryFlag(txn.country)} alt={`${txn.country} flag`}/>
                                    <span className="country-text">{txn.country}</span>
                                </div>
                            </td>
                            <td>{txn.device}</td>
                            <td><span className={`risk ${riskColor(txn.risk_score)}`}>{txn.risk_score}</span>
                            <span className={riskLevelColor(txn.risk_level)} style={{marginLeft: "7px"}}>{txn.risk_level}</span></td>
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