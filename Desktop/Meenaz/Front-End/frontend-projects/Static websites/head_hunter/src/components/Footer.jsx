import { LocationOn, MailOutline, Phone } from "@mui/icons-material";
import { Box, IconButton, Stack, TextField, Typography } from "@mui/material";
import React from "react";

function Footer() {
  return (
    <Box
      style={{
        backgroundColor: "#152429",
        height: "500px",
        position: "relative",
      }}
    >
      <Box
        style={{
          height: "100%",
          width: "35%",
          float: "right",
        }}
      >
        <Box
          style={{
            backgroundColor: "white",
            margin: "50px 70px",
            height: "80%",
            padding: "20px 40px",
            textAlign: "center",
          }}
        >
          <Typography variant="h6" style={{ paddingBottom: "15px" }}>
            Contact Us
          </Typography>
          <Stack spacing={2}>
            <TextField id="name" label="Name" variant="outlined" />
            <TextField id="email" label="Email" variant="outlined" />
            <TextField id="mobile" label="Mobile No." variant="outlined" />
            <TextField
              id="name"
              label="Describe a message"
              variant="outlined"
              rows={3}
              multiline
            />
          </Stack>
        </Box>
      </Box>

      <Box
        style={{
          float: "left",
          color: "white",
          position: "absolute",
          top: "50%",
          left: "50%",
          transform: "translate(-50%,-50%)",
          width: "65%",
        }}
      >
        <Stack direction="row" spacing={10}>
          <Stack direction="column" spacing={3}>
            <Typography variant="boday1">Our Service</Typography>
            <Typography variant="boday1">Our Stylist</Typography>
            <Typography variant="boday1">Gallery</Typography>
            <Typography variant="boday1">About Us</Typography>
          </Stack>
          <Stack direction="column">
            <Box>
              <IconButton>
                <LocationOn style={{ fill: "white", paddingRight: "20px" }} />
              </IconButton>
              <Typography variant="boday2" style={{ fontWeight: "10px" }}>
                205 S Baylen St, Pensacola, FL 32502, United States
              </Typography>
            </Box>

            <Box>
              <IconButton>
                <Phone style={{ fill: "white", paddingRight: "20px" }} />
              </IconButton>

              <Typography variant="boday2">850-433-3308 | </Typography>

              <Typography variant="boday2">850-433-3308</Typography>
            </Box>

            <Box>
              <IconButton>
                <MailOutline style={{ fill: "white", paddingRight: "20px" }} />
              </IconButton>

              <Typography variant="boday2">
                info@headhunterhairstyling.com{" "}
              </Typography>
            </Box>
          </Stack>
        </Stack>
      </Box>
    </Box>
  );
}

export default Footer;
