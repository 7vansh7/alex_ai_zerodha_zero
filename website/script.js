const url = "http://0.0.0.0:8000/cs";
// const url = "http://0.0.0.0:8000/ce"

async function postData(question, file = null) {
  let formData = new FormData();
  formData.append("question", question);
  if (file){formData.append('file',file)}
  try {
    const response = await fetch(url, {
      method: "POST",
      body: formData,
    });
    if (!response.ok) {
      const errorText = await response.text();
      console.log(errorText);
      throw new Error(
        "Network response was not ok " + response.statusText + ": " + errorText
      );
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("There has been a problem with your fetch operation:", error);
  }
}

async function msg_add(event) {
  if (event.key === "Enter" || event.type === "click") {
    console.log(event.type);
    let message = document.querySelector(".chat-input").value.trim();
    let file = document.getElementById("file_input").files[0];
    console.log(file);
    if (message) {
      let chatMessages = document.querySelector(".chat-messages");
      let messageContainer = document.createElement("div");
      messageContainer.classList.add("user");
      messageContainer.textContent = message;
      document.querySelector(".chat-messages").appendChild(messageContainer);
      chatMessages.scrollTop = chatMessages.scrollHeight;
      let answer;
      if (file) {
        answer = await postData(question = message, file = file);
      } else {
        answer = await postData(question = message);
      }
      console.log(answer);
      let botMessage = document.createElement("div");
      botMessage.classList.add("bot");
      botMessage.textContent = answer.answer;
      document.querySelector(".chat-messages").appendChild(botMessage);
      document.querySelector(".chat-input").value = "";
      chatMessages.scrollTop = chatMessages.scrollHeight;
      document.getElementById('file_input').value = ''
    }
  }
}

document.addEventListener("DOMContentLoaded", function () {
  const chatbotButton = document.querySelector(".open-chatbot-button");
  const chatContainer = document.querySelector(".chat-container");
  chatbotButton.addEventListener("click", function () {
    chatContainer.classList.toggle("hidden");
  });
  document.querySelector(".send-button").addEventListener("click", msg_add);
  document.querySelector(".chat-input").addEventListener("keydown", msg_add);
});
