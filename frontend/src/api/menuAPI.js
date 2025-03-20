import axois from "axios";

const API_URL = "http://127.0.0.1:5000/";

export const fetchWendysData = async () => {
	try {
		const res = await axois.get(`${API_URL}/wendys `);
		return res.data;
	} catch (error) {
		console.error("Error fetching data:", error);
		return null;
	}
};
export const fetchMcDonaldsData = async () => {
	try {
		const res = await axois.get(`${API_URL}/mcdonalds`);
		return res.data;
	} catch (error) {
		console.error("Error fetching data", error);
		return null;
	}
};
