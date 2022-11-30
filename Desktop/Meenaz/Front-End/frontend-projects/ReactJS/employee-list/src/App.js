import "./index.css";
import Header from "./components/Header";
import Input from "./components/Input";
import Display from "./components/Display";
import { EmpProvider } from "./components/Context";

function App() {
  return (
    <EmpProvider>
      <div className="container">
        <Header />
        <Input />
        <Display />
      </div>
    </EmpProvider>
  );
}

export default App;
