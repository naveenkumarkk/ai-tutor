class ClickEvents {

    clickPlanning() {
        let currentElement = document.getElementsByClassName("on");
        if (currentElement.length == 1 && currentElement[0].id != "planning"){
            currentElement[0].classList.toggle("on");
        }
        document.getElementById("planning").classList.toggle("on");
        localStorage.setItem("activeElement", "planning");
    
        //TODO update history & change view
    }
    
    clickMonitoring() {
        let currentElement = document.getElementsByClassName("on");
        if (currentElement.length == 1 && currentElement[0].id != "monitoring"){
            currentElement[0].classList.toggle("on");
        }
        document.getElementById("monitoring").classList.toggle("on");
        localStorage.setItem("activeElement", "monitoring");
        //TODO update history & change view
    }
    
    clickReflecting() {
        let currentElement = document.getElementsByClassName("on");
        if (currentElement.length == 1 && currentElement[0].id != "reflecting"){
            currentElement[0].classList.toggle("on");
        }
        document.getElementById("reflecting").classList.toggle("on");
        localStorage.setItem("activeElement", "reflecting");
        //TODO update history & change view
    }
    
    clickTips(event) {
        localStorage.setItem("activeElement", "tips");
        window.location.href = "/chatgpt/tips";
    }
}

export default ClickEvents;