import { configureStore } from "@reduxjs/toolkit";
//import reduxLogger from "redux-logger";
import cakeReducer from "../features/cake/cakeSlice";
import iceCreameReducer from "../features/icecreame/icecreameSlice";
import userReducer from "../features/user/userSlice";

//const logger = reduxLogger.createLogger();

const store = configureStore({
  reducer: {
    cake: cakeReducer,
    icecreame: iceCreameReducer,
    user: userReducer,
  },
  //middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(logger),
});

export default store;
