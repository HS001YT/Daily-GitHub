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


const memoryCount =
    document.getElementById(
        "memoryCount"
    );


const clearMemoryButton =
    document.getElementById(
        "clearMemoryButton"
    );



/* --------------------------------------------------
   AUTO RESIZE
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
   SCROLL
-------------------------------------------------- */

function scrollToBottom() {

    chatContainer.scrollTop =
        chatContainer.scrollHeight;

}



/* --------------------------------------------------
   UPDATE MEMORY COUNT
-------------------------------------------------- */

function updateMemoryCount(
    count
) {

    memoryCount.textContent =
        count;

}



/* --------------------------------------------------
   LOAD MEMORY STATUS
-------------------------------------------------- */

async function loadMemoryStatus() {

    try {

        const response =
            await fetch(
                "/api/memory"
            );


        const data =
            await response.json();


        if (
            data.success
        ) {

            updateMemoryCount(
                data.memory_count
            );

        }

    }

    catch (error) {

        console.error(
            "Unable to load memory:",
            error
        );

    }

}



/* --------------------------------------------------
   ADD MESSAGE
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


    messageElement.classList.add(

        sender === "user"
            ? "user-message"
            : "assistant-message"

    );


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
   BUTTON LOADING
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


        updateMemoryCount(
            data.memory_count
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
   CLEAR MEMORY
-------------------------------------------------- */

async function clearMemory() {

    const confirmed =
        confirm(
            "Clear the conversation memory?"
        );


    if (!confirmed) {

        return;

    }


    try {

        clearMemoryButton.disabled =
            true;


        const response =
            await fetch(

                "/api/clear-memory",

                {
                    method:
                        "POST"
                }

            );


        const data =
            await response.json();


        if (

            !response.ok

            ||

            !data.success

        ) {

            throw new Error(
                "Unable to clear memory."
            );

        }


        updateMemoryCount(
            0
        );


        addMessage(

            "Conversation memory has been cleared. "
            + "I will no longer remember previous "
            + "messages from this session.",

            "assistant"

        );

    }


    catch (error) {

        addMessage(

            "Unable to clear conversation memory.",

            "assistant",

            true

        );

    }


    finally {

        clearMemoryButton.disabled =
            false;

    }

}



/* --------------------------------------------------
   EVENTS
-------------------------------------------------- */

sendButton.addEventListener(
    "click",
    sendMessage
);


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


clearMemoryButton.addEventListener(
    "click",
    clearMemory
);



/* --------------------------------------------------
   INITIAL LOAD
-------------------------------------------------- */

loadMemoryStatus();


messageInput.focus();