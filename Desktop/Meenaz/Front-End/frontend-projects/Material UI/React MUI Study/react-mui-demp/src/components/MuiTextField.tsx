import { InputAdornment, Stack, TextField } from "@mui/material";
import VisibilityIcon from "@mui/icons-material/Visibility";
import VisibilityOffIcon from "@mui/icons-material/VisibilityOff";

export const MuiTextField = () => {
  return (
    <Stack spacing={2}>
      <Stack spacing={2} direction="row">
        <TextField label="Name" variant="outlined" />
        <TextField label="Name" variant="filled" />
        <TextField label="Name" variant="standard" />
      </Stack>

      <Stack spacing={2} direction="row">
        <TextField label="small secondary" size="small" color="secondary" />
        {/* <TextField label="large success" size="large" color="success" /> */}
        <TextField label="medium warning" size="medium" color="warning" />
      </Stack>

      <Stack spacing={2} direction="row">
        <TextField label="form" required />
        <TextField
          label="password"
          type="password"
          helperText="do not share your password"
          disabled
        />
        <TextField label="read only" InputProps={{ readOnly: true }} />
      </Stack>

      <Stack spacing={2} direction="row">
        <TextField
          label="Amount"
          InputProps={{
            startAdornment: <InputAdornment position="start">$</InputAdornment>,
          }}
        />
        <TextField
          label="weight"
          InputProps={{
            endAdornment: <InputAdornment position="end">kg</InputAdornment>,
          }}
        />
      </Stack>

      <Stack spacing={2} direction="row">
        <TextField
          label="password"
          InputProps={{
            endAdornment: (
              <InputAdornment position="end">
                <VisibilityIcon />
              </InputAdornment>
            ),
          }}
        />
      </Stack>
    </Stack>
  );
};
