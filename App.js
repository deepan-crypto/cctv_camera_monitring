import React, { useState } from "react";
import axios from "axios";
import AnomalyDetector from "./AnomalyDetector";

function App() {
    const [cameras, setCameras] = useState([]);

    const scanNetwork = async () => {
        const response = await axios.get("http://localhost:8000/scan");
        setCameras(response.data.cameras);
    };

    return (
        <div>
            <h1>CCTV Scanner</h1>
            <button onClick={scanNetwork}>Scan Network</button>
            <table>
                <thead>
                    <tr>
                        <th>IP Address</th>
                        <th>Hostname</th>
                        <th>Open Ports</th>
                    </tr>
                </thead>
                <tbody>
                    {cameras.map((camera, index) => (
                        <tr key={index}>
                            <td>{camera.ip_address}</td>  {/* Updated property access */}
                            <td>{camera.hostname || "Unknown"}</td>
                            <td>{Object.keys(camera.open_ports).join(", ")}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
            <AnomalyDetector />
        </div>
    );
}

export default App;
