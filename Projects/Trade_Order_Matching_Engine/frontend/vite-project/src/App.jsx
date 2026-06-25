import "./App.css"

import OrderBook from "./components/OrderBook";
import Trades from "./components/Trades";
import OrderForm from "./components/OrderForm";
import UserOrders from "./components/UserOrders";
import LiveStats from "./components/LiveStats";

function App() {
    return (
        <div className="dashboard">

            <div className="card stats">
                <LiveStats />
            </div>

            <div className="card orderbook">
                <OrderBook />
            </div>

            <div className="card orderform">
                <OrderForm />
            </div>

            <div className="card userorders">
                <UserOrders />
            </div>

            <div className="card trades">
                <Trades />
            </div>

        </div>
    );
}

export default App;