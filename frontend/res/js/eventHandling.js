import LoadData from "./LoadData.js";
import ClickEvents from "./ClickEvents.js";

const loadDataFromBackend = new LoadData();
const click = new ClickEvents();

function clickPlanning(event) {
    click.clickPlanning();

    loadDataFromBackend.clear();
    loadDataFromBackend.loadData();
}

function clickMonitoring(event) {
    click.clickMonitoring();

    loadDataFromBackend.clear();
    loadDataFromBackend.loadData();
}

function clickReflecting(event) {
    click.clickReflecting();

    loadDataFromBackend.clear();
    loadDataFromBackend.loadData();
}

function clickTips(event) {
    click.clickTips();
}

document.getElementById("planning").addEventListener("click", clickPlanning);
document.getElementById("monitoring").addEventListener("click", clickMonitoring);
document.getElementById("reflecting").addEventListener("click", clickReflecting);
document.getElementById("tips").addEventListener("click", clickTips);