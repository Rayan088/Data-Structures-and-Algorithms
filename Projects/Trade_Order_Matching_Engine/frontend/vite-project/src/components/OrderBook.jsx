import { useEffect, useState } from "react";
import { getOrderBook } from "../api/exchange";

function OrderBook() {
    const [data, setData] = useState({ bids: [], asks: [] });

    useEffect(() => {
        async function load() {
            const res = await getOrderBook();
            setData(res);
        }

        load();

        const interval = setInterval(load, 2000);
        return () => clearInterval(interval);
    }, []);

    return (
        <div>
            <h2>Order Book</h2>
            <div style={{ display: "flex", gap: "40px" }}>
                <div>
                    <h3>Bids</h3>
                    {data.bids.map((b, i) => (
                        <div key={i}>
                            {b.price} | {b.qty}
                        </div>
                    ))}
                </div>

                <div>
                    <h3>Asks</h3>
                    {data.asks.map((a, i) => (
                        <div key={i}>
                            {a.price} | {a.qty}
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
}

export default OrderBook;