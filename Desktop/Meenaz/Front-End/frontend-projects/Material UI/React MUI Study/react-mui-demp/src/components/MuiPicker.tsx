import { Stack, TextField } from "@mui/material";
import { DatePicker, TimePicker } from "@mui/x-date-pickers";
import { useState } from "react";

export const MuiPicker = () => {
  const [selectDate, setSelectDate] = useState<Date | null>(null);
  const [selectTime, setSelectTime] = useState<Date | null>(null);
  console.log(selectTime);

  return (
    <Stack spacing={2} sx={{ width: "250px" }}>
      <TimePicker
        label="Time picker"
        renderInput={(params) => <TextField {...params} />}
        value={selectTime}
        onChange={(newValue) => {
          setSelectTime(newValue);
        }}
      />

      <DatePicker
        label="Date Picker"
        renderInput={(params) => <TextField {...params} />}
        value={selectDate}
        onChange={(newValue) => setSelectDate(newValue)}
      />
    </Stack>
  );
};
