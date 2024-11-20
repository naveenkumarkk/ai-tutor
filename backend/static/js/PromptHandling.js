import LoadData from "./LoadData.js";
const loadData = new LoadData();

class PromptHandling {

  async handlePrompt(prompt) {
    try {
      // Send message to Flask backend
      const response = await fetch("/chatgpt/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: prompt, conversation_type: localStorage.getItem("activeElement") }),
      });

      const data = await response.json();

      const messagesContainer = document.querySelector(".messages");
      const userMessageDiv = document.createElement("div");
      userMessageDiv.textContent = `You: ${prompt}`;
      messagesContainer.appendChild(userMessageDiv);

      if (data.response) {
        const botMessageDiv = document.createElement("div");
        botMessageDiv.textContent = `AI Tutor: ${data.response}`;
        messagesContainer.appendChild(botMessageDiv);
      } else {
        alert(data.error || "Error processing your message.");
      }
    } catch (error) {
      console.error("Error:", error);
      alert("An error occurred while communicating with the server.");
    }

    // Clear the input field
    document.getElementById("prompt").value = "";
    loadData.scrollToBottom();
  }

}

export default PromptHandling;