import LoadData from "./LoadData.js";
import GeneralFunctions from "./GeneralFunctions.js";

const loadDataFromBackend = new LoadData();
const generalFunctions = new GeneralFunctions();

window.onload = async function() {

    //TODO: make sure only those who are logged in can access the tutor
    // all of the other should be redirected to the login page

    // Setting active element
    let activeElement = document.getElementsByClassName("on");
    let activeSelection = localStorage.getItem('activeElement');
    setActiveElement(activeElement, activeSelection);
    generalFunctions.toggleDarkmode();
    loadDataFromBackend.loadData();
}

function setActiveElement(activeElement, activeSelection){
    if (activeSelection == null){
        return document.getElementById("planning").classList.toggle("on");
    }
    
    if (activeElement.length == 0){
        return document.getElementById(activeSelection).classList.toggle("on");
    } 
    
    if (activeElement[0].id != activeSelection){
        activeElement[0].classList.toggle("on");
        return document.getElementById(activeSelection).classList.toggle("on");
    }
}