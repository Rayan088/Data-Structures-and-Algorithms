import { useEffect, useState } from "react";
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Cell, LabelList } from "recharts";
import { getFraudByRule } from "../../api/fraudApi";

function toTitleCase(str) {
    return str.toLowerCase().split("_")
        .map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(" ");
}

function BottomAlignedTick({ x, y, payload }) {
    const words = toTitleCase(payload.value).split(" ");

    return (
        <text x={x} y={y} textAnchor="middle" fill="white" fontSize={13}>
            {words.map((word, i) => (
                <tspan key={i} x={x} dy={i === 0 ? 12 : 14}>{word}</tspan>))}
        </text>
    );
}

function FraudByRule() {
    const [rules, setRules] = useState([]);

    useEffect(() => {
        async function loadData() {
            try {
                const response = await getFraudByRule();

                const formatted = Object.entries(response)
                    .map(([rule, count]) => ({ rule, count }))
                    .sort((a, b) => b.count - a.count);

                setRules(prev => {
                    const isSame = JSON.stringify(prev) === JSON.stringify(formatted);
                    return isSame ? prev : formatted;
                });
            } catch (error) {
                console.log("Failed to load fraud by rule data", error);
            }
        }

        loadData();

        const interval = setInterval(loadData, 2000);

        return () => clearInterval(interval);
    }, []);

    return (
        <div className="rule-container">
            <h3 className="rule-title">Fraud By Rule</h3>

            <BarChart
                width={420}
                height={280}
                data={rules}
                layout="horizontal"
                margin={{ top: 20, right: 20, left: 0, bottom: 30 }}
            >
                <CartesianGrid stroke="#334155" vertical={false} />
                <XAxis
                    dataKey="rule"
                    tick={<BottomAlignedTick />}
                    axisLine={{ stroke: "#334155" }}
                    tickLine={false}
                    interval={0}
                />
                <YAxis
                    type="number"
                    tick={{ fill: "#94a3b8", fontSize: 12 }}
                    axisLine={{ stroke: "#334155" }}
                    tickLine={{ stroke: "#334155" }}
                />
                <Bar dataKey="count" radius={[4, 4, 0, 0]} barSize={30} isAnimationActive={false}>
                    {rules.map((entry, i) => (
                        <Cell key={i} fill="#3b82f6" />
                    ))}
                    <LabelList
                        dataKey="count"
                        position="top"
                        fill="#94a3b8"
                        fontSize={12}
                    />
                </Bar>
            </BarChart>
        </div>
    );
}

export default FraudByRule;