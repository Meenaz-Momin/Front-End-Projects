import { useState } from "react";
import Modal from "react-modal";
import { toast } from "react-toastify";
import { useNavigate } from "react-router-dom";
import { useDispatch } from "react-redux";
import { updateUser } from "../features/users/userSlice";
// import { getAllPost, getMyPost } from "../features/post/PostSlice";

const customStyles = {
  content: {
    width: "600px",
    top: "50%",
    left: "50%",
    right: "auto",
    bottom: "auto",
    marginRight: "-50%",
    transform: "translate(-50%, -50%)",
    position: "relative",
  },
};

function InputForm({ name2, email2, description2 }) {
  const [formData, setFormData] = useState({
    name: name2,
    email: email2,
    description: description2,
  });

  const { name, email, description } = formData;

  const onChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const [modalIsOpen, setModalIsOpen] = useState(true);
  const closeModal = () => setModalIsOpen(false);

  const dispatch = useDispatch();
  const navigate = useNavigate();

  const handleUpdate = (e) => {
    e.preventDefault();
    dispatch(updateUser(formData))
      .unwrap()
      .then(() => {
        toast.success(`Updated successfully`);
        navigate("/");
        // dispatch(getAllPost()).unwrap().catch(toast.error);
        // dispatch(getMyPost()).unwrap().catch(toast.error);
      })
      .catch(toast.error);
    closeModal();
  };

  return (
    <>
      <Modal
        isOpen={modalIsOpen}
        onRequestClose={closeModal}
        style={customStyles}
        ariaHideApp={false}
        contentLabel="Add Note"
      >
        <h2>Update Details</h2>
        <button className="btn-close" onClick={closeModal}>
          X
        </button>
        <form>
          <div className="form-group">
            <label htmlFor="name">Enter your name</label>
            <input
              type="text"
              name="name"
              value={name}
              onChange={onChange}
              required
            />

            <label htmlFor="email">Enter your email</label>
            <input
              type="email"
              name="email"
              value={email}
              onChange={onChange}
              required
            />

            <label htmlFor="description">Description</label>
            <input
              type="text"
              name="description"
              value={description}
              onChange={onChange}
              required
            />

            <button className="btn btn-block btn-submit" onClick={handleUpdate}>
              Update Details
            </button>
          </div>
        </form>
      </Modal>
    </>
  );
}

export default InputForm;
