const API = "http://localhost:5000"

export async function getLiveTransactions() {
    const res = await fetch(`${API}/api/live-transactions`)
    return res.json();
}

export async function getTotalTransactions() {
    const res = await fetch(`${API}/api/analytics/total-transactions`)
    return res.json();
}

export async function getHighRiskAlerts() {
    const res = await fetch(`${API}/api/analytics/high-risk-alerts`)
    return res.json();
}

export async function getTransactionsAwaitingReview() {
    const res = await fetch(`${API}/api/analytics/transactions-awaiting-review`)
    return res.json()
}

export async function getFraudPrevented() {
    const res = await fetch(`${API}/api/analytics/fraud-prevented`)
    return res.json()
}

export async function getTransactionsByRisk() {
    const res = await fetch(`${API}/api/analytics/transactions-by-risk`)
    return res.json()
}

export async function getRiskiestCustomers() {
    const res = await fetch(`${API}/api/analytics/riskiest-customers`)
    return res.json()
}

export async function getTransactionsByCountry() {
    const res = await fetch(`${API}/api/analytics/transactions-by-country`)
    return res.json()
}

export async function getFraudByRule() {
    const res = await fetch(`${API}/api/analytics/fraud-by-rule`)
    return res.json()
}

export async function getRecentTransactions(customerId) {
    const res = await fetch(`${API}/api/customers/${customerId}/recent-transactions`)
    return res.json()
}

export async function getCustomerProfile(customerId) {
    const res = await fetch(`${API}/api/customers/${customerId}/profile`)
    return res.json()
}

export async function getTransactionAlerts(transactionId) {
    const res = await fetch(`${API}/api/transactions/${transactionId}/alerts`)
    return res.json()
}

export async function approveTransaction(id) {
    const res = await fetch(`${API}/api/transactions/${id}/approve`, {method: "PATCH"})
    return res.json()
}

export async function blockTransaction(id) {
    const res = await fetch(`${API}/api/transactions/${id}/block`, {method: "PATCH"})
    return res.json()
}