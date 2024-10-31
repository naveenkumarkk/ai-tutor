function clickPlanning (event) {
    currentElement = document.getElementsByClassName("on");
    if (currentElement.length == 1 && currentElement[0].id != "planning"){
        currentElement[0].classList.toggle("on");
    }
    document.getElementById("planning").classList.toggle("on");
    sessionStorage.setItem("activeElement", "planning");
    //TODO update history & change view
}

function clickMonitoring (event) {
    currentElement = document.getElementsByClassName("on");
    if (currentElement.length == 1 && currentElement[0].id != "monitoring"){
        currentElement[0].classList.toggle("on");
    }
    document.getElementById("monitoring").classList.toggle("on");
    sessionStorage.setItem("activeElement", "monitoring");
    //TODO update history & change view

}

function clickReflecting (event) {
    currentElement = document.getElementsByClassName("on");
    if (currentElement.length == 1 && currentElement[0].id != "reflecting"){
        currentElement[0].classList.toggle("on");
    }
    document.getElementById("reflecting").classList.toggle("on");
    sessionStorage.setItem("activeElement", "reflecting");
    //TODO update history & change view

}

function clickTips (event) {
    sessionStorage.setItem("activeElement", "tips");
    window.location.href = "../../../frontend/pages/tips.html";

}

function navigatePlanning (event) {
    clickPlanning(event)
    window.location.href = "../../../frontend/pages/main.html";
}

function navigateMonitoring (event) {
    clickMonitoring(event)
    window.location.href = "../../../frontend/pages/main.html";
}

function navigateReflecting (event) {
    clickReflecting(event)
    window.location.href = "../../../frontend/pages/main.html";
}