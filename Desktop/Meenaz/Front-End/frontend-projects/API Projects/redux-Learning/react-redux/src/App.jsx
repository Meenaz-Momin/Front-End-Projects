import { useState } from "react";
import { CakeView } from "./features/cake/CakeView";
import { IcecreameView } from "./features/icecreame/IcecreameView";
import { UserView } from "./features/user/UserView";
import "./App.css";

function App() {
  return (
    <div>
      <CakeView />
      <IcecreameView />
      <UserView />
    </div>
  );
}

export default App;
