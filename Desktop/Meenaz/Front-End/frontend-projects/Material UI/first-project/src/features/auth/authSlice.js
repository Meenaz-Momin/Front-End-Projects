import { createSlice, createAsyncThunk, createAction } from "@reduxjs/toolkit";
import { extractError } from "../../utils";
import authService from "./authService";

const auth = JSON.parse(localStorage.getItem("auth"));
const initialState = {
  auth: auth ? auth : null,
  isLoading: false,
};

// register user
export const register = createAsyncThunk(
  "auth/register",
  async (auth, thunkAPI) => {
    try {
      return await authService.register(auth);
    } catch (error) {
      thunkAPI.rejectWithValue(extractError(error));
    }
  }
);

//login user
export const login = createAsyncThunk("auth/login", async (auth, thunkAPI) => {
  try {
    return await authService.login(auth);
  } catch (error) {
    thunkAPI.rejectWithValue(extractError(error));
  }
});

//user logout
export const logout = createAction("auth/logout", () => {
  authService.logout();
  return {};
});

const authSlice = createSlice({
  name: "auth",
  initialState,
  reducer: {
    logout: (state) => {
      state.auth = null;
    },
  },
  extraReducers: (builders) => {
    builders
      .addCase(register.pending, (state) => {
        state.isLoading = true;
      })
      .addCase(register.fulfilled, (state, action) => {
        state.auth = action.payload;
        state.isLoading = false;
      })
      .addCase(register.rejected, (state) => {
        state.auth = false;
      })
      .addCase(login.pending, (state) => {
        state.isLoading = true;
      })
      .addCase(login.fulfilled, (state, action) => {
        state.auth = action.payload;
        state.isLoading = false;
      })
      .addCase(login.rejected, (state) => {
        state.auth = false;
      });
  },
});

export default authSlice.reducer;
