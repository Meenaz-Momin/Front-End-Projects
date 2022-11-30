const redux = require("redux");
const produce = require("immer").produce;

const initialState = {
  name: "Meenaz",
  address: {
    street: "meethanagar",
    city: "pune",
    state: "Maharashtra",
  },
};

const streetUpdate = (street) => {
  return {
    type: "STREET_UPDATE",
    payload: street,
  };
};

const reducer = (state = initialState, action) => {
  switch (action.type) {
    case "STREET_UPDATE":
      //   return {
      //     ...state,
      //     address: {
      //       ...state.address,
      //       street: action.payload,
      //     },
      //   };
      return produce(state, (draft) => {
        draft.address.street = action.payload;
      });
    default:
      return state;
  }
};

const store = redux.createStore(reducer);
console.log("initial state: ", store.getState());

const unsubscribe = store.subscribe(() =>
  console.log("updated state: ", store.getState())
);

store.dispatch(streetUpdate("bhgyoday nagar"));

unsubscribe();
