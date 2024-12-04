class LoadData {

    clear() {
        const parent = document.getElementsByClassName("messages")[0];
        parent.innerHTML = '';
    }

    loadData() {
        const activeElement = localStorage.getItem("activeElement");

        if (activeElement === "monitoring") {
            document.title = "AI Tutor - Monitoring";
            this.getHistory()

        } else if (activeElement === "reflecting") {
            document.title = "AI Tutor - Reflecting";
            this.getHistory()

        } else if (activeElement == "tips") {
            window.location.href = "/chatgpt/tips";
            return;
        } else {
            localStorage.setItem("activeElement", "planning");
            document.title = "AI Tutor - Planning";
            this.getHistory()
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

    scrollToBottom(timedelay = 0) {
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

    async getHistory() {
        try {
            const parent = document.getElementsByClassName("messages")[0];
            parent.innerHTML = ''
            const response = await fetch("/chatgpt/history", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({conversation_type: localStorage.getItem("activeElement") }),
            });

            const data = await response.json();

            if (data?.reply) {
                for (let i = 0; i < data.reply.length; i++) {
                    this.addPromptAnswer(data.reply[i].prompt, data.reply[i].reply);
                }                
            } else {
                alert(data.error || "Error processing your message.");
            }
        } catch (error) {
            console.log(error);
            alert("An error occurred while communicating with the server.");
        }
        document.getElementById("prompt").value = "";
        this.scrollToBottom();
    }
}

export default LoadData;
