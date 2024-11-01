window.onload = async function() {

    //TODO: make sure only those who are logged in can access the tutor
    // all of the other should be redirected to the login page

    // Setting active element
    
    activeElement = document.getElementsByClassName("on");
    activeSelection = sessionStorage.getItem('activeElement');
    setActiveElement(activeElement, activeSelection);
    

    if (sessionStorage.getItem("activeElement") != "tips"){

    //TODO fetch messages from DB - we need to know which was an answer & which a prompt to which topic
    
    //TODO fetch message response from AI, display and save in DB

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

    scrollToBottom();
}

function scrollToBottom(timedelay=0) {
    var scrollId;
    var height = 0;
    var minScrollHeight = 100;
    scrollId = setInterval(function () {
        if (height <= document.body.scrollHeight) {
            window.scrollBy(0, minScrollHeight);
        }
        else {
            clearInterval(scrollId);
        }
        height += minScrollHeight;
    }, timedelay);           
}