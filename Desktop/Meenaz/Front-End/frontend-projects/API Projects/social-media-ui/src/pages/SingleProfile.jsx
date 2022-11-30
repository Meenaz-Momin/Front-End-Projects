import { useEffect } from "react";
import { useParams } from "react-router-dom";
import { toast } from "react-toastify";
import { useSelector, useDispatch } from "react-redux";
import Back from "../components/Back";
import { getOnePost, getAllPost } from "../features/post/PostSlice";

function SingleProfile() {
  const dispatch = useDispatch();
  const postList = useSelector((state) => state.post).posts;
  const postId = useParams().id;

  const post = postList.data.filter((item) => {
    return item.id + "" === postId;
  });
  useEffect(() => {
    dispatch(getAllPost()).unwrap().catch(toast.error);
    dispatch(getOnePost(postId)).unwrap().catch(toast.error);
  }, [dispatch, postId]);

  return (
    <div className="container">
      <div className="profile">
        <div className="profile-page-image-container">
          <img
            src={`http://192.168.1.37:8888/${post[0].user.prfile_pic}`}
            alt="nature"
            className="profile-page-image"
          />
        </div>
        <div className="profile-description">
          <h1 className="header">{post[0].user.name}</h1>
          <Back url="/" />
        </div>
      </div>
      <h2>Posts</h2>
      <div className="single-profile-post">
        <div className="">
          <div className="post-heading">
            <img
              className="profile-image"
              src={`http://192.168.1.37:8888/${post[0].user.prfile_pic}`}
              alt="profile"
            />
            <div className="profile-name">
              <h3>{post[0].user.name}</h3>
            </div>
          </div>
          <div className="post-image">
            <img
              className="post-post-image"
              src={`http://192.168.1.37:8888/${post[0].post_files}`}
              alt="post"
            />
          </div>
          <div className="post-footer">
            <div className="icons">
              <span className="material-symbols-outlined icon">favorite</span>
              <span className="material-symbols-outlined icon">
                contact_support
              </span>
              <span className="material-symbols-outlined icon">send</span>
            </div>
            <br />
            <br />
            <br />
            <div className="description">
              <p>{post[0].caption}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default SingleProfile;
