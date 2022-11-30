import { useState } from "react";
import { toast } from "react-toastify";
import { Link, useNavigate } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import Back from "../components/Back";
import { login } from "../features/auth/authSlice";

function Login() {
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const { isLoading } = useSelector((state) => state.auth);

  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });
  const { email, password } = formData;
  const onChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const userLogin = (e) => {
    e.preventDefault();

    dispatch(login(formData))
      .unwrap()
      .then((user) => {
        toast.success(`User Logged in as ${user.data.name}`);
        navigate("/");
      })
      .catch(toast.error);
  };

  if (isLoading) {
    return <h1>Loading.....</h1>;
  }

  return (
    <div className="container">
      <div className="login">
        <div className="login1">
          <div className="header">
            <h1>Login</h1>
          </div>
          <Back url="/" />
          <form className="form form-group">
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
                required
                onChange={onChange}
              />
            </div>

            <button onClick={userLogin} className="btn btn-block btn-submit">
              Login
            </button>

            <div className="msg">
              <p>don't have an account?</p>
              <Link to="/register">create account</Link>
            </div>
          </form>
        </div>

        <div className="login2">
          <img
            src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQVZBVZQKdbJy59TQ0tJFWl8yo_3r6RP-zuIA&usqp=CAU"
            alt="login"
            className="login-image"
          />
        </div>
      </div>
    </div>
  );
}

export default Login;
