import { useEffect, useState } from "react";
import { placeOrder, getWallet } from "../api/exchange";

function OrderForm() {

    const [side, setSide] = useState("BUY");
    const [price, setPrice] = useState("");
    const [qty, setQty] = useState("");

    const [wallet, setWallet] = useState({
        btc: 0,
        usd: 0
    });

    useEffect(() => {

        async function loadWallet() {
            const data = await getWallet();
            setWallet(data);
        }

        loadWallet();

        const interval = setInterval(loadWallet, 2000);
        return () => clearInterval(interval);

    }, []);

    async function submit() {
        await placeOrder({
            side,
            price,
            quantity: qty
        });

        alert("Order placed");
    }

    return (
        <div>

            <h2>Place Order</h2>
            
            <select value={side} onChange={(e) => setSide(e.target.value)}>
                <option>BUY</option>
                <option>SELL</option>
            </select>

            <input
                placeholder="Price"
                onChange={(e) => setPrice(e.target.value)}
            />

            <input
                placeholder="Quantity"
                onChange={(e) => setQty(e.target.value)}
            />

            <button onClick={submit}>
                Submit
            </button>

            <div style={{ marginBottom: "10px" }}>
                <p>BTC: {wallet.btc}</p>
                <p>USD: {wallet.usd}</p>
            </div>

        </div>
    );
}

export default OrderForm;