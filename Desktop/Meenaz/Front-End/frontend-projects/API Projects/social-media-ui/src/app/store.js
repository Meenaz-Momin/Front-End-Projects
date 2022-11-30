import { configureStore } from "@reduxjs/toolkit";
import authReducer from "../features/auth/authSlice.js";
import userReducer from "../features/users/userSlice.js";
import postReducer from "../features/post/PostSlice.js";

export const store = configureStore({
  reducer: {
    auth: authReducer,
    user: userReducer,
    post: postReducer,
  },
});
