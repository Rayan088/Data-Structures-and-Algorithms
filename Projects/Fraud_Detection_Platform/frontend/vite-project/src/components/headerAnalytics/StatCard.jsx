function statCard({title, value, subtitle}) {
    return (
        <div>
            <h3>{title}</h3>
            <h1>{value}</h1>
            <p>{subtitle}</p>
        </div>
    )
}

export default statCard