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

        const interval = setInterval(load, 2000);
        return () => clearInterval(interval);

    }, []);

    return (
        <div>
            <h2>{market.asset} Market</h2>
            <p>Price: {market.current_price}</p>
            <p>24h Change: {market.change_24h}%</p>
            <p>High / Low: {market.highlow}</p>
            <p>Volume: {market.volume}</p>
        </div>
    );
}

export default LiveStats;