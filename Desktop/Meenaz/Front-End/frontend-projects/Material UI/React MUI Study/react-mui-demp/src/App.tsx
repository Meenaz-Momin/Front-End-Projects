import "./App.css";
import { LocalizationProvider } from "@mui/x-date-pickers";
import { AdapterDateFns } from "@mui/x-date-pickers/AdapterDateFns";
import { MuiMasonry } from "./components/MuiMasonry";
// import { MuiPicker } from "./components/MuiPicker";
// import { MuiLayout } from "./components/MuiLayout";
// import { MuiAutocomplete } from "./components/MuiAutocomplete";
// import { MuiRating } from "./components/MuiRating";
// import { MuiSwitch } from "./components/MuiSwitch";
// import { MuiCheckBox } from "./components/MuiCheckBox";
// import { MuiRadioButton } from "./components/MuiRadioButton";
// import { MuiTypography } from "./components/MuiTypography";
// import { MuiButtons } from "./components/MuiButtons";
// import { MuiTextField } from "./components/MuiTextField";
// import { MuiSelect } from "./components/MuiSelect";

function App() {
  return (
    <LocalizationProvider dateAdapter={AdapterDateFns}>
      <div className="App">
        {/* <MuiTypography /> */}
        {/* <MuiButtons /> */}
        {/* <MuiTextField /> */}
        {/* <MuiSelect /> */}
        {/* <MuiRadioButton /> */}
        {/* <MuiCheckBox /> */}
        {/* <MuiSwitch /> */}
        {/* <MuiRating /> */}
        {/* <MuiAutocomplete /> */}
        {/* <MuiLayout /> */}
        {/* <MuiPicker /> */}
        <MuiMasonry />
      </div>
    </LocalizationProvider>
  );
}

export default App;
