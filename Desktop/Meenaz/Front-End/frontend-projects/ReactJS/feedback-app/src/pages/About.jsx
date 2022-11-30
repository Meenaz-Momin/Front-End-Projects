import Card from "../component/shared/Card";
import { Link } from "react-router-dom";
function About() {
  return (
    <Card>
      <div className="about">
        <h1>About This Project</h1>
        <p> This is a react App to collect a feedback of a product </p>
        <Link to="/">Home</Link>
      </div>
    </Card>
  );
}

export default About;
