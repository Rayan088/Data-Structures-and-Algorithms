import { useEffect, useState } from "react";
import { placeOrder, getWallet } from "../api/exchange";

function OrderForm() {

    const [side, setSide] = useState("BUY");
    const [price, setPrice] = useState("");
    const [qty, setQty] = useState("");
    const [wallet, setWallet] = useState({btc: 0, usd: 0});

    useEffect(() => {

        async function loadWallet() {
            const data = await getWallet();
            setWallet(data);
        }

        loadWallet();

        const interval = setInterval(loadWallet, 2000);
        return () => clearInterval(interval);

    }, []);

    const total = price && qty ? (parseFloat(price) * parseFloat(qty)).toFixed(2) : "0.00"

    function applyPct(pct) {
        if (side === "BUY") {
            const maxQty = wallet.usd / parseFloat(price || 1);
            setQty((maxQty * pct / 100).toFixed(6));
        } else {
            setQty((wallet.btc * pct / 100).toFixed(6));
        }
    }

    async function submit() {
        if (!price || !qty) return;
        await placeOrder({side, price, quantity: qty});
    }

    return (
        <div>
            <h2 className="panel-title">PLACE ORDER</h2>

            <div className="of-wrap">
                <div className="of-side-toggle">
                    <button
                        className={`of-side-btn buy ${side === "BUY" ? "active" : ""}`}
                        onClick={() => setSide("BUY")}>
                        Buy
                    </button>
                    <button
                        className={`of-side-btn sell ${side === "SELL" ? "active" : ""}`}
                        onClick={() => setSide("SELL")}
                    >
                        Sell
                    </button>
                </div>

                <div className="of-section">
                    <label className="of-label">Order Type</label>
                    <div className="of-type-bar">
                        <span className="of-type-btn active">Market</span>
                    </div>
                </div>

                <div className="of-section">
                    <label className="of-label">Price (USD)</label>
                    <input
                        className="of-input"
                        type="number"
                        placeholder="0.00"
                        value={price}
                        onChange={(e) => setPrice(e.target.value)}
                    />
                </div>

                <div className="of-section">
                    <label className="of-label">Quantity (BTC)</label>
                    <input
                        className="of-input"
                        type="number"
                        placeholder="0.000000"
                        value={qty}
                        onChange={(e) => setQty(e.target.value)}
                    />
                </div>

                <div className="of-pct-row">
                    {[25, 50, 75, 100].map(p => (
                        <button key={p} className="of-pct-btn" onClick={() => applyPct(p)}>
                            {p}%
                        </button>
                    ))}
                </div>

                <div className="of-total-row">
                    <span className="of-label">Total (USD)</span>
                    <span className="of-total-value">${total}</span>
                </div>

                <button className={`of-submit ${side === "BUY" ? "buy" : "sell"}`} onClick={submit}>
                    {side === "BUY" ? "Buy BTC" : "Sell BTC"}
                </button>

                <div className="of-balance">
                    <div className="of-balance-row">
                        <span>Available USD</span>
                        <span>${wallet.usd?.toLocaleString()}</span>
                    </div>
                    <div className="of-balance-row">
                        <span>Available BTC</span>
                        <span>{wallet.btc?.toFixed(6)}</span>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default OrderForm;