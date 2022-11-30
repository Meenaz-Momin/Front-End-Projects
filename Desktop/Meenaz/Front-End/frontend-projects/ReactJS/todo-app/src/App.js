import "./index.css";
import { useState } from "react";

function App() {
  const [list, setList] = useState([]);
  const [input, setInput] = useState("");

  const handleChange = (e) => {
    setInput(e.target.value);
  };

  const handleClick = () => {
    const newList = list.concat(input);
    setList(newList);
    setInput("");
  };
  const handleDelete = (value) => {
    setList(list.filter((item) => item !== value));
  };

  return (
    <div className="container">
      <h1 className="heading">Todo List</h1>
      <div className="display">
        <input
          onChange={handleChange}
          type="text"
          id="input"
          value={input}
          placeholder="Enter yout todo"
        />
        <button className="btn" onClick={handleClick}>
          Add
        </button>
      </div>
      <div className="list"></div>
      <ul>
        {list.map((value, i) => {
          return (
            <li className="list" key={i}>
              {value}
              <button className="close" onClick={() => handleDelete(value)}>
                X
              </button>
            </li>
          );
        })}
      </ul>
    </div>
  );
}

export default App;
