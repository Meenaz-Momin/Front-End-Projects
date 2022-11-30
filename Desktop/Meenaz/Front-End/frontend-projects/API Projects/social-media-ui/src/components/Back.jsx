import { FaArrowAltCircleLeft } from "react-icons/fa";
import { Link } from "react-router-dom";

function BackButton({ url }) {
  return (
    <Link to={url} className="btn btn-back">
      <FaArrowAltCircleLeft style={{ marginRight: "5px" }} /> Back
    </Link>
  );
}

export default BackButton;
