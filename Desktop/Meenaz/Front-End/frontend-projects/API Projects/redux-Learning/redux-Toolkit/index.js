const store = require("./app/store");
const cakeActions = require("./features/cake/cakeSlice").cakeActions;
const iceCreameActions =
  require("./features/icecreame/icecreameSlice").iceCreameActions;
const fetchUsers = require("./features/user/userSlice").fetchUsers;

const unsubscribe = store.subscribe(() => {});

store.dispatch(fetchUsers());

// store.dispatch(iceCreameActions.ordered());
// store.dispatch(cakeActions.ordered());
// store.dispatch(cakeActions.ordered());
// store.dispatch(cakeActions.restocked(2));
// store.dispatch(iceCreameActions.restocked(2));

//unsubscribe();
