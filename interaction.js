document.addEventListener("DOMContentLoaded", () => {
    const chatBox = document.getElementById("chat-box");
    const userInput = document.getElementById("user-input");
    const sendButton = document.getElementById("send-button");

    function appendMessage(sender, message) {
        const messageElement = document.createElement("div");
        messageElement.classList.add("message", sender);
        messageElement.textContent = message;
        chatBox.appendChild(messageElement);
        chatBox.scrollTop = chatBox.scrollHeight; // Scroll to bottom
    }

    async function sendMessage() {
        const message = userInput.value.trim();
        if (message === "") return;

        appendMessage("user", message);
        userInput.value = "";

        try {
            const response = await fetch("/get_response", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ message: message }),
            });

            const data = await response.json();
            if (data.response) {
                appendMessage("bot", data.response);
            } else if (data.error) {
                appendMessage("bot", "Error: " + data.error);
            }
        } catch (error) {
            console.error("Error sending message:", error);
            appendMessage("bot", "Oops! Something went wrong. Please try again.");
        }
    }

    sendButton.addEventListener("click", sendMessage);

    userInput.addEventListener("keypress", (e) => {
        if (e.key === "Enter") {
            sendMessage();
        }
    });

    // Initial bot message
    appendMessage("bot", "Hi User! How can I help you today with ExecuMate AI?");
});
