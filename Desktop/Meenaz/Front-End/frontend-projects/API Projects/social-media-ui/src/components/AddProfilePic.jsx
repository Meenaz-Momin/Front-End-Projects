import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useDispatch } from "react-redux";
import Modal from "react-modal";
import { FaPlus } from "react-icons/fa";
import { profilePic } from "../features/users/userSlice";
import { getMyPost } from "../features/post/PostSlice";
import { toast } from "react-toastify";

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

function AddProfilePic() {
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const openModal = () => setModalIsOpen(true);
  const closeModal = () => setModalIsOpen(false);

  const [file, setFile] = useState();
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const handleChange = (e) => {
    const newFiles = Object?.values(e.target.files).map((item) => item);
    setFile(newFiles);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const formData = new FormData();

    formData.append("profile_pic", file[0]);

    dispatch(profilePic(formData))
      .unwrap()
      .then(() => {
        toast.success("Profile Pic Added successfully");
        navigate("/");
        dispatch(getMyPost());
      })
      .catch(toast.error);
    closeModal();
  };

  return (
    <div>
      <button className="btn" onClick={openModal}>
        <FaPlus />
      </button>
      <Modal
        isOpen={modalIsOpen}
        onRequestClose={closeModal}
        style={customStyles}
        ariaHideApp={false}
        contentLabel="Add Note"
      >
        <h2>upload Profile</h2>
        <button className="btn-close" onClick={closeModal}>
          X
        </button>
        <form onSubmit={handleSubmit}>
          <div className="form-group"></div>
          <div className="form-group">
            <label>upload profile photo</label>
            <input type="file" accept="image/*" onChange={handleChange} />
            <button className="btn" type="submit">
              Submit
            </button>
          </div>
        </form>
      </Modal>
    </div>
  );
}

export default AddProfilePic;
