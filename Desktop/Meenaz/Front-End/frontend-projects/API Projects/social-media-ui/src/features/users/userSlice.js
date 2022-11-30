import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import { extractErrorMessage } from "../../utils";
import userService from "./userSevice";

const user = JSON.parse(localStorage.getItem("user"));
const initialState = {
  user: user ? user : null,
  isLoading: false,
};

// get Me
export const getMe = createAsyncThunk("user/getMe", async (_, thunkAPI) => {
  try {
    const token = thunkAPI.getState().auth.user.token;
    return await userService.getMe(token);
  } catch (error) {
    thunkAPI.rejectWithValue(extractErrorMessage(error));
  }
});

// upload profile pic
export const profilePic = createAsyncThunk(
  "user/profilePic",
  async (pic, thunkAPI) => {
    try {
      const token = thunkAPI.getState().auth.user.token;
      return await userService.profilePic(pic, token);
    } catch (error) {
      thunkAPI.rejectWithValue(extractErrorMessage(error));
    }
  }
);

// update a user
export const updateUser = createAsyncThunk(
  "user/updateUser",
  async (data, thunkAPI) => {
    try {
      const token = thunkAPI.getState().auth.user.token;
      console.log("i am in slice file");
      return await userService.updateUser(data, token);
    } catch (error) {
      thunkAPI.rejectWithValue(extractErrorMessage(error));
    }
  }
);

// delete a user
export const deleteUser = createAsyncThunk(
  "user/deleteUser",
  async (_, thunkAPI) => {
    try {
      const token = thunkAPI.getState().auth.user.token;
      return await userService.deleteUser(token);
    } catch (error) {
      thunkAPI.rejectWithValue(extractErrorMessage(error));
    }
  }
);

const userSlice = createSlice({
  name: "user",
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(getMe.pending, (state) => {
        state.isLoading = true;
      })
      .addCase(getMe.fulfilled, (state, action) => {
        state.user = action.payload;
        state.isLoading = false;
      })
      .addCase(getMe.rejected, (state) => {
        state.isLoading = false;
      })
      .addCase(profilePic.pending, (state) => {
        state.isLoading = true;
      })
      .addCase(profilePic.fulfilled, (state, action) => {
        state.user = action.payload;
        state.isLoading = false;
      })
      .addCase(profilePic.rejected, (state) => {
        state.isLoading = false;
      })
      .addCase(updateUser.pending, (state) => {
        state.isLoading = true;
      })
      .addCase(updateUser.fulfilled, (state, action) => {
        state.user = action.payload;
        state.isLoading = false;
      })
      .addCase(updateUser.rejected, (state) => {
        state.isLoading = false;
      })
      .addCase(deleteUser.pending, (state) => {
        state.isLoading = true;
      })
      .addCase(deleteUser.fulfilled, (state, action) => {
        state.user = action.payload;
        state.isLoading = false;
      })
      .addCase(deleteUser.rejected, (state) => {
        state.isLoading = false;
      });
  },
});

export default userSlice.reducer;
