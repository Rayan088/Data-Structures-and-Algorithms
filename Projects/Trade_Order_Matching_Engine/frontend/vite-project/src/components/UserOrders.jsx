import { useEffect, useState } from "react";
import { getUserOrders } from "../api/exchange";

function UserOrders() {
    const [orders, setOrders] = useState([]);

    useEffect(() => {
        async function load() {
            const res = await getUserOrders();
            setOrders(res);
        }

        load();

        const interval = setInterval(load, 2000); // Executes every 2 seconds
        return () => clearInterval(interval); // Cleanup function when component is removed
    }, []);

    return (
        <div>
            <h2>YOUR ORDERS</h2>
            {orders.map((o, i) => (
                <div key={i}>
                    {o.id} | {o.side} | {o.price} | {o.qty} | {o.filled} | {o.status}
                </div>
            ))}
        </div>
    );
}

export default UserOrders;