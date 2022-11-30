import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import { Rightbar } from "../components/Rightbar";
import { Feed } from "../components/Feed";
import { useState } from "react";
import { Add } from "../components/Add";
import { createTheme, ThemeProvider, Box, Stack } from "@mui/material";
import { useSelector } from "react-redux";
import Login from "./Login";

const Home = () => {
  const { auth } = useSelector((state) => state.auth);

  const [mode, setMode] = useState("light");
  const darkTheme = createTheme({
    palette: {
      mode: mode,
    },
  });

  {
    if (auth == null) {
      return <Login />;
    } else {
      return (
        <ThemeProvider theme={darkTheme}>
          <Box bgcolor={"background.default"} color={"text.primary"}>
            <Navbar />
            <Stack direction="row" spacing={2} justifyContent="space-between">
              <Sidebar setMode={setMode} mode={mode} />
              <Feed />
              <Rightbar />
            </Stack>
            <Add />
          </Box>
        </ThemeProvider>
      );
    }
  }
};

export default Home;
