const chatContainer =
    document.getElementById(
        "chatContainer"
    );


const messageInput =
    document.getElementById(
        "messageInput"
    );


const sendButton =
    document.getElementById(
        "sendButton"
    );


const sendIcon =
    document.getElementById(
        "sendIcon"
    );


const loadingIcon =
    document.getElementById(
        "loadingIcon"
    );



/* --------------------------------------------------
   AUTO RESIZE TEXTAREA
-------------------------------------------------- */

function autoResize() {

    messageInput.style.height =
        "auto";


    messageInput.style.height =
        messageInput.scrollHeight
        + "px";

}


messageInput.addEventListener(
    "input",
    autoResize
);



/* --------------------------------------------------
   SCROLL TO BOTTOM
-------------------------------------------------- */

function scrollToBottom() {

    chatContainer.scrollTop =
        chatContainer.scrollHeight;

}



/* --------------------------------------------------
   CREATE MESSAGE
-------------------------------------------------- */

function addMessage(
    message,
    sender,
    isError = false
) {

    const messageElement =
        document.createElement(
            "div"
        );


    messageElement.classList.add(
        "message"
    );


    if (
        sender === "user"
    ) {

        messageElement.classList.add(
            "user-message"
        );

    }

    else {

        messageElement.classList.add(
            "assistant-message"
        );

    }


    if (isError) {

        messageElement.classList.add(
            "error-message"
        );

    }


    const avatar =
        document.createElement(
            "div"
        );


    avatar.classList.add(
        "avatar"
    );


    avatar.textContent =
        sender === "user"
            ? "YOU"
            : "AI";


    const content =
        document.createElement(
            "div"
        );


    content.classList.add(
        "message-content"
    );


    const name =
        document.createElement(
            "div"
        );


    name.classList.add(
        "message-name"
    );


    name.textContent =
        sender === "user"
            ? "You"
            : (
                isError
                    ? "Error"
                    : "AI Assistant"
            );


    const bubble =
        document.createElement(
            "div"
        );


    bubble.classList.add(
        "message-bubble"
    );


    bubble.textContent =
        message;


    content.appendChild(
        name
    );


    content.appendChild(
        bubble
    );


    messageElement.appendChild(
        avatar
    );


    messageElement.appendChild(
        content
    );


    chatContainer.appendChild(
        messageElement
    );


    scrollToBottom();

}



/* --------------------------------------------------
   TYPING INDICATOR
-------------------------------------------------- */

function showTyping() {

    const typingElement =
        document.createElement(
            "div"
        );


    typingElement.classList.add(
        "message",
        "assistant-message"
    );


    typingElement.id =
        "typingIndicator";


    typingElement.innerHTML = `

        <div class="avatar">
            AI
        </div>

        <div class="message-content">

            <div class="message-name">
                AI Assistant
            </div>

            <div class="message-bubble typing">

                <span></span>
                <span></span>
                <span></span>

            </div>

        </div>
    `;


    chatContainer.appendChild(
        typingElement
    );


    scrollToBottom();

}



function removeTyping() {

    const typingElement =
        document.getElementById(
            "typingIndicator"
        );


    if (typingElement) {

        typingElement.remove();

    }

}



/* --------------------------------------------------
   LOADING BUTTON
-------------------------------------------------- */

function setLoading(
    isLoading
) {

    sendButton.disabled =
        isLoading;


    if (isLoading) {

        sendIcon.style.display =
            "none";


        loadingIcon.classList.add(
            "show"
        );

    }

    else {

        sendIcon.style.display =
            "inline";


        loadingIcon.classList.remove(
            "show"
        );

    }

}



/* --------------------------------------------------
   SEND MESSAGE
-------------------------------------------------- */

async function sendMessage() {

    const message =
        messageInput.value.trim();


    if (!message) {

        return;

    }


    addMessage(
        message,
        "user"
    );


    messageInput.value =
        "";


    messageInput.style.height =
        "auto";


    setLoading(
        true
    );


    showTyping();


    try {

        const response =
            await fetch(

                "/api/chat",

                {
                    method:
                        "POST",

                    headers: {

                        "Content-Type":
                            "application/json"

                    },

                    body:

                        JSON.stringify(
                            {
                                message:
                                    message
                            }
                        )

                }
            );


        const data =
            await response.json();


        removeTyping();


        if (
            !response.ok
            ||
            !data.success
        ) {

            throw new Error(
                data.error
                ||
                "Unable to get an AI response."
            );

        }


        addMessage(
            data.response,
            "assistant"
        );

    }


    catch (error) {

        removeTyping();


        addMessage(

            error.message
            ||
            "Something went wrong.",

            "assistant",

            true

        );

    }


    finally {

        setLoading(
            false
        );


        messageInput.focus();

    }

}



/* --------------------------------------------------
   SEND BUTTON
-------------------------------------------------- */

sendButton.addEventListener(

    "click",

    sendMessage

);



/* --------------------------------------------------
   ENTER TO SEND
-------------------------------------------------- */

messageInput.addEventListener(

    "keydown",

    function (event) {

        if (

            event.key === "Enter"

            &&

            !event.shiftKey

        ) {

            event.preventDefault();


            sendMessage();

        }

    }

);



/* --------------------------------------------------
   INITIAL FOCUS
-------------------------------------------------- */

messageInput.focus();