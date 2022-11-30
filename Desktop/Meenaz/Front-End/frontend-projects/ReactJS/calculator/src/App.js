import React, { useState } from "react";
import "./App.css";

function App() {
  const [result, setResult] = useState("");

  const handleClick = (e) => {
    setResult(result.concat(e.target.name));
  };

  const clear = () => {
    setResult("");
  };

  const equal = () => {
    try {
      setResult(eval(result).toString());
    } catch (err) {
      setResult("ERROR");
    }
  };

  return (
    <>
      <h1 className="heading"> Calculator</h1>
      <div className="box">
        <div className="display">
          <input type="text" value={result} />
        </div>
        <div className="key">
          <p>
            <button name="(" onClick={handleClick} className="btn">
              (
            </button>
            <button name=")" onClick={handleClick} className="btn">
              )
            </button>
            <button name="/" onClick={handleClick} className="btn">
              /
            </button>
            <button onClick={clear} className="btn red" id="clear">
              C
            </button>
          </p>
          <p>
            <button name="7" onClick={handleClick} className="btn">
              7
            </button>
            <button name="8" onClick={handleClick} className="btn">
              8
            </button>
            <button name="9" onClick={handleClick} className="btn">
              9
            </button>
            <button name="*" onClick={handleClick} className="btn">
              *
            </button>
          </p>
          <p>
            <button name="4" onClick={handleClick} className="btn">
              4
            </button>
            <button name="5" onClick={handleClick} className="btn">
              5
            </button>
            <button name="6" onClick={handleClick} className="btn">
              6
            </button>
            <button name="-" onClick={handleClick} className="btn">
              -
            </button>
          </p>
          <p>
            <button name="1" onClick={handleClick} className="btn">
              1
            </button>
            <button name="2" onClick={handleClick} className="btn">
              2
            </button>
            <button name="3" onClick={handleClick} className="btn">
              3
            </button>
            <button name="+" onClick={handleClick} className="btn">
              +
            </button>
          </p>
          <p>
            <button name="0" onClick={handleClick} className="btn">
              0
            </button>
            <button name="00" onClick={handleClick} className="btn">
              00
            </button>
            <button name="." onClick={handleClick} className="btn">
              .
            </button>
            <button onClick={equal} className="btn">
              =
            </button>
          </p>
        </div>
      </div>
    </>
  );
}

export default App;
