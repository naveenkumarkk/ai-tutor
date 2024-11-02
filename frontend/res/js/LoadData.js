class LoadData {

    clear() {
        const parent = document.getElementsByClassName("messages")[0];
        parent.innerHTML = '';
    }

    loadData() {
        const activeElement = sessionStorage.getItem("activeElement");

        if (activeElement === "monitoring") {
            // Render monitoring
            document.title = "AI Tutor - Monitoring";
            this.addPromptAnswer("This is a monitoring prompt!", "This is a monitoring answer!");
            this.addPromptAnswer("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?");
            //TODO fetch messages from DB - we need to know which was an answer & which a prompt to which topic
            //TODO fetch message response from AI, display and save in DB
        
        } else if (activeElement === "reflecting") {
            // Render reflecting
            document.title = "AI Tutor - Reflecting";
            this.addPromptAnswer("This is a reflecting prompt!", "This is a reflecting answer!");
            this.addPromptAnswer("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?");
            //TODO fetch messages from DB - we need to know which was an answer & which a prompt to which topic
            //TODO fetch message response from AI, display and save in DB
        
        } else if (activeElement == "planning") {
            // Render planning
            document.title = "AI Tutor - Planning";
            this.addPromptAnswer("This is a planning prompt!", "This is a planning answer!");
            this.addPromptAnswer("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?");
            //TODO fetch messages from DB - we need to know which was an answer & which a prompt to which topic
            //TODO fetch message response from AI, display and save in DB
        } else if (activeElement == "tips"){
            window.location.href = "../../../frontend/pages/tips.html";
            return;
        } else {
            window.location.href = "../../../frontend/pages/login.html";
            return;
        }

        this.scrollToBottom();
    }

    addPromptAnswer(prompt, answer) {
        const parent = document.getElementsByClassName("messages")[0];
        parent.appendChild(this.addPrompt(prompt));
        parent.appendChild(this.addAnswer(answer));
    }
    
    addPrompt(message) {
        const prompt = document.createElement("p");
        prompt.className = "prompt";
        prompt.innerText = message;
        return prompt;
    }
    
    addAnswer(message) {
        const answerContainer = document.createElement("div");
        answerContainer.className = "answer_container";
        answerContainer.innerHTML = `
            <div class="icon logo">
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#000000">
                    <path d="M280-280h160v-160H280v160Zm240 0h160v-160H520v160ZM280-520h160v-160H280v160Zm240 0h160v-160H520v160ZM200-120q-33 0-56.5-23.5T120-200v-560q0-33 23.5-56.5T200-840h560q33 0 56.5 23.5T840-760v560q0 33-23.5 56.5T760-120H200Zm0-80h560v-560H200v560Zm0-560v560-560Z"/>
                </svg>
            </div>
            <p class="answer">${message}</p>
        `;
        return answerContainer;
    }

    scrollToBottom(timedelay=0) {
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
        
        // MORE Smoothly: 
        // const answerContainers = document.querySelectorAll('.answer_container');
        // if (answerContainers.length > 0) {
        //   const lastAnswerContainer = answerContainers[answerContainers.length - 1];
        //   lastAnswerContainer.scrollIntoView({ behavior: 'smooth' });
        // }
    }
}

export default LoadData;
