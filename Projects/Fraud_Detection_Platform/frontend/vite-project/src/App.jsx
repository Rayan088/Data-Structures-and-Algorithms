import "./App.css";

import { useEffect, useState } from "react";

import StatCard from "./components/headerAnalytics/StatCard";

import LiveTransactions from "./components/LiveTransactions";

import RiskDistribution from "./components/visualisations/RiskDistribution";
import TransactionsByCountry from "./components/visualisations/TransactionsByCountry";
import FraudByRule from "./components/visualisations/FraudByRule";
import RiskiestCustomers from "./components/visualisations/RiskiestCustomers";

import transactionsIcon from "./assets/wallet-icon.png"
import riskIcon from "./assets/risk-icon.png"
import reviewIcon from "./assets/accounts-icon.png"
import preventedIcon from "./assets/prevented-icon.png"

import {getTotalTransactions, getHighRiskAlerts, getTransactionsAwaitingReview, getFraudPrevented} from "./api/fraudApi";

function App() {
    const [totalTransactions, setTotalTransactions] = useState(0);
    const [highRiskAlerts, setHighRiskAlerts] = useState(0);
    const [awaitingReview, setAwaitingReview] = useState(0);
    const [fraudPrevented, setFraudPrevented] = useState(0);

    useEffect(() => {
        async function loadAnalytics() {
            try {
                const total = await getTotalTransactions();
                const alerts = await getHighRiskAlerts();
                const review = await getTransactionsAwaitingReview();
                const prevented = await getFraudPrevented();

                setTotalTransactions(total.total_transactions);
                setHighRiskAlerts(alerts.high_risk_alerts);
                setAwaitingReview(review.transactions_awaiting_review);
                setFraudPrevented(prevented.fraud_prevented);
            }

            catch (error) {
                console.log(error);
            }
        }

        loadAnalytics();

        const interval = setInterval(loadAnalytics, 1000)

        return () => clearInterval(interval);
    }, []);

    return (
        <div className="dashboard">
            <div className="headerAnalytics">
                <div className="stat-card transactions-processed">
                    <StatCard
                        title="Transactions Processed"
                        value={totalTransactions}
                        image={transactionsIcon}/>
                </div>

                <div className="stat-card risk-alerts">
                    <StatCard
                        title="High Risk Alerts"
                        value={highRiskAlerts}
                        image={riskIcon}/>
                </div>

                <div className="stat-card awaiting-review">
                    <StatCard
                        title="Transactions Awaiting Review"
                        value={awaitingReview}
                        image={reviewIcon}/>
                </div>

                <div className="stat-card fraud-prevented">
                    <StatCard
                        title="Fraud Prevented (£)"
                        value={`£${fraudPrevented.toLocaleString()}`}
                        image={preventedIcon}/>
                </div>
            </div>

            <div className="card transactions">
                <LiveTransactions />
            </div>

            <div className="visualisations">
                <div className="card">
                    <RiskDistribution />
                </div>

                <div className="card">
                    <RiskiestCustomers />
                </div>

                <div className="card">
                    <TransactionsByCountry />
                </div>

                <div className="card">
                    <FraudByRule />
                </div>
            </div>
        </div>
    );
}

export default App;