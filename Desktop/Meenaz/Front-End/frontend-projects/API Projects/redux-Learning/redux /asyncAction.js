const redux = require("redux");
const axios = require("axios");
const thunkMiddleware = require("redux-thunk").default;
const createStore = redux.createStore;
const applyMiddleware = redux.applyMiddleware;

const initialState = {
  loading: true,
  users: [],
  error: "",
};

const PENDING = "PENDING";
const FULFILLED = "FULFILLED";
const REJECTED = "REJECTED";

const fetchPending = () => {
  return {
    type: PENDING,
  };
};

const fetchfulfilled = (user) => {
  return {
    type: FULFILLED,
    payload: user,
  };
};

const fetchRejected = (error) => {
  return {
    type: REJECTED,
    payload: error,
  };
};

const reducer = (state = initialState, action) => {
  switch (action.type) {
    case PENDING:
      return {
        ...state,
        loading: true,
      };
    case FULFILLED:
      return {
        loading: false,
        users: action.payload,
        error: "",
      };
    case REJECTED:
      return {
        loading: false,
        users: [],
        error: action.payload,
      };
  }
};

const fetchUsers = () => {
  return function (dispatch) {
    dispatch(fetchPending());
    axios
      .get(`https://jsonplaceholder.typicode.com/users/`)
      .then((response) => {
        //response.data is the users
        const users = response.data.map((user) => user.id);
        dispatch(fetchfulfilled(users));
      })
      .catch((error) => {
        // error.message is the error message
        dispatch(fetchRejected(error.message));
      });
  };
};

const store = createStore(reducer, applyMiddleware(thunkMiddleware));

const unsubscribe = store.subscribe(() => console.log(store.getState()));

store.dispatch(fetchUsers());
