import './TrendItem.css';
import React from 'react';

function TrendItem(props) {
  const commify = (n) => {
    var parts = n.toString().split(".");
    const numberPart = parts[0];
    const decimalPart = parts[1];
    const thousands = /\B(?=(\d{3})+(?!\d))/g;
    return numberPart.replace(thousands, ",") + (decimalPart ? "." + decimalPart : "");
  }

  return (
    <div>
      <h2>{props.title}</h2>
      <p>{props.description}</p>
      <img src={props.imageUrl} alt={props.title} />
      <a className="trending" href="#">
        <span className="hashtag">#{props.hashtag}</span>
        <span className="count">#{commify(props.count)} cruds</span>
      </a>
    </div>
  );
}

export default TrendItem;
