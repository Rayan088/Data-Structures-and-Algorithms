import Wallet from "./components/Wallet";
import OrderBook from "./components/OrderBook";
import Trades from "./components/Trades";
import OrderForm from "./components/OrderForm";
import UserOrders from "./components/UserOrders";
import MarketStats from "./components/MarketStats";

function App() {

    return (
        <div>

            <h1>Mini Exchange</h1>

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