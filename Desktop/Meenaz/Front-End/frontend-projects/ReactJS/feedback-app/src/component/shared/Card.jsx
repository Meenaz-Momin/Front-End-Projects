import PropTypes from 'prop-types';

function Card({ children, reverse }) {
  return <div className="card">{children}</div>;
}

Card.defaulProps = {
  reverse : false,
}

Card.propTypes = {
  children: PropTypes.node.isRequired,
  reverse: PropTypes.bool,
}

export default Card;
