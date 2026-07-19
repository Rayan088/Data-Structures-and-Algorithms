import { useEffect, useState } from "react";
import { getRiskiestCustomers } from "../../api/fraudApi";

function TopRiskCustomers() {
    const [customers, setCustomers] = useState([]);

    useEffect(() => {
        async function loadData() {
            try {
                const response = await getRiskiestCustomers();
                setCustomers(response);
            } catch (error) {
                console.log("Failed to load top risk customers", error);
            }
        }

        loadData();

        const interval = setInterval(loadData, 2000);

        return () => clearInterval(interval);
    }, []);

    function riskClass(score) {
        if (score >= 86) return "critical";
        if (score >= 70) return "high";
        if (score >= 40) return "medium";
        return "low";
    }

    return (
        <div className="top-risk-container">
            <h3 className="top-risk-title">Top 5 Highest Risk Customers</h3>

            <div className="top-risk-table">
                <div className="top-risk-header">
                    <span className="col-id">Customer ID</span>
                    <span className="col-name">Customer Name</span>
                    <span className="col-score">Highest Risk Score</span>
                </div>

                {customers.map((customer, i) => (
                    <div key={i} className="top-risk-row">
                        <span className="col-id">CUS-{customer.customer_id}</span>
                        <span className="col-name">{customer.name}</span>
                        <span className="col-score">
                            <span className={`risk-badge ${riskClass(customer.risk_score)}`}>
                                {customer.risk_score}
                            </span>
                        </span>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default TopRiskCustomers;