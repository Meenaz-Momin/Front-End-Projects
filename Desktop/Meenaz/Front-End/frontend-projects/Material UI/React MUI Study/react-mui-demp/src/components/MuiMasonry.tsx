import { Box, Paper } from "@mui/material";
import { Masonry } from "@mui/lab";

const heights = [130, 45, 87, 12, 55, 80, 98, 145, 23, 30, 65, 37, 25, 10, 30];
export const MuiMasonry = () => {
  return (
    <Box sx={{ width: 500, minHeight: 400 }}>
      <Masonry columns={4} spacing={1}>
        {heights.map((height, index) => (
          <Paper
            key={index}
            sx={{
              display: "flex",
              height,
              justifyContent: "center",
              alignItems: "center",
              border: "1px solid ",
            }}
          >
            {height}
          </Paper>
        ))}
      </Masonry>
    </Box>
  );
};
