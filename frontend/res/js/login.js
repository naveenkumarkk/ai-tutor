function handleLogin (event) {
    event.preventDefault();

    const form = document.getElementById("login");

    const formData = new FormData(form);
    const username = formData.get("username");
    const password = formData.get("password");

    sessionStorage.setItem("activeElement", "planning");

    //TODO validating
    window.location.href = "../../../frontend/pages/main.html";
}