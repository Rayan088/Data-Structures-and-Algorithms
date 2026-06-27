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
        <div className="uo-wrap">
            <div className="uo-title-row">
                <h2 className="panel-title">OPEN ORDERS</h2>
            </div>

            <div className="uo-table-wrap">
                <table className="uo-table">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Side</th>
                            <th>Price (USD)</th>
                            <th>Qty (BTC)</th>
                            <th>Filled</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        {orders.map((o, i) => {
                            const isBuy = o.side?.toUpperCase() === "BUY";
                            const isOpen = o.status?.toUpperCase() === "OPEN";
                            return (
                                <tr key={i} className="uo-row">
                                    <td>{o.id}</td>
                                    <td className={isBuy ? "uo-buy" : "uo-sell"}>{o.side}</td>
                                    <td>{o.price?.toLocaleString()}</td>
                                    <td>{o.qty}</td>
                                    <td>{o.filled}</td>
                                    <td className={isOpen ? "uo-open" : "uo-muted"}>{o.status}</td>
                                </tr>
                            );
                        })}
                    </tbody>
                </table>
            </div>
        </div>
    );
}

export default UserOrders;