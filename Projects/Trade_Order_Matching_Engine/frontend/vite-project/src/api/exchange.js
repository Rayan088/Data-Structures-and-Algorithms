const API = "http://localhost:5000";

export async function getMarket() {
    const res = await fetch(`${API}/market`);
    return res.json();
}

export async function getOrderBook() {
    const res = await fetch(`${API}/orderbook`)
    return res.json();
}

export async function getTrades(){
    const res = await fetch(`${API}/trades`);
    return res.json();
}

export async function getUserOrders(){
    const res = await fetch(`${API}/userorders`);
    return res.json();
}

export async function getWallet() {
    const res = await fetch(`${API}/wallet`)
    return res.json();
}

export async function getStats(){
    const res = await fetch(`${API}/stats`);
    return res.json();
}

export async function placeOrder(order){
    const res = await fetch(
        `${API}/order`,
        {
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify(order)
        }
    );
    return res.json();
}