import { Box, Switch, FormControlLabel } from "@mui/material";
import React, { useState } from "react";

export const MuiSwitch = () => {
  const [value, setvalue] = useState(false);
  console.log(value);
  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setvalue(event.target.checked);
  };
  return (
    <Box>
      <FormControlLabel
        label="dark Mode"
        control={<Switch checked={value} onChange={handleChange} />}
      />
    </Box>
  );
};
