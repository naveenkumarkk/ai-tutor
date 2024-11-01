import LoadData from "./LoadData.js";
import ClickEvents from "./ClickEvents.js";
import PromptHandling from "./PromptHandling.js";

const loadDataFromBackend = new LoadData();
const click = new ClickEvents();
const promptHandling = new PromptHandling();

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

function submitForm(event) {
    event.preventDefault();

    const form = document.getElementById("promptInput");
    const prompt = new FormData(form).get("prompt");

    //TODO: save data in DB & get response from AI for answer
    promptHandling.handlePrompt(prompt);

    form.reset();
}

document.getElementById("planning").addEventListener("click", clickPlanning);
document.getElementById("monitoring").addEventListener("click", clickMonitoring);
document.getElementById("reflecting").addEventListener("click", clickReflecting);
document.getElementById("tips").addEventListener("click", clickTips);
document.getElementById("promptInput").addEventListener("submit", submitForm);
document.addEventListener('keydown', function(event) {
    if ((event.key === 'Enter') && (event.metaKey || event.ctrlKey) && document.getElementById("prompt").value.trim() !== '') {
        submitForm(event);
    }
});