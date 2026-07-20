function StatCard({ title, value, image }) {
  return (
    <div className="stat-card-content">
      <img src={image} alt={title} className="stat-card-image" />

      <div className="stat-card-text">
        <h3>{title}</h3>
        <h1>{value}</h1>
      </div>
    </div>
  );
}

export default StatCard;