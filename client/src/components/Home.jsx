import { useState ,useEffect } from "react"
const Home = () => {
    const [data, setData] = useState([])
    useEffect(() => {
        fetch("http://localhost:5000/crop")
        .then(res => res.json())
        .then(data => setData(data))
    }, [])
    console.log(data)
  return (
      <p className="text-3xl bg-green-400 text-center">Crop Yeild Production</p>
     
  )
}

export default Home