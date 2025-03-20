import React, { useEffect, useState } from "react";
import { fetchWendysData, fetchMcDonaldsData } from "./api/menuAPI";
import "./App.css";

function App() {
	const [data, setData] = useState(null);
	const [mcdonaldsData, setMcDonaldsData] = useState(null);
	useEffect(() => {
		fetchWendysData().then(setData);
	}, []);
	useEffect(() => {
		fetchMcDonaldsData().then(setMcDonaldsData);
	});
	return (
		<>
			<h1>Fast Food Random</h1>
			{/* {data ? <pre>{JSON.stringify(data, null, 2)}</pre> : <p>Loading...</p>} */}
			{mcdonaldsData ? (
				<pre>{JSON.stringify(mcdonaldsData, null, 2)}</pre>
			) : (
				<p>Loading...</p>
			)}
		</>
	);
}

export default App;
