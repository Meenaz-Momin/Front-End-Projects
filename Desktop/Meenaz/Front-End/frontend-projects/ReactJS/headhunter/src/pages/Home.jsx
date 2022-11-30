import { FaEnvelope, FaInstagram, FaMobile } from "react-icons/fa";

function Home() {
  return (
    <>
      <div className="rectangle-6">
        <ul>
          <li>
            <FaMobile color="white" size={30} />
            <span>987654321</span>
          </li>
          <li>
            <FaInstagram color="white" size={30} />
          </li>
          <li>
            <FaEnvelope color="white" size={30} />
          </li>
        </ul>
      </div>

      <div className="rectangle-8">
        <ul>
          <li>About us</li>
          <li>Gallery</li>
          <li>Stylist</li>
          <li>Services</li>
          <li>Home</li>
        </ul>
      </div>

      <div className="rectangle-14">
        <div className="text-left">
          <header>Headhunter Hairstyling</header>
          <p>SERVING PANSCOLA SINCE 1987</p>
          <button className="btn">Book Now</button>
        </div>
        <div className="img-left"></div>
      </div>

      <div className="rectangle">
        <header>Welcome to Headhunter Hairstyle</header>
        <p>
          We're excited that you found us and are interested in learning more
          about our stylists and services. Take a look around, call us, or stop
          by and we'll be happy to show you why we've been a staple in historic
          Pensacola since 1978. We're conveniently located in Downtown Pensacola
          and within walking distance to most businesses and restaurants in the
          area. Find our more <a href="/">About Us</a>
        </p>
      </div>

      <div className="rectangle-15">
        <header>Exclusive Services</header>
        <div className="grid">
            <div><img src="../img.jpg" alt=" " /></div>
            <div><img src="" alt=" " /></div>
            <div><img src="" alt=" " /></div>
            <div><img src="" alt=" " /></div>
            <div><img src="" alt=" " /></div>
            <div><img src="" alt=" " /></div>
        </div>
      </div>
    </>
  );
}

export default Home;
