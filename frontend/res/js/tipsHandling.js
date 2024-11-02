import ClickEvents from "./ClickEvents.js";
import GeneralFunctions from "./GeneralFunctions.js";

const click = new ClickEvents();
const generalFunctions = new GeneralFunctions();

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

window.onload = async function () {
    generalFunctions.toggleDarkmode();
}

document.getElementById("planning").addEventListener("click", clickPlanning);
document.getElementById("monitoring").addEventListener("click", clickMonitoring);
document.getElementById("reflecting").addEventListener("click", clickReflecting);