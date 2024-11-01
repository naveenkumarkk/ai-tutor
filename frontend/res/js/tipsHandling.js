import ClickEvents from "./ClickEvents.js";

const click = new ClickEvents();

function clickPlanning (event) {
    click.clickPlanning();
    window.location.href = "../../../frontend/pages/main.html";
}

function clickMonitoring (event) {
    click.clickMonitoring();
    window.location.href = "../../../frontend/pages/main.html";
}

function clickReflecting (event) {
    click.clickReflecting();
    window.location.href = "../../../frontend/pages/main.html";
}

document.getElementById("planning").addEventListener("click", clickPlanning);
document.getElementById("monitoring").addEventListener("click", clickMonitoring);
document.getElementById("reflecting").addEventListener("click", clickReflecting);