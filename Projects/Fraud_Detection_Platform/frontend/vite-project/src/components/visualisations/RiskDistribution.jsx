import { useEffect, useState } from "react";
import { PieChart, Pie, Cell } from "recharts";

import { getTransactionsByRisk } from "../../api/fraudApi";

function RiskDistribution() {
    const [data, setData] = useState([]);
    const [total, setTotal] = useState(0);

    useEffect(() => {
        async function loadData() {
            try {
                const response = await getTransactionsByRisk();

                const totalTransactions = response.reduce((sum, item) => sum + item.count, 0);

                setTotal(totalTransactions);

                const colours = {LOW: "#22c55e", MEDIUM: "#eab308", HIGH: "#f97316", CRITICAL: "#ef4444"};
                const ranges = {LOW: "0-25",MEDIUM: "26-50", HIGH: "51-69", CRITICAL: "70-100"};

                const formatted = response.map(item => ({
                        name: item.risk_level.charAt(0) + item.risk_level.slice(1).toLowerCase(),
                        originalKey: item.risk_level,
                        value: item.count,
                        color: colours[item.risk_level],
                        range: ranges[item.risk_level]}));

                const order = {
                    CRITICAL: 1,
                    HIGH: 2,
                    MEDIUM: 3,
                    LOW: 4};
                
                formatted.sort((a, b) => order[a.originalKey] - order[b.originalKey]);

                setData(formatted);

            } catch (error) {
                console.log("Failed to load risk data", error);
            }
        }

        loadData();

        const interval = setInterval(loadData, 2000);

        return () => clearInterval(interval);
    }, []);

    return (
        <div className="risk-container">
            <h3 className="risk-title">FRAUD ANALYTICS</h3>
            <p className="risk-subtitle">Transactions by Risk Score</p>

            <div className="risk-content">
                <div className="donut-wrapper">
                    <PieChart width={200} height={200}>
                        <Pie
                            data={data}
                            innerRadius={60}
                            outerRadius={90}
                            dataKey="value"
                            startAngle={90}
                            endAngle={-270}
                            paddingAngle={1}
                        >
                            {data.map((entry, i) => (<Cell key={i} fill={entry.color} stroke="none"/>))}
                        </Pie>
                    </PieChart>

                    <div className="donut-center">
                        <div className="donut-total">{total}</div>
                        <div className="donut-total-label">Total</div>
                    </div>
                </div>

                <div className="risk-legend">
                    {data.map((entry, i) => (
                        <div key={i} className="risk-legend-row">
                            <div className="risk-legend-key">
                                <span
                                    className="risk-legend-swatch"
                                    style={{ backgroundColor: entry.color }}
                                />
                                <span className="risk-legend-label">
                                    {entry.name} ({entry.range})
                                </span>
                            </div>

                            <span className="risk-legend-percent">
                                {(entry.value / total * 100).toFixed(1)}%
                            </span>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
}

export default RiskDistribution;