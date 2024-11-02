class GeneralFunctions {
    toggleDarkmode() {
        if (localStorage.getItem("darkMode") === "enabled") {
            document.body.classList.add("dark-mode");
        }
    }
}

export default GeneralFunctions;