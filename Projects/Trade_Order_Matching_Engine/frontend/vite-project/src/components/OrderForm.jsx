import { useState } from "react";
import { placeOrder } from "../api/exchange";

function OrderForm() {

    const [side, setSide] = useState("BUY");
    const [price, setPrice] = useState("");
    const [qty, setQty] = useState("");

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
        </div>
    );
}

export default OrderForm;