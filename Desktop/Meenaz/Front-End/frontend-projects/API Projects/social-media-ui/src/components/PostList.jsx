import { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { toast } from "react-toastify";
// import { useState } from "react";
import { Link } from "react-router-dom";
import { getAllPost } from "../features/post/PostSlice";

function PostList() {
  const dispatch = useDispatch();
  const postList = useSelector((state) => state.post).posts;
  const { user } = useSelector((state) => state.auth);

  useEffect(() => {
    dispatch(getAllPost()).unwrap().catch(toast.error);
  }, [dispatch]);

  if (!user) {
    return <h1>Please Login to continue with us</h1>;
  } else if (!postList) {
    return <h1>Loading.......</h1>;
  }

  return (
    <div className="container">
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
                    <span className="material-symbols-outlined icon">send</span>
                  </div>
                  <br />
                  <br />
                  <br />
                  <div className="description">
                    <p>
                      {post.caption}
                      {"  to see more  "}
                      <Link to={`/single-profile/${post.id}`}>
                        {post.user.name}
                      </Link>
                    </p>
                  </div>
                </div>
              </div>
            );
          })
        : null}
    </div>
  );
}

export default PostList;
