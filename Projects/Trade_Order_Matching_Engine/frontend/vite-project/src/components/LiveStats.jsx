import { useEffect, useState } from "react";
import { getMarket } from "../api/exchange";

function LiveStats() {

    const [market, setMarket] = useState({
        asset: "BTC",
        current_price: 0,
        change_24h: 0,
        highlow: "0/0",
        volume: 0
    });

    useEffect(() => {
        async function load() {
            const data = await getMarket();
            setMarket(data);
        }

        load();

        const interval = setInterval(load, 500);
        return () => clearInterval(interval);

    }, []);

    return (
        <div className="market-bar">

            <div className="market-box">
                <span>Asset</span>
                <strong>{market.asset}</strong>
            </div>

            <div className="market-box">
                <span>Price</span>
                <strong>${market.current_price}</strong>
            </div>

            <div className="market-box">
                <span>24h Change</span>
                <strong style={{ color: market.change_24h > 0 ? "#22c55e" : "#ef4444" }}>
                    {market.change_24h}%
                </strong>
            </div>

            <div className="market-box">
                <span>High / Low</span>
                <strong>{market.highlow}</strong>
            </div>

            <div className="market-box">
                <span>24h Volume</span>
                <strong>{market.volume}</strong>
            </div>

        </div>
    );
}

export default LiveStats;