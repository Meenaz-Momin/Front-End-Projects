import {
  Box,
  Typography,
  ImageList,
  ImageListItem,
  ImageListItemBar,
} from "@mui/material";

function Imagelist() {
  return (
    <Box style={{ height: "800px", backgroundColor: "#F1F2F7" }}>
      <Typography variant="h4" style={{ padding: "30px", textAlign: "center", marginBottom:"30px"}}>
        Exclusive Services
      </Typography>
      <Box style={{ margin: "0 100px" }}>
        <ImageList cols={3} gap={80}>
          {itemData.map((item) => (
            <ImageListItem key={item.img} style={{ borderRadius: "50%" }}>
              <img
                src={`${item.img}?w=164&h=164&fit=crop&auto=format`}
                srcSet={`${item.img}?w=164&h=164&fit=crop&auto=format&dpr=2 2x`}
                alt={item.title}
                loading="lazy"
              />
              <ImageListItemBar
                title={item.title}
                subtitle={item.author}
                style={{
                  backgroundColor: "#C4C4C4",
                  opacity: 0.7,
                  color: "black",
                }}
              />
            </ImageListItem>
          ))}
        </ImageList>
      </Box>
    </Box>
  );
}

const itemData = [
  {
    img: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmS2ArMdruegYxM3lJCG6zvaxSC1F7Bb2Zjg&usqp=CAU",
    title: "Hair Cut",
  },
  {
    img: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmS2ArMdruegYxM3lJCG6zvaxSC1F7Bb2Zjg&usqp=CAU",
    title: "Hair Color",
  },
  {
    img: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmS2ArMdruegYxM3lJCG6zvaxSC1F7Bb2Zjg&usqp=CAU",
    title: "Foil Color",
  },
  {
    img: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmS2ArMdruegYxM3lJCG6zvaxSC1F7Bb2Zjg&usqp=CAU",
    title: "Styling",
  },
  {
    img: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmS2ArMdruegYxM3lJCG6zvaxSC1F7Bb2Zjg&usqp=CAU",
    title: "Hair Care",
  },
  {
    img: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmS2ArMdruegYxM3lJCG6zvaxSC1F7Bb2Zjg&usqp=CAU",
    title: "Waxing",
  },
];

export default Imagelist;
