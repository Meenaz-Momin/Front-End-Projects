import { AppBar, Box, Button, Toolbar, Typography } from "@mui/material";

const navItems = ["Home", "Service", "Stylist", "Gallery", "About us"];
function Navbar() {
  return (
    <Box sx={{ flexGrow: 0 }}>
      <AppBar
        position="static"
        style={{ backgroundColor: "#152429", height: "90px" }}
      >
        <Toolbar>
          <Typography sx={{ flexGrow: 1 }}></Typography>
        </Toolbar>
      </AppBar>

      <AppBar position="static" style={{ backgroundColor: "#F1F2F7" }}>
        <Toolbar>
          <Typography sx={{ flexGrow: 1 }}></Typography>
          {navItems.map((item, index) => (
            <Box style={{ paddingLeft: "100px" }} key={index}>
              <Button style={{ color: "black"}}>{item}</Button>
            </Box>
          ))}
        </Toolbar>
      </AppBar>
    </Box>
  );
}

export default Navbar;
