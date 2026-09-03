function sendMessage() {
    let input = document.getElementById("userInput");
    let message = input.value;

    if (message == "") {
        return;
    }

    let messages = document.getElementById("messages");

    messages.innerHTML += "<p class='user'>You: " + message + "</p>";

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: message
        })
    })
    .then(response => response.json())
    .then(data => {
        messages.innerHTML += "<p class='bot'>Bot: " + data.response + "</p>";
    });

    input.value = "";
}