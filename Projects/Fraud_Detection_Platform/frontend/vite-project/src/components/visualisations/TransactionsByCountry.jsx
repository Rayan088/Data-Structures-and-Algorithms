import { useEffect, useState } from "react";
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Cell, LabelList } from "recharts";
import { getTransactionsByCountry } from "../../api/fraudApi";

function LeftAlignedTick({y, payload }) {
    return (
        <text x={0} y={y} dy={4} textAnchor="start" fill="white" fontSize={13}>
            {payload.value}
        </text>
    );
}

function TransactionsByCountry() {
    const [countries, setCountries] = useState([]);

    useEffect(() => {
        async function loadData() {
            try {
                const response = await getTransactionsByCountry();

                const total = response.reduce((sum, item) => sum + item.count, 0);

                const formatted = response
                    .map(item => ({
                        country: item.country,
                        count: item.count,
                        percent: Number(((item.count / total) * 100).toFixed(1)),
                    }))
                    .sort((a, b) => b.count - a.count);

                setCountries(prev => {
                    const isSame = JSON.stringify(prev) === JSON.stringify(formatted);
                    return isSame ? prev : formatted;
                });
            } catch (error) {
                console.log("Failed to load transactions by country", error);
            }
        }

        loadData();

        const interval = setInterval(loadData, 2000);

        return () => clearInterval(interval);
    }, []);

    return (
        <div className="country-container">
            <h3 className="country-title">Transactions by Country</h3>

            <BarChart
                width={420}
                height={Math.max(countries.length * 40, 160) + 30}
                data={countries}
                layout="vertical"
                margin={{ top: 5, right: 30, left: -10, bottom: 5 }}
            >
                <CartesianGrid stroke="#334155" horizontal={false} />
                <XAxis
                    type="number"
                    domain={[0, 100]}
                    tickFormatter={(value) => `${value}%`}
                    tick={{ fill: "#94a3b8", fontSize: 12 }}
                    axisLine={{ stroke: "#334155" }}
                    tickLine={{ stroke: "#334155" }}
                />
                <YAxis
                    type="category"
                    dataKey="country"
                    width={153}
                    tick={<LeftAlignedTick/>}
                    axisLine={{ stroke: "#334155" }}
                    tickLine={false}
                />
                <Bar dataKey="percent" radius={[0, 4, 4, 0]} barSize={16} isAnimationActive={false}>
                    {countries.map((entry, i) => (
                        <Cell key={i} fill="#3b82f6" />
                    ))}
                    <LabelList
                        dataKey="percent"
                        position="right"
                        formatter={(value) => `${value}%`}
                        fill="#94a3b8"
                        fontSize={13}
                    />
                </Bar>
            </BarChart>
        </div>
    );
}

export default TransactionsByCountry;