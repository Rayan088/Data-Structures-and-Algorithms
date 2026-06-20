import { useEffect, useState } from "react";
import { getStats } from "../api/exchange";

function MarketStats() {
    const [stats, setStats] = useState({
        mean_price: 0,
        spread: 0
    });

    useEffect(() => {
        async function load() {
            const res = await getStats();
            setStats(res);
        }

        load();

        const interval = setInterval(load, 2000);
        return () => clearInterval(interval);

    }, []);

    return (
        <div>
            <h2>Market Stats</h2>
            <p>Mean Price: {stats.mean_price}</p>
            <p>Spread: {stats.spread}</p>
        </div>
    );
}

export default MarketStats;