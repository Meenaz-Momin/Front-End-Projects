import { Stack, Autocomplete, TextField } from "@mui/material";
import { useState } from "react";

const skills = ["HTML", "CSS", "Javascript", "Typescript", "React"];

export const MuiAutocomplete = () => {
  const [value, setValue] = useState<String | null>(null);
  console.log(value);
  return (
    <Stack spacing={2}>
      <Autocomplete
        options={skills}
        renderInput={(params) => <TextField {...params} label="skills" />}
        value={value}
        onChange={(event: any, newString: String | null) => setValue(newString)}
        freeSolo
      />
    </Stack>
  );
};
