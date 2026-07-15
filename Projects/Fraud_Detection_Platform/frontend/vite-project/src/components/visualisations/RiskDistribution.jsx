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
        <div
            style={{fontFamily: "sans-serif"}}>
            <h3 style={{ margin: 0, fontSize: 19, fontWeight: 700, marginTop: -9}}>FRAUD ANALYTICS</h3>

            <p style={{margin: "4px 0 16px", fontSize: 17, marginTop: 10}}>Transactions by Risk Score</p>
            <div style={{display: "flex", alignItems: "center", gap: 24}}>

                <div
                    style={{
                        position: "relative",
                        width: 200,
                        height: 200,
                        flexShrink: 0
                    }}
                    >
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

                    <div
                        style={{
                            position: "absolute",
                            top: "50%",
                            left: "50%",
                            transform: "translate(-50%, -50%)",
                            textAlign: "center"
                        }}
                    >
                        <div style={{fontSize: 20, fontWeight: 700}}>{total}</div>
                        <div style={{fontSize: 15}}>Total</div>
                    </div>
                </div>

                <div
                    style={{display: "flex", flexDirection: "column", gap: 20}}>

                    {data.map((entry, i) => (
                            <div key={i} style={{
                                    display: "flex", alignItems: "center", justifyContent: "space-between", gap: 16, fontSize: 16}}>
                                
                                <div style={{display: "flex", alignItems: "center", gap: 8}}>
                                    <span style={{width: 10, height: 10, backgroundColor: entry.color, display: "inline-block"}}/>

                                    <span style={{fontSize: 15.3}}>
                                        {entry.name} {" "} ({entry.range})
                                    </span>
                                </div>

                                <span style={{color: "white"}}>
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