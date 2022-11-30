import React, { useState } from "react";
import { Stack, Rating } from "@mui/material";
import FavoriteIcon from "@mui/icons-material/Favorite";
import FavoriteBorderIcon from "@mui/icons-material/FavoriteBorder";

export const MuiRating = () => {
  const [value, setValue] = useState<number | null>(null);
  const readOnly = 3;
  console.log(value);
  const handleChange = (
    _event: React.ChangeEvent<{}>,
    newNumber: number | null
  ) => {
    setValue(newNumber);
  };
  return (
    <Stack spacing={2}>
      <Rating value={value} onChange={handleChange} />

      <Rating
        value={value}
        onChange={handleChange}
        precision={0.5}
        icon={<FavoriteIcon color="error" />}
        emptyIcon={<FavoriteBorderIcon />}
      />

      <Rating
        value={readOnly}
        precision={0.5}
        icon={<FavoriteIcon color="error" />}
        emptyIcon={<FavoriteBorderIcon />}
        readOnly
      />

      <Rating value={value} onChange={handleChange} highlightSelectedOnly />
    </Stack>
  );
};
