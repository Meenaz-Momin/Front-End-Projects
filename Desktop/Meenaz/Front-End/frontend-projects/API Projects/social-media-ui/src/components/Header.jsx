import { Link, useNavigate } from "react-router-dom";
import { FaSignInAlt, FaUser, FaSignOutAlt } from "react-icons/fa";
import { useSelector, useDispatch } from "react-redux";
import { logout } from "../features/auth/authSlice";
import { getMe } from "../features/users/userSlice";
import { toast } from "react-toastify";

function Header() {
  const { user } = useSelector((state) => state.auth);
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const userLogout = () => {
    dispatch(logout())
      .unwrap()
      .then(() => {
        navigate("/");
        toast.success("User Logged succecfully");
      })
      .catch(toast.error);
  };

  const Me = () => {
    dispatch(getMe()).unwrap().catch(toast.error);
  };

  return (
    <div className="header">
      <h1>Social Media</h1>
      <ul>
        {!user ? (
          <>
            <li>
              <Link to="/login">
                <FaSignInAlt style={{ marginRight: "5px" }} />
                Login
              </Link>
            </li>
            <li>
              <Link to="/register">
                <FaUser style={{ marginRight: "5px" }} />
                Register
              </Link>
            </li>
          </>
        ) : (
          <>
            <li>
              <Link to="/" onClick={userLogout}>
                <FaSignOutAlt style={{ marginRight: "5px" }} />
                Logout
              </Link>
            </li>
            <li>
              <Link to="/profile" onClick={Me}>
                <FaUser style={{ marginRight: "5px" }} />
                Go to Profile
              </Link>
            </li>
          </>
        )}
      </ul>
    </div>
  );
}

export default Header;
