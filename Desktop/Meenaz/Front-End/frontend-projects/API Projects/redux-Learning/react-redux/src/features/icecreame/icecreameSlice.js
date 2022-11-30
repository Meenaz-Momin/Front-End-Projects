import { createSlice } from "@reduxjs/toolkit";
import { ordered as cakeOrdered } from "../cake/cakeSlice";

const initialState = {
  numOfIceCreame: 20,
};

const iceCreameSlice = createSlice({
  name: "icecreame",
  initialState,
  reducers: {
    ordered: (state) => {
      state.numOfIceCreame--;
    },
    restocked: (state, action) => {
      state.numOfIceCreame += action.payload;
    },
  },
  // extraReducers: {
  //   ["cake/ordered"]: (state) => {
  //     state.numOfIceCreame--;
  //   },
  // },
  extraReducers: (builders) => {
    builders.addCase(cakeOrdered, (state) => {
      state.numOfIceCreame--;
    });
  },
});

export default iceCreameSlice.reducer;
export const { ordered, restocked } = iceCreameSlice.actions;
