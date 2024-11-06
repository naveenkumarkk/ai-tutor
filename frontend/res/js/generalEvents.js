function openHelpPage () {
    window.location.href = "../../../frontend/pages/help.html";
}

function openMenuPopup () {
    document.getElementById("menu_container")?.classList.toggle("open");

    const darkModeToggle = document.getElementById("darkmode-toggle");

    if (localStorage.getItem("darkMode") === "enabled") {
        document.body.classList.add("dark-mode");
        darkModeToggle.checked = true;
    }

    darkModeToggle.addEventListener("change", () => {
        document.body.classList.toggle("dark-mode");

        if (document.body.classList.contains("dark-mode")) {
            localStorage.setItem("darkMode", "enabled");
        } else {
            localStorage.setItem("darkMode", "disabled");
        }
    });

    document.getElementById("logout")?.addEventListener("click", handleLogout);
}

function handleLogout(event){
    event.preventDefault();
    localStorage.removeItem("activeElement");
    window.location.href = "../../../frontend/pages/login.html";
}

document.getElementById("help")?.addEventListener("click", openHelpPage);
document.getElementById("menu")?.addEventListener("click", openMenuPopup);