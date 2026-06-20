import { useEffect, useState } from "react";
import { getWallet } from "../api/exchange";

function Wallet() {
    const [wallet, setWallet] = useState({
        btc: 0,
        usd: 0
    })

    useEffect(() => {
        async function loadWallet() {
            const data = await getWallet()
            setWallet(data)
        }

        loadWallet()
    }, [])

    return (
        <div>
            <p>Wallet</p>
            <p>BTC: {wallet.btc}</p>
            <p>USD: {wallet.usd}</p>
        </div>
    )
}

export default Wallet;