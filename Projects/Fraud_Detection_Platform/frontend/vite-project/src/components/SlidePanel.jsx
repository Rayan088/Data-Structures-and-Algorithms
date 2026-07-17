function SlidePanel({ transaction, onClose }) {
    if (!transaction) return null;

    return (
        <>
            <div className="slide-overlay" onClick={onClose} />
            <div className="slide-panel">
                <div className="slide-header">
                    <h3>Transaction Details</h3>
                    <button className="slide-close" onClick={onClose}>✕</button>
                </div>

                <div className="slide-body">
                    <div className="slide-row">
                        <span className="slide-label">Transaction ID</span>
                        <span>{transaction.transaction_id}</span>
                    </div>
                    <div className="slide-row">
                        <span className="slide-label">Customer</span>
                        <span>{transaction.customer_name} ({transaction.customer_id})</span>
                    </div>
                    <div className="slide-row">
                        <span className="slide-label">Merchant</span>
                        <span>{transaction.merchant}</span>
                    </div>
                    <div className="slide-row">
                        <span className="slide-label">Amount</span>
                        <span>£{Number(transaction.amount).toFixed(2)}</span>
                    </div>
                    <div className="slide-row">
                        <span className="slide-label">Country</span>
                        <span>{transaction.country}</span>
                    </div>
                    <div className="slide-row">
                        <span className="slide-label">Device</span>
                        <span>{transaction.device}</span>
                    </div>
                    <div className="slide-row">
                        <span className="slide-label">Risk Score</span>
                        <span>{transaction.risk_score}</span>
                    </div>
                    <div className="slide-row">
                        <span className="slide-label">Status</span>
                        <span>{transaction.status}</span>
                    </div>
                </div>

                <div className="slide-actions">
                    <button className="approve-btn">Approve</button>
                    <button className="decline-btn">Decline</button>
                </div>
            </div>
        </>
    );
}

export default SlidePanel;