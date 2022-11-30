import React from "react";
import { useSelector, useDispatch } from "react-redux";
import { ordered, restocked } from "./icecreameSlice";

export const IcecreameView = () => {
  const numOfIcecreames = useSelector(
    (state) => state.icecreame.numOfIceCreame
  );
  const dispatch = useDispatch();
  return (
    <div>
      <h2>Number of Ice-Creames - {numOfIcecreames}</h2>
      <button onClick={() => dispatch(ordered())}>Order Ice-creame</button>
      <button onClick={() => dispatch(restocked(5))}>
        Restock Ice-creames
      </button>
    </div>
  );
};
