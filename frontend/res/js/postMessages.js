window.onload = async function() {

    //TODO: make sure only those who are logged in can access the tutor
    // all of the other should be redirected to the login page

    // Setting active element
    activeElement = document.getElementsByClassName("on");
    activeSelection = sessionStorage.getItem('activeElement');
    if (activeElement.length != 1){
        document.getElementById("planning").classList.toggle("on");
    }else if (activeElement[0].id != activeSelection){
        activeElement[0].classList.toggle("on");
        document.getElementById(activeSelection).classList.toggle("on");
    }

    if (sessionStorage.getItem("activeElement") == "tips"){
        postTips();
    } else {

    //TODO fetch messages from DB - we need to know which was an answer & which a prompt to which topic
    
    //TODO fetch message response from AI, display and save in DB

    }
}