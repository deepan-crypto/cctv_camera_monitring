document.getElementById("scanButton").addEventListener("click", async () => {
    try {
        const response = await fetch("http://localhost:8000/scan");
        const data = await response.json();
        const tableBody = document.querySelector("#resultsTable tbody");
        tableBody.innerHTML = "";

        data.cameras.forEach(camera => {
            const row = `<tr>
                <td>${camera.ip}</td>
                <td>${camera.hostname || "Unknown"}</td>
                <td>${Object.keys(camera.open_ports).join(", ")}</td>
            </tr>`;
            tableBody.innerHTML += row;
        });
    } catch (error) {
        console.error("Error fetching data:", error);
    }
    const API_BASE_URL = "https://your-backend-url.com";


});