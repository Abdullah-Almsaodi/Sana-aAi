// LOADER
window.addEventListener('load', () => {
    setTimeout(() => {
        document.querySelector(".loader-warpper").classList.toggle("loader-warpper-hide");
    }, 1000);
})

// MENU MOBILE
function MenuMobile() {
    document.getElementById("MenuMobile").classList.toggle("MenuMobileStyle");
    document.getElementById("chatsMobile").classList.toggle("chatsMobileStyle");

    const footerMainWindow = document.getElementById("footerMainWindow");
    footerMainWindow.classList.toggle("footerMainWindowStyle");
}

// SIDEBAR
// CHATS TOGGLE
function chatsToggle() {
    document.getElementById("chatsToggle").classList.toggle("chatsToggleStyle");
}
// AVATAR DROPDOWN TOGGLE
function avatarDropdownToggle() {
    document.getElementById("avatarDropdownToggle").classList.toggle("avatarDropdownToggleStyle");
}
// SETTINGS TOGGLE
function settingsToggle() {
    document.getElementById("settingsToggle").classList.toggle("settingsToggleStyle");
}
// MORE TOGGLE
function moreToggle() {
    document.getElementById("moreToggle").classList.toggle("moreToggleStyle");
}
// NEW CHAT & REMOVE CHAT
function newChat() {
    var newChatBody = document.getElementById("newChatBody");
    var newChatCard = document.getElementById("newChatCard");

    newChatBody.appendChild(newChatCard.style.display = "block");
}

function removeChat() {
    var removeChat = document.getElementById("removeChat");

    removeChat.appendChild(newChatCard.style.display = "none");
}

// TOGGLE MODE
function toggleMode() {
    document.body.classList.toggle("toggleModeStyle");
    document.getElementById("farDarkToggleModeBtn").classList.toggle("farDarkToggleModeBtnStyle");
    document.getElementById("farLightToggleModeBtn").classList.toggle("farLightToggleModeBtnStyle");
}
var nowDate = new Date();
if (nowDate.getHours() >= 18 ^ nowDate.getHours() == 00) {
    document.body.classList.toggle("toggleModeStyle");
    document.getElementById("farDarkToggleModeBtn").classList.toggle("farDarkToggleModeBtnStyle");
    document.getElementById("farLightToggleModeBtn").classList.toggle("farLightToggleModeBtnStyle");
} else {

}

// MAIN WINDOW
function renameConversation() {
    var conversationName = document.getElementById("conversationName");
    var chatsConversationName = document.getElementById("chatsConversationName");
    var renameConversationPrompt = prompt("Rename Chat", conversationName.innerHTML);

    conversationName.innerHTML = renameConversationPrompt;
    chatsConversationName.innerHTML = renameConversationPrompt;
    if (renameConversationPrompt == null || renameConversationPrompt == "") {
        conversationName.innerHTML = "New Conversation";
        chatsConversationName.innerHTML = "New Conversation";
    } else {

    }
}

// INPUTS
function textareaResize(ts) {
    ts.classList.toggle("textareaResizeStyle");
}
// SETTINGS FONT SIZE
const inputNumber = document.getElementById("inputNumber");
const chatSectionMessageItemFontSize = document.getElementById("chatSectionMessageItemFontSize");
inputNumber.oninput = () => {
    chatSectionMessageItemFontSize.style.fontSize = inputNumber.value + "px";
}

// Function to send message to Flask API and display response
function sendMessage() {
    var message = document.getElementById('user-input').value.trim();
    if (message !== '') {
        fetch('/api/chat', { // Send requests to the Flask API endpoint
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    message: message
                })
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                // Handle response from the server
                // Display the response in the chat window
                displayMessage('You', message);
                displayMessage('Bot', data.response);
                scrollToBottom(); // Scroll to bottom after new message is displayed
            })
            .catch(error => console.error('Error:', error));
    }
    document.getElementById('user-input').value = ''; // Clear input field after sending message
}

// Function to display messages in the chat
function displayMessage(sender, message) {
    // Replace this with your logic to display messages
    var chatSection = document.querySelector('.chat-section');

    var messageCard = document.createElement('div');
    messageCard.className = 'chat-section-message-card';

    var avatar = document.createElement('img');
    avatar.src = sender === 'Bot' ? '{% static "frontend/images/logo/SVG/IntelliAI_Logo_Icon.svg" %}' : '{% static "frontend/images/avatar/Abdullah.jpg" %}';
    avatar.alt = '';
    avatar.draggable = false;

    var messageItem = document.createElement('div');
    messageItem.className = 'chat-section-message-item';
    messageItem.innerHTML = '<p>' + message + '</p>';

    var messageActions = document.createElement('div');
    messageActions.className = 'chat-section-message-actions';
    messageActions.innerHTML = getCurrentTime(); // Add a function to get the current time

    messageCard.appendChild(avatar);
    messageCard.appendChild(messageItem);
    messageCard.appendChild(messageActions);

    chatSection.appendChild(messageCard);
}

// Function to get the current time in the format HH:mm:ss
function getCurrentTime() {
    var now = new Date();
    var hours = now.getHours();
    var minutes = now.getMinutes();
    var seconds = now.getSeconds();

    // Add leading zeros if needed
    hours = hours < 10 ? '0' + hours : hours;
    minutes = minutes < 10 ? '0' + minutes : minutes;
    seconds = seconds < 10 ? '0' + seconds : seconds;

    return hours + ':' + minutes + ':' + seconds;
}

// Function to scroll to the bottom of the chat section with smooth animation
function scrollToBottom() {
    var chatSection = document.querySelector('.chat-section');
    var lastMessage = chatSection.lastElementChild;
    lastMessage.scrollIntoView({
        behavior: 'smooth'
    });
}

// Add event listener for Send button click
document.getElementById('submit').addEventListener('click', function (e) {
    e.preventDefault();
    sendMessage();
});

// Add event listener for Enter key press
document.getElementById('user-input').addEventListener('keydown', function (e) {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
    }
});