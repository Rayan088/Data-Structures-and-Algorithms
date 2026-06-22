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

    // Duplicates into seperate 18 size array
    const asks = [...data.asks].slice(0, 100);
    const bids = [...data.bids].slice(0, 100);

    // Finds largest ask and bid
    const maxAskQty = Math.max(...asks.map(a => a.qty), 1);
    const maxBidQty = Math.max(...bids.map(b => b.qty), 1);

    // Calculating spread
    const spread = asks.length && bids.length
        ? (asks[0].price - bids[0].price).toFixed(2)
        : "—";

    // Calculating mid price
    const mid = asks.length && bids.length
        ? ((asks[0].price + bids[0].price) / 2).toFixed(2)
        : "—";

    return (
        <div className="ob-wrap">
            <h2 className="panel-title">Order Book</h2>

            <div className="ob-grid ob-header-row">
                <div className="ob-col-header ask-header">
                    <span>Price (USD)</span><span>Qty (BTC)</span>
                </div>
                <div className="ob-col-header bid-header">
                    <span>Price (USD)</span><span>Qty (BTC)</span>
                </div>
            </div>

            <div className="ob-grid ob-body">

                <div className="ob-side">
                    <div className="ob-side-label ask-label">SELL (ASKS)</div>
                    {asks.map((a, i) => (
                        <div key={i} className="ob-row ask-row">
                            <div
                                className="ob-fill ask-fill"
                                style={{ width: `${(a.qty / maxAskQty) * 100}%` }} // Visual bar based on quantity
                            />
                            <span className="ob-price ask-price">{a.price.toLocaleString()}</span>
                            <span className="ob-qty">{a.qty}</span>
                        </div>
                    ))}
                </div>

                <div className="ob-side">
                    <div className="ob-side-label bid-label">BUY (BIDS)</div>
                    {bids.map((b, i) => (
                        <div key={i} className="ob-row bid-row">
                            <div
                                className="ob-fill bid-fill"
                                style={{ width: `${(b.qty / maxBidQty) * 100}%` }}
                            />
                            <span className="ob-price bid-price">{b.price.toLocaleString()}</span>
                            <span className="ob-qty">{b.qty}</span>
                        </div>
                    ))}
                </div>
            </div>

            <div className="ob-spread-row">
                <span>SPREAD <strong>{spread} ({spread && bids[0] ? ((spread / bids[0].price) * 100).toFixed(2) : "—"}%)</strong></span>
                <span>MID PRICE <strong>{mid}</strong></span>
            </div>
        </div>
    );
}

export default OrderBook;