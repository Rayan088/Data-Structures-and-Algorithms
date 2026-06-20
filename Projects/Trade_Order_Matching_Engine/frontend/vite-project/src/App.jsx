import Wallet from "./components/Wallet";
import OrderBook from "./components/OrderBook";
import Trades from "./components/Trades";
import OrderForm from "./components/OrderForm";
import UserOrders from "./components/UserOrders";
import MarketStats from "./components/MarketStats";
import LiveStats from "./components/LiveStats";

function App() {

    return (
        <div>

            <h1>Mini Exchange</h1>
            <LiveStats />

            <MarketStats />
            <OrderBook />
            <Wallet />

            <OrderForm />

            <UserOrders />

            <Trades />

        </div>
    );
}

export default App;