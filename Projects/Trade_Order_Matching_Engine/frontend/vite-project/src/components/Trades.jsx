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

    return (
        <div>
            <h2>Trades</h2>

            {trades.map((t, i) => (
                <div key={i}>
                    {t.price} | {t.qty} | {t.side}
                </div>
            ))}
        </div>
    );
}

export default Trades;