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

    return (
        <div style={{ fontFamily: "sans-serif" }}>
            <h3 style={{ margin: 0, fontSize: 19, fontWeight: 700 }}>Top 5 Highest Risk Customers</h3>

            <div style={{ marginTop: 16 }}>
                <div
                    style={{
                        display: "flex",
                        justifyContent: "space-between",
                        fontSize: 14,
                        color: "white",
                        paddingBottom: 8,
                        borderBottom: "1px solid #333",
                    }}>
                    <span style={{ flex: 1.2 }}>Customer ID</span>
                    <span style={{ flex: 2 }}>Customer Name</span>
                    <span style={{ flex: 1.5, textAlign: "right" }}>Highest Risk Score</span>
                </div>

                {customers.map((customer, i) => (
                    <div key={i}
                        style={{
                            display: "flex",
                            justifyContent: "space-between",
                            alignItems: "center",
                            padding: "10px 0",
                            borderBottom: "1px solid #222",
                            fontSize: 16,
                        }}>

                        <span style={{ flex: 1.2 }}>{customer.customer_id}</span>
                        <span style={{ flex: 2 }}>{customer.name}</span>
                        <span
                            style={{flex: 1.5, textAlign: "right",}}>
                            <span
                                style={{
                                    display: "inline-block",
                                    padding: "4px 12px",
                                    borderRadius: 5,
                                    fontWeight: 300,
                                    color: "white",
                                    backgroundColor:
                                        customer.risk_score >= 86 ? "#ef4444"
                                        : customer.risk_score >= 70 ? "#f97316"
                                        : customer.risk_score >= 40 ? "#eab308"
                                        : "#22c55e",
                                }}>
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