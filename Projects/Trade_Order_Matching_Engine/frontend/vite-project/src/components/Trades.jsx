import { useEffect, useState } from "react";
import { getTrades } from "../api/exchange";

function Trades() {
    const [trades, setTrades] = useState([]);

    useEffect(() => {

        async function load() {
            const res = await getTrades();
            setTrades(res);
        }

        load();

        const interval = setInterval(load, 2000);
        return () => clearInterval(interval);
    }, []);

    // Function to format time into appropriate format
    const formatTime = (ts) => {
        if (!ts) return "—";
        return new Date(ts * 1000).toLocaleTimeString("en-GB", {
            hour: "2-digit",
            minute: "2-digit",
            second: "2-digit",
        });
    };

    return (
        <div className="ts-wrap">
            <h2 className="panel-title">Time & Sales</h2>

            <div className="ts-header-row">
                <span>Time</span>
                <span>Price (USD)</span>
                <span>Qty (BTC)</span>
            </div>

            {[...trades].slice(-100).reverse().map((t, i) => {
                const isBuy = t.side?.toLowerCase() === "buy";
                return (
                    <div key={i} className={`ts-row ${isBuy ? "ts-buy" : "ts-sell"}`}>
                        <span className="ts-time">{formatTime(t.time)}</span>
                        <span className="ts-price">{t.price?.toLocaleString() ?? t.price}</span>
                        <span className="ts-qty">{t.qty}</span>
                    </div>
                );
            })}
        </div>
    );
}

export default Trades;