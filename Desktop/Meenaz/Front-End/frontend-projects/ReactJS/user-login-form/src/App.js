import "./index.css";
import { useState } from "react";
import Card from "./Card";
/*import { BrowserRouter as Router, Route, Routes } from "react-router-dom";*/
import { FaQuestion } from "react-icons/fa";

function App() {
  const [name, setName] = useState("");
  const [number, setNumber] = useState("");
  const [gmail, setGmail] = useState("");
  const [add, setAdd] = useState("");
  const [textnum, setTextnum] = useState("");
  const [textn, setTextn] = useState("");
  const [texta, setTexta] = useState("");
  const [textg, setTextg] = useState("");
  const [texts, setTexts] = useState("");

  const handleName = (e) => {
    if (name.length === 0) {
      setTextn("Name can not be empty");
    } else {
      setTextn("");
    }
    setName(e.target.value);
  };

  const handleNumber = (e) => {
    if (number.length > 10 || number.length < 9) {
      setTextnum("Number must contain 10 digits only!!!");
    } else {
      setTextnum("");
    }
    setNumber(e.target.value);
  };

  const handleAdd = (e) => {
    if (add.length === 0) {
      setTexta("Addess can not be empty");
    } else {
      setTexta("");
    }
    setAdd(e.target.value);
  };

  const handleGmail = (e) => {
    const pattern = new RegExp("^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$");
    if (!pattern.test(gmail)) {
      setTextg("Invalid Gmail");
    } else {
      setTextg("");
    }
    setGmail(e.target.value);
  };

  const handleClick = () => {
    if (texta === "" && textg === "" && textn === "" && textnum === "") {
      setAdd("");
      setGmail("");
      setName("");
      setNumber("");
      setTexts("");
      alert("Form has been submitted succesfully.....");
    } else {
      setTexts("Something is missing...");
    }
  };
  return (
    <div className="container">
      <h1>User Login Form </h1>
      <Card>
        <div className="input">
          Enter your name : <br />
          <input type="text" id="name" value={name} onChange={handleName} />
          <br />
          <div className="text">{textn}</div>
        </div>
      </Card>
      <Card>
        <div className="input">
          Enter your mobile number : <br />
          <input
            type="text"
            id="number"
            value={number}
            onChange={handleNumber}
          />
          <br />
          <div className="text">{textnum}</div>
        </div>
      </Card>
      <Card>
        <div className="input">
          Enter your valid gmail : <br />
          <input type="gmail" id="gmail" value={gmail} onChange={handleGmail} />
          <br />
          <div className="text">{textg}</div>
        </div>
      </Card>
      <Card>
        <div className="input">
          Enter your address : <br />
          <input type="text" id="add" value={add} onChange={handleAdd} /> <br />
          <div className="text">{texta}</div>
        </div>
      </Card>
      <input type="submit" id="btn" onClick={handleClick} />
      <div className="text">{texts}</div>
      <div className="about">
        <FaQuestion size={30} />
      </div>
    </div>
  );
}

export default App;
