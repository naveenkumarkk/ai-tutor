function openHelpPage () {
    window.location.href = "../../../frontend/pages/help.html";
}

function openMenuPopup () {
    document.getElementById("menu_container").classList.toggle("open");

}

document.getElementById("help").addEventListener("click", openHelpPage);
document.getElementById("menu").addEventListener("click", openMenuPopup);