import { useState } from "react";
import { toast } from "react-toastify";
import Modal from "react-modal";
import { useNavigate } from "react-router-dom";
import { useDispatch } from "react-redux";
import { getMyPost, updatePost } from "../features/post/PostSlice";

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

function EditPost({ id, caption2, postImage }) {
  const navigate = useNavigate();
  const dispatch = useDispatch();

  const [modalIsOpen, setModalIsOpen] = useState(true);
  const closeModal = () => setModalIsOpen(false);

  const [file, setFile] = useState(postImage);
  const [caption, setCaption] = useState(caption2);

  const handleFile = (e) => {
    const newFiles = Object?.values(e.target.files).map((item) => item);
    setFile(newFiles);
  };

  const handleCaption = (e) => {
    setCaption(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // const formData = new FormData();
    // formData.append("post_files", file[0]);
    // formData.append("caption", caption);
    // formData.append("id", id);
    // console.log(formData);
    dispatch(updatePost({ files: file[0], caption, id }))
      .unwrap()
      .then(() => {
        dispatch(getMyPost());
        navigate("/");
      })
      .catch(toast.error);
    closeModal();
  };

  return (
    <>
      <Modal
        isOpen={modalIsOpen}
        // onRequestClose={closeModal}
        style={customStyles}
        ariaHideApp={false}
        // contentLabel="Add Note"
      >
        <h2>Update your changes</h2>
        <button className="btn-close" onClick={closeModal}>
          X
        </button>
        <form>
          <div className="form-group"></div>
          <div className="form-group">
            <label>Write caption</label>
            <input type="text" value={caption} onChange={handleCaption} />
            <label>upload an image</label>
            <input type="file" accept="image/*" onChange={handleFile} />
            <button className="btn" type="submit" onClick={handleSubmit}>
              Submit
            </button>
          </div>
        </form>
      </Modal>
    </>
  );
}

export default EditPost;
