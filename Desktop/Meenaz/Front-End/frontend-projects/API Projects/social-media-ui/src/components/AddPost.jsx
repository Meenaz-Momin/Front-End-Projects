import { useState } from "react";
import { toast } from "react-toastify";
import { FaPlus } from "react-icons/fa";
import Modal from "react-modal";
import { useNavigate } from "react-router-dom";
import { useDispatch } from "react-redux";
import { createPost, getMyPost } from "../features/post/PostSlice";

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

function Post() {
  const navigate = useNavigate();
  const dispatch = useDispatch();

  const [modalIsOpen, setModalIsOpen] = useState(false);
  const openModal = () => setModalIsOpen(true);
  const closeModal = () => setModalIsOpen(false);

  const [file, setFile] = useState();
  const [caption, setCaption] = useState("");

  const handleFile = (e) => {
    const newFiles = Object?.values(e.target.files).map((item) => item);
    setFile(newFiles);
  };

  const handleCaption = (e) => {
    setCaption(e.target.value);
  };

  const submitPost = (e) => {
    e.preventDefault();
    const formData = new FormData();

    for (let i = 0; i < file.length; i++) {
      formData.append("post_files", file[i]);
    }
    formData.append("caption", caption);
    dispatch(createPost(formData))
      .unwrap()
      .then(
        closeModal(),
        toast.success("Post Added Successfully"),
        dispatch(getMyPost()),
        navigate("/")
      )
      .catch(toast.error);
  };

  // files.map((item) => {
  //   formData.append("post_files", item);
  // });
  // file: files[]
  return (
    <div>
      <button className="btn" onClick={openModal}>
        <FaPlus />
        Add Post
      </button>

      <Modal
        isOpen={modalIsOpen}
        onRequestClose={closeModal}
        style={customStyles}
        ariaHideApp={false}
        contentLabel="Add Note"
      >
        <h2>Add Pictures</h2>
        <button className="btn-close" onClick={closeModal}>
          X
        </button>
        <form>
          <div className="form-group">
            <label>Write caption</label>
            <input
              type="text"
              value={caption}
              onChange={(e) => handleCaption(e)}
            />
            <label>upload an image</label>
            <input
              type="file"
              accept="image/*"
              onChange={(e) => handleFile(e)}
            />
            <button className="btn" type="submit" onClick={submitPost}>
              Submit
            </button>
          </div>
        </form>
      </Modal>
    </div>
  );
}

export default Post;
