import { useEffect, useState } from "react";
import {
    getCustomerProfile,
    getRecentTransactions,
    getTransactionAlerts,
    
} from "../api/fraudApi";
import "../styles/SlidePanel.css";

function SlidePanel({ transaction, onClose }) {
    const [profile, setProfile] = useState(null);
    const [recentTxns, setRecentTxns] = useState([]);
    const [alerts, setAlerts] = useState([]);

    useEffect(() => {
        if (!transaction) return;

        async function loadPanelData() {
            try {
                const [profileRes, recentRes, alertsRes] = await Promise.all([
                    getCustomerProfile(transaction.customer_id),
                    getRecentTransactions(transaction.customer_id),
                    getTransactionAlerts(transaction.transaction_id),
                ]);

                setProfile(profileRes);
                setRecentTxns(recentRes);
                setAlerts(alertsRes);

            } catch (error) {
                console.log("Failed to load panel data", error);
            }
        }

        loadPanelData();
    }, [transaction]);

    function statusColour (status) {
        if (status === "APPROVED") return "approved-colour"
        if (status ==="REVIEW") return "review-colour"
        if (status === "BLOCKED") return "blocked-colour"
    }

    function riskScoreColour (score) {
        if (score >= 75) return "blocked-colour";
        if (score >= 65) return "med-colour";
        if (score >= 40) return "review-colour";
        return "approved-colour";
    }

    if (!transaction) return null;

    return (
        <>
            <div className="slide-overlay" onClick={onClose} />
            <div className="slide-panel">
                <div className="slide-header">
                    <h3>Transaction Details</h3>
                    <button className="slide-close" onClick={onClose}>✕</button>
                </div>

                <div className="slide-body">
                    <div className="slide-row">
                        <span className="slide-label">Transaction ID</span>
                        <span>{transaction.transaction_id}</span>
                    </div>
                    <div className="slide-row">
                        <span className="slide-label">Customer</span>
                        <span>{transaction.customer_name} ({transaction.customer_id})</span>
                    </div>
                    <div className="slide-row">
                        <span className="slide-label">Merchant</span>
                        <span>{transaction.merchant}</span>
                    </div>
                    <div className="slide-row">
                        <span className="slide-label">Amount</span>
                        <span>£{Number(transaction.amount).toFixed(2)}</span>
                    </div>
                    <div className="slide-row">
                        <span className="slide-label">Country</span>
                        <span>{transaction.country}</span>
                    </div>
                    <div className="slide-row">
                        <span className="slide-label">Device</span>
                        <span>{transaction.device}</span>
                    </div>
                    <div className="slide-row">
                        <span className="slide-label">Risk Score</span>
                        <span className={`${riskScoreColour(transaction.risk_score)}`}>{transaction.risk_score}</span>
                    </div>
                    <div className="slide-row">
                        <span className="slide-label">Status</span>
                        <span className={`${statusColour(transaction.status)}`}>{transaction.status}</span>
                    </div>
                </div>

                {profile && (
                    <div className="panel-section">
                        <div className="section-title">Customer Overview</div>
                        <div className="section-row">
                            <span className="section-label">Home Country</span>
                            <span>{profile.home_country}</span>
                        </div>
                        <div className="section-row">
                            <span className="section-label">Average Spend</span>
                            <span>£{Number(profile.avg_spend).toFixed(2)}</span>
                        </div>
                    </div>
                )}

                {profile && (
                    <div className="panel-section trusted-devices">
                        <div className="section-title green">Trusted Devices ({profile.trusted_devices.length})</div>
                        {profile.trusted_devices.map((device, i) => (
                            <div key={i} className="device-row">
                                <span>{device}</span>
                            </div>
                        ))}
                    </div>
                )}

                {alerts.length > 0 && (
                    <div className="panel-section rules-broken">
                        <div className="section-title red">Rules Broken ({alerts.length})
                        </div>
                        {alerts.map((alert, i) => (
                            <div key={i} className="rule-row">
                                <span className="rule-icon">{alert.reason}</span>
                            </div>
                        ))}
                    </div>
                )}

                <div className="panel-section previous-transactions">
                    <div className="section-title">Previous Transactions</div>
                    <div className="prev-txn-header">
                        <span>Merchant</span>
                        <span>Amount</span>
                        <span>Time</span>
                    </div>
                    {recentTxns.map((txn, i) => (
                        <div key={i} className="prev-txn-row">
                            <div>
                                <div className="prev-txn-merchant">{txn.merchant}</div>
                                <div className="prev-txn-country">{txn.country}</div>
                            </div>
                            <span className="prev-txn-amount">£{Number(txn.amount).toFixed(2)}</span>
                            <div className="prev-txn-time">
                                <span>{new Date(txn.timestamp).toLocaleDateString()}</span>
                                <span className="prev-txn-device">{txn.device}</span>
                            </div>
                        </div>
                    ))}
                </div>

                <div className="slide-actions">
                    <button className="approve-btn">Approve</button>
                    <button className="decline-btn">Decline</button>
                </div>
            </div>
        </>
    );
}

export default SlidePanel;