import { useEffect, useState } from "react";
import { toast } from "react-toastify";
import { useNavigate } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import { FaEdit, FaTimes } from "react-icons/fa";
import AddPost from "../components/AddPost";
import AddProfilePic from "../components/AddProfilePic";
import Back from "../components/Back";
import InputForm from "../components/UpdateUser";
import EditPost from "../components/EditPost";
import { deleteUser } from "../features/users/userSlice";
import { getMyPost, deletePost, getAllPost } from "../features/post/PostSlice";

function Profile() {
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const [open, setOpen] = useState(false);
  const [isUpdate, setIsUpdate] = useState(false);
  const [isEdit, setIsEdit] = useState({
    edit: false,
    id: "",
    caption: "",
    file: [],
  });

  const { user } = useSelector((state) => state.user);
  const postList = useSelector((state) => state.post).post;

  useEffect(() => {
    dispatch(getAllPost()).unwrap().catch(toast.error);
    dispatch(getMyPost()).unwrap().catch(toast.error);
  }, [dispatch]);

  const postDelete = (id) => {
    if (window.confirm("are you sure you want to delete post?")) {
      dispatch(deletePost(id))
        .unwrap()
        .then(
          toast.success("post deleted succcesfully"),
          dispatch(getAllPost()),
          dispatch(getMyPost()),
          navigate("/")
        )
        .catch(toast.error);
    }
  };

  const handleDelete = () => {
    if (window.confirm("Are you sure? You want to delete you account")) {
      dispatch(deleteUser())
        .unwrap()
        .then(() => {
          toast.success("UserDeleted successfully");
          dispatch(getAllPost());
          navigate("/");
        })
        .catch(toast.error);
      navigate("/");
    }
  };

  const handleEdit = (postId, postCaption, postFile) => {
    setIsEdit({
      edit: true,
      id: postId,
      caption: postCaption,
      file: postFile,
    });
  };

  if (!postList) {
    return <h1>No Post Yet</h1>;
  }
  // (id)
  //   let newArray =Postlist?.map(item => id===item?.id? {...item,isEdit: true}: item )
  //   setPostLit(newArray)
  return (
    <div className="container">
      {!user ? (
        <>
          <h1>Something Went wrong..Please try again</h1>
        </>
      ) : (
        <>
          <div className="profile">
            <div className="profile-page-image-container">
              {!user.data.prfile_pic ? (
                <>
                  {" "}
                  <div className="profile-page-image">
                    <AddProfilePic />
                  </div>
                </>
              ) : (
                <>
                  <img
                    className="profile-page-image"
                    src={`http://192.168.1.37:8888/${user.data.prfile_pic}`}
                    alt="prfile_pic"
                  />
                </>
              )}
            </div>
            <div className="profile-description">
              <div className="header">
                <h1>{user.data.name}</h1>
                <div className="dropdown">
                  <button onClick={() => setOpen(!open)}>
                    <span className="material-symbols-outlined option">
                      more_horiz
                    </span>
                  </button>
                  {open ? (
                    <ul className="menu">
                      <li className="menu-item">
                        <button onClick={() => setIsUpdate(!isUpdate)}>
                          Update User
                        </button>
                      </li>
                      <li className="menu-item">
                        <button onClick={handleDelete}>Delete User</button>
                      </li>
                    </ul>
                  ) : null}
                  {isUpdate ? (
                    <InputForm
                      name2={user.data.name}
                      email2={user.data.email}
                      description={user.data.description}
                    />
                  ) : null}
                </div>
              </div>
              <p>{user.data.email}</p>
              <p>{user.data.description}</p>
              <AddPost />
              <Back url="/" />
            </div>
          </div>
        </>
      )}

      {!user && !postList ? (
        <>
          <h1>Something went wrong</h1>
        </>
      ) : (
        <>
          <h2> Posts</h2>
          {Array.isArray(postList.data)
            ? postList.data.map((post) => {
                return (
                  <div className="post" key={post.id}>
                    <div className="post-heading">
                      <img
                        className="profile-image"
                        src={`http://192.168.1.37:8888/${post.user.prfile_pic}`}
                        alt="profile"
                      />
                      <div className="profile-name">
                        <h3>{post.user.name}</h3>
                      </div>

                      <div className="delete">
                        <button onClick={() => postDelete(post.id)}>
                          <FaTimes size={15} />
                        </button>
                      </div>
                      <div className="edit">
                        <button
                          onClick={() =>
                            handleEdit(
                              post.id,
                              post.caption,
                              post.post_files[0]
                            )
                          }
                        >
                          <FaEdit size={15} />
                          {isEdit.edit ? (
                            <EditPost
                              caption2={isEdit.caption}
                              postImage={isEdit.file}
                              id={isEdit.id}
                            />
                          ) : null}
                        </button>
                      </div>
                    </div>

                    <div className="post-image">
                      <img
                        className="post-post-image"
                        src={`http://192.168.1.37:8888/${post.post_files[0]}`}
                        alt="post"
                      />
                    </div>
                    <div className="post-footer">
                      <div className="icons">
                        <span className="material-symbols-outlined icon">
                          favorite
                        </span>
                        <span className="material-symbols-outlined icon">
                          contact_support
                        </span>
                        <span className="material-symbols-outlined icon">
                          send
                        </span>
                      </div>
                      <br />
                      <br />
                      <br />
                      <div className="description">
                        <p>{post.caption}</p>
                      </div>
                    </div>
                  </div>
                );
              })
            : null}
        </>
      )}
    </div>
  );
}

export default Profile;
