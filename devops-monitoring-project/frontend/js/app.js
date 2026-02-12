console.log("Frontend loaded");

// ----------------------------------------------------------
// GLOBAL CHART VARIABLES
// ----------------------------------------------------------
let cpuChart, memoryChart;

// ----------------------------------------------------------
// INITIALIZE CHARTS
// ----------------------------------------------------------
function initCharts() {
    const cpuCtx = document.getElementById("cpuChart").getContext("2d");
    cpuChart = new Chart(cpuCtx, {
        type: "line",
        data: {
            labels: [],
            datasets: [{
                label: "CPU Usage (%)",
                data: [],
                borderWidth: 2
            }]
        },
        options: {
            responsive: true
        }
    });

    const memCtx = document.getElementById("memoryChart").getContext("2d");
    memoryChart = new Chart(memCtx, {
        type: "line",
        data: {
            labels: [],
            datasets: [{
                label: "Memory Usage (MB)",
                data: [],
                borderWidth: 2
            }]
        },
        options: {
            responsive: true
        }
    });
}

// ----------------------------------------------------------
// FETCH CPU USAGE
// ----------------------------------------------------------
async function loadCPU() {
    const res = await fetch("http://localhost:5000/api/cpu");
    const data = await res.json();
    const cpu = data.cpu;

    document.getElementById("cpu_value").innerText = cpu + "%";

    const time = new Date().toLocaleTimeString();
    cpuChart.data.labels.push(time);
    cpuChart.data.datasets[0].data.push(cpu);

    if (cpuChart.data.labels.length > 20) {
        cpuChart.data.labels.shift();
        cpuChart.data.datasets[0].data.shift();
    }

    cpuChart.update();
}

// ----------------------------------------------------------
// FETCH MEMORY USAGE
// ----------------------------------------------------------
async function loadMemory() {
    const res = await fetch("http://localhost:5000/api/memory");
    const data = await res.json();
    const memory = data.memory;

    document.getElementById("memory_value").innerText = memory + " MB";

    const time = new Date().toLocaleTimeString();
    memoryChart.data.labels.push(time);
    memoryChart.data.datasets[0].data.push(memory);

    if (memoryChart.data.labels.length > 20) {
        memoryChart.data.labels.shift();
        memoryChart.data.datasets[0].data.shift();
    }

    memoryChart.update();
}

// ----------------------------------------------------------
// FETCH NETWORK USAGE
// ----------------------------------------------------------
async function loadNetwork() {
    const res = await fetch("http://localhost:5000/api/network");
    const data = await res.json();

    document.getElementById("network_rx").innerText = data.rx + " KB";
    document.getElementById("network_tx").innerText = data.tx + " KB";
}

// ----------------------------------------------------------
// FETCH AI INSIGHT
// ----------------------------------------------------------
async function loadAI() {
    const res = await fetch("http://localhost:5000/api/ai");
    const data = await res.json();
    document.getElementById("ai_text").innerText = data.insight;
}

// ----------------------------------------------------------
// AUTO REFRESH
// ----------------------------------------------------------
function autoRefresh() {
    loadCPU();
    loadMemory();
    loadNetwork();
    loadAI();
}

// ----------------------------------------------------------
// INITIALIZE EVERYTHING
// ----------------------------------------------------------
initCharts();
setInterval(autoRefresh, 3000);
