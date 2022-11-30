import { Box, Button, Stack, Typography } from "@mui/material";
import Imagelist from "./Imagelist";

function Feed() {
  return (
    <>
      <Box style={{ backgroundColor: "#152429", height: "463px" }}>
        <Box
          style={{
            float: "left",
            width: "50%",
            height: "100%",
            position: "relative",
          }}
        >
          <Box
            style={{
              position: "absolute",
              top: "45%",
              left: "50%",
              transform: "translate(-50%,-50%)",
              width: "80%",
              color: "#ffff",
              margin: "20px",
            }}
          >
            <Stack spacing={3}>
              <Typography variant="h4">Headhunter Hairstyling</Typography>
              <Typography variant="body1">
                SERVING PENSACOLA SINCE 1978
              </Typography>
              <Button
                style={{
                  color: "black",
                  backgroundColor: "white",
                  width: "120px",
                }}
              >
                Book Now
              </Button>
            </Stack>
          </Box>
        </Box>
        <img
          src="https://images.unsplash.com/photo-1466695108335-44674aa2058b?"
          alt="photo1"
          style={{
            width: "50%",
            height: "100%",
            float: "right",
            objectFit: "cover",
            objectPosition: "50px center ",
          }}
        />
      </Box>

      <Box
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          margin: "150px 400px",
        }}
      >
        <Stack spacing={4}>
          <Typography variant="h3" style={{ fontSize: "34px" }}>
            Welcome to Headhunter Hairstyling
          </Typography>
          <Typography variant="body2">
            We're excited that you found us and are interested in learning more
            about our stylists and services. Take a look around, call us, or
            stop by and we'll be happy to show you why we've been a staple in
            historic Pensacola since 1978. We're conveniently located in
            Downtown Pensacola and within walking distance to most businesses
            and restaurants in the area. Find our more About Us
          </Typography>
        </Stack>
      </Box>

      <Imagelist />
      
    </>
  );
}

export default Feed;
