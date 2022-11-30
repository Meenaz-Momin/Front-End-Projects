import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { toast } from "react-toastify";
import Back from "../components/Back";
import { useSelector, useDispatch } from "react-redux";
import { register } from "../features/auth/authSlice";

function Register() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const { isLoading } = useSelector((state) => state.auth);

  const [formData, setFormData] = useState({
    name: "",
    email: "",
    password: "",
  });

  const { name, email, password } = formData;

  const onChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const userRegister = (e) => {
    e.preventDefault();

    console.log("clicked");
    dispatch(register(formData))
      .unwrap()
      .then((user) => {
        toast.success(`Registered New User - ${user.data.name}`);
        navigate("/");
      })
      .catch(toast.error);
  };

  if (isLoading) {
    return <h1>Loading.......</h1>;
  }

  return (
    <div className="container">
      <div className="register">
        <div className="register1">
          <img
            src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6zkqnZKxJcsf7uE6f4ePAqWKsYxFYTergOg&usqp=CAU"
            alt="rgistration"
            className="register-image"
          />
        </div>

        <div className="register2">
          <div className="header">
            <h1>Register</h1>
          </div>

          <Back url="/" />
          <form className="form form-group">
            <div>
              <label htmlFor="name">Enter your name</label>
              <input
                type="text"
                name="name"
                value={name}
                onChange={onChange}
                required
              />
            </div>
            <div>
              <label htmlFor="email">Enter your email</label>
              <input
                type="email"
                name="email"
                value={email}
                onChange={onChange}
                required
              />
            </div>
            <div>
              <label htmlFor="password">Enter your password</label>
              <input
                type="password"
                name="password"
                value={password}
                onChange={onChange}
                required
              />
            </div>
            <button className="btn btn-block btn-submit" onClick={userRegister}>
              Register
            </button>
            <div className="msg">
              <p>already have an account?</p>
              <Link to="/login">login</Link>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Register;
