import React from "react";

export default function App() {
  let date = new Date().toLocaleDateString();
  let time = new Date().toLocaleTimeString();
  return (
    <>
      <h1>Hiiii, My name is Meenaz Momin</h1>
      <p>Today's Date : {date}</p>
      <p>Current Time : {time}</p>
    </>
  );
}
