import LoadData from "./LoadData.js";

const loadData = new LoadData();

class PromptHandling {

    handlePrompt (prompt) {
        const parent = document.getElementsByClassName("messages")[0];
        parent.appendChild(loadData.addPrompt(prompt));
        this.getAnswer(prompt);
    }

    getAnswer (prompt) {
        //TODO: answer handling with AI request and catching error
        try {

        } catch {

        }
        const parent = document.getElementsByClassName("messages")[0];
        parent.appendChild(loadData.addAnswer("answer"));
        loadData.scrollToBottom();
    }
}

export default PromptHandling;