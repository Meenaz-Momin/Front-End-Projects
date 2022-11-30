import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import { extractError } from "../../utils";
import userService from "./userService";

const auth = JSON.parse(localStorage.getItem("auth"));
const initialState = {
  user: auth ? auth : null,
  isLoading: false,
};

// update a user
export const updateUser = createAsyncThunk(
  "user/update",
  async (data, thunkAPI) => {
    try {
      const token = thunkAPI.getState().auth.auth.token;
      return await userService.updateUser(data,token);
    } catch (error) {
      thunkAPI.rejectWithValue(extractError(error));
    }
  }
);

// delete a user
export const deleteUser = createAsyncThunk(
  "user/delete",
  async (_, thunkAPI) => {
    try {
      const token = thunkAPI.getState().auth.auth.token;
      return await userService.deleteUser(token);
    } catch (error) {
      thunkAPI.rejectWithValue(extractError(error));
    }
  }
);

const userSlice = createSlice({
  name: "user",
  initialState,
  reducer: {},
  extraReducers: (builders) => {
    builders
      .addCase(deleteUser.pending, (state) => {
        state.isLoading = true;
      })
      .addCase(deleteUser.fulfilled, (state, action) => {
        state.isLoading = false;
        state.user = action.payload;
      })
      .addCase(deleteUser.rejected, (state) => {
        state.isLoading = false;
      })
      .addCase(updateUser.pending, (state) => {
        state.isLoading = true;
      })
      .addCase(updateUser.fulfilled, (state, action) => {
        state.isLoading = false;
        state.user = action.payload;
      })
      .addCase(updateUser.rejected, (state) => {
        state.isLoading = false;
      });
  },
});

export default userSlice.reducer;
