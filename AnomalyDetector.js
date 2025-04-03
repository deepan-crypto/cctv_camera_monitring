import React, { useState } from "react";
import axios from "axios";

function AnomalyDetector() {
    const [status, setStatus] = useState("");

    const checkAnomaly = async () => {
        const data = { packet_size: 512, src_ip: "192.168.1.100", dst_port: 554, connection_time: 120 };
        const response = await axios.post("http://localhost:8000/detect", data);
        setStatus(response.data.status);
    };

    return (
        <div>
            <h2>AI-Based Anomaly Detector</h2>
            <button onClick={checkAnomaly}>Check Network Traffic</button>
            <p>Status: {status}</p>
        </div>
    );
}

export default AnomalyDetector;