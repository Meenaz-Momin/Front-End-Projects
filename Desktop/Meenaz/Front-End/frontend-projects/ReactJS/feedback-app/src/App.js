import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import React from "react";
import FeedbackList from "./component/FeedbackList";
import Header from "./component/Header";
/*import FeedbackData from "./data/FeedbackData";*/
import FeedbackStats from "./component/FeedbackStats";
import FeedbackForm from "./component/FeedbackForm";
import About from "./pages/About";
import AboutLink from "./component/AboutLink";
import { FeedbackProvider } from "./component/context/FeedbackContext";

function App() {
  return (
    <FeedbackProvider>
      <Router>
        <Header />
        <div className="container">
          <Routes>
            <Route
              exact
              path="/"
              element={
                <>
                  <FeedbackForm />
                  <FeedbackStats />
                  <FeedbackList />
                </>
              }
            ></Route>

            <Route path="/about" element={<About />} />
          </Routes>
          <AboutLink />
        </div>
      </Router>
    </FeedbackProvider>
  );
}

export default App;
