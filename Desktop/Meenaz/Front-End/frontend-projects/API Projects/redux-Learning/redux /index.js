const redux = require("redux");
const createStore = redux.createStore;
const bindActionCreators = redux.bindActionCreators;
const combineReducers = redux.combineReducers;
const applyMiddleware = redux.applyMiddleware;

const reduxLogger = require("redux-logger");
const logger = reduxLogger.createLogger();

const CAKE_ORDERED = "CAKE_ORDERED";
const CAKE_RESTOCKED = "CAKE_RESTOCKED";
const ICECREAME_ORDERED = "ICECREAME_ORDERED";
const ICECREAME_RESTOCKED = "ICECREAME_RESTOCKED";

function orderCake(qty = 1) {
  return {
    type: CAKE_ORDERED,
    payload: qty,
  };
}

function reStcokCake(qty = 1) {
  return {
    type: CAKE_RESTOCKED,
    payload: qty,
  };
}

function orderIceCreame(qty = 1) {
  return {
    type: ICECREAME_ORDERED,
    payload: qty,
  };
}

function reStcokIceCreame(qty = 1) {
  return {
    type: ICECREAME_RESTOCKED,
    payload: qty,
  };
}

// const initialState = {
//   numCakes: 10,
//   numIceCreame: 20,
// };
const initialCakeState = { numCakes: 10 };
const initialIceCreameState = { numIceCreame: 15 };

// (previousState, action) => newState

const cakeReducer = (state = initialCakeState, action) => {
  switch (action.type) {
    case CAKE_ORDERED:
      return {
        ...state,
        numCakes: state.numCakes - 1,
      };
    case CAKE_RESTOCKED:
      return {
        ...state,
        numCakes: state.numCakes + action.payload,
      };
    default:
      return state;
  }
};

const iceCreameReducer = (state = initialIceCreameState, action) => {
  switch (action.type) {
    case ICECREAME_ORDERED:
      return {
        ...state,
        numIceCreame: state.numIceCreame - 1,
      };
    case ICECREAME_RESTOCKED:
      return {
        ...state,
        numIceCreame: state.numIceCreame + action.payload,
      };
    default:
      return state;
  }
};

const rootReducer = combineReducers({
  cake: cakeReducer,
  iceCreame: iceCreameReducer,
});
const store = createStore(rootReducer, applyMiddleware(logger));
console.log("Initial State:", store.getState());

const unsubscribe = store.subscribe(() => {} );

// store.dispatch(orderCake());
// store.dispatch(orderCake());
// store.dispatch(orderCake());
// store.dispatch(reStcokCake(5));

const actions = bindActionCreators(
  { orderCake, reStcokCake, orderIceCreame, reStcokIceCreame },
  store.dispatch
);
actions.orderCake();
actions.reStcokCake(6);
actions.orderIceCreame();
actions.orderIceCreame();
actions.reStcokIceCreame(4);

unsubscribe();
