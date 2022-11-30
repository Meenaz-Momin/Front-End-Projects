import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { extractError } from "../../utils";
import postService from "./postService";

const initialState = {
  allPost: [],
  myPost: [],
  isLoading: false,
};

//create post
export const createPost = createAsyncThunk(
  "post/createPost",
  async (post, thunkAPI) => {
    try {
      const token = thunkAPI.getState().auth.auth.token;
      return await postService.createPost(post,token);
    } catch (error) {
      thunkAPI.rejectWithValue(extractError(error));
    }
  }
);

//get All post
export const getAllPost = createAsyncThunk(
  "post/getAllPost",
  async (_, thunkAPI) => {
    try {
      const token = thunkAPI.getState().auth.auth.token;
      return await postService.getAllPost(token);
    } catch (error) {
      thunkAPI.rejectWithValue(extractError(error));
    }
  }
);

//get My Post
export const getMyPost = createAsyncThunk(
  "post/getMyPost",
  async (_, thunkAPI) => {
    try {
      const token = thunkAPI.getState().auth.auth.token;
      return await postService.getMyPost(token);
    } catch (error) {
      thunkAPI.rejectWithValue(extractError(error));
    }
  }
);

//delete My Post
export const deletePost = createAsyncThunk(
  "post/deletePost",
  async (postId, thunkAPI) => {
    try {
      const token = thunkAPI.getState().auth.auth.token;
      return await postService.deletePost(postId,token);
    } catch (error) {
      thunkAPI.rejectWithValue(extractError(error));
    }
  }
);


const postSlice = createSlice({
  name: "post",
  initialState,
  reducer: {},
  extraReducers: (builders) => {
    builders
      .addCase(getAllPost.pending, (state) => {
        state.isLoading = true;
      })
      .addCase(getAllPost.fulfilled, (state, action) => {
        state.allPost = action.payload;
        state.isLoading = false;
      })
      .addCase(getAllPost.rejected, (state) => {
        state.isLoading = false;
      })
      .addCase(getMyPost.pending, (state) => {
        state.isLoading = true;
      })
      .addCase(getMyPost.fulfilled, (state, action) => {
        state.myPost = action.payload;
        state.isLoading = false;
      })
      .addCase(getMyPost.rejected, (state) => {
        state.isLoading = false;
      })
      .addCase(deletePost.pending, (state) => {
        state.isLoading = true;
      })
      .addCase(deletePost.fulfilled, (state) => {
        state.isLoading = false;
      })
      .addCase(deletePost.rejected, (state) => {
        state.isLoading = false;
      });
  },
});

export default postSlice.reducer;
