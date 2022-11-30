import Header from "../components/Header";
import PostList from "../components/PostList";

function Home() {
  return (
    <>
      <div className="container">
        <Header />
        <PostList /> 
      </div>
    </>
  );
}

export default Home;
