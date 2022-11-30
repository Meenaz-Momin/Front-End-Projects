import { useContext } from "react";
import EmpContext from "./Context";

function Input() {
  const { input } = useContext(EmpContext);
  const { handleInputChange } = useContext(EmpContext);
  const { handleSubmit } = useContext(EmpContext);

  return (
    <div className="user-input">
      <div className="input">
        Enter employee id:
        <br />
        <input
          type="text"
          id="id"
          name="id"
          value={input.id}
          onChange={handleInputChange}
        />
        <br />
      </div>

      <div className="input">
        Enter your name:
        <br />
        <input
          type="text"
          id="name"
          name="name"
          value={input.name}
          onChange={handleInputChange}
        />
        <br />
      </div>

      <div className="input">
        Enter your mobile number:
        <br />
        <input
          type="text"
          id="number"
          name="number"
          value={input.number}
          onChange={handleInputChange}
        />
        <br />
      </div>

      <div className="input">
        Enter your designation:
        <br />
        <input
          type="text"
          id="designation"
          name="designation"
          value={input.designation}
          onChange={handleInputChange}
        />
        <br />
      </div>

      <div className="input">
        Enter your address:
        <br />
        <input
          type="text"
          id="address"
          name="address"
          value={input.address}
          onChange={handleInputChange}
        />
        <br />
      </div>
      <div className="input">
        <button className="btn" onClick={handleSubmit}>
          Submit
        </button>
      </div>
    </div>
  );
}

export default Input;
