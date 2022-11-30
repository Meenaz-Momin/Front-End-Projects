import { Typography } from "@mui/material";

export const MuiTypography = () => {
  return (
    <div>
      <Typography variant="h1">H1 Heading</Typography>
      <Typography variant="h2">H2 Heading</Typography>
      <Typography variant="h3">H3 Heading</Typography>
      <Typography variant="h4">H4 Heading</Typography>
      <Typography variant="h5">H5 Heading</Typography>
      <Typography variant="h6" component="h1" gutterBottom>
        H6 Heading
      </Typography>

      <Typography variant="subtitle1">Sub Title 1</Typography>
      <Typography variant="subtitle2">Sub Title 2</Typography>

      <Typography variant="body1">
        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Architecto
        voluptatibus tempore optio maiores quas, quam deserunt tempora at
        officia fugiat cupiditate dolorem consectetur ipsam provident
        reprehenderit sequi excepturi accusantium illum.
      </Typography>
      <Typography variant="body2">
        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Corporis
        maxime aspernatur consequuntur non quod sint eaque tenetur architecto
        nulla veritatis officia facere saepe nostrum deleniti earum, quisquam
        eveniet? Perferendis, consectetur?
      </Typography>
    </div>
  );
};
