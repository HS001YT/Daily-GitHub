const chatForm =
    document.getElementById("chatForm");

const messageInput =
    document.getElementById("messageInput");

const chatContainer =
    document.getElementById("chatContainer");

const sendButton =
    document.getElementById("sendButton");

const clearButton =
    document.getElementById("clearButton");

const statusElement =
    document.getElementById("status");


function scrollToBottom() {
    chatContainer.scrollTop =
        chatContainer.scrollHeight;
}


function createMessage(
    content,
    type
) {
    const message =
        document.createElement("div");

    message.classList.add(
        "message",
        type
    );

    const label =
        document.createElement("div");

    label.classList.add(
        "message-label"
    );

    label.textContent =
        type === "user"
            ? "You"
            : "AI";


    const text =
        document.createElement("div");

    text.classList.add(
        "message-text"
    );

    text.textContent =
        content;


    message.appendChild(label);

    message.appendChild(text);

    chatContainer.appendChild(
        message
    );

    scrollToBottom();

    return text;
}


function showStatus(message) {
    statusElement.textContent =
        message;
}


function setLoading(isLoading) {
    sendButton.disabled =
        isLoading;

    messageInput.disabled =
        isLoading;

    clearButton.disabled =
        isLoading;

    if (isLoading) {
        sendButton.textContent =
            "Thinking...";
    } else {
        sendButton.textContent =
            "Send";
    }
}


async function sendMessage(
    message
) {

    createMessage(
        message,
        "user"
    );


    const aiMessage =
        createMessage(
            "",
            "ai"
        );


    setLoading(true);

    showStatus(
        "AI is generating a response..."
    );


    try {

        const response =
            await fetch(
                "/chat",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        message: message
                    })
                }
            );


        if (!response.ok) {

            let errorMessage =
                "Unable to connect to the AI.";

            try {

                const errorData =
                    await response.json();

                errorMessage =
                    errorData.error
                    || errorMessage;

            } catch (error) {
                console.error(error);
            }


            throw new Error(
                errorMessage
            );
        }


        if (!response.body) {

            throw new Error(
                "Streaming is not supported by this browser."
            );
        }


        const reader =
            response.body.getReader();

        const decoder =
            new TextDecoder();

        let responseText =
            "";


        while (true) {

            const {
                done,
                value
            } =
                await reader.read();


            if (done) {
                break;
            }


            const chunk =
                decoder.decode(
                    value,
                    {
                        stream: true
                    }
                );


            responseText +=
                chunk;


            aiMessage.textContent =
                responseText;


            scrollToBottom();
        }


        if (!responseText.trim()) {

            aiMessage.textContent =
                "The AI returned an empty response.";
        }


        showStatus("");

    } catch (error) {

        console.error(
            "Chat error:",
            error
        );


        aiMessage.textContent =
            "Error: "
            + error.message;


        showStatus(
            "Unable to complete the request."
        );

    } finally {

        setLoading(false);

        messageInput.focus();
    }
}


chatForm.addEventListener(
    "submit",
    async function (event) {

        event.preventDefault();


        const message =
            messageInput.value.trim();


        if (!message) {
            return;
        }


        messageInput.value =
            "";


        await sendMessage(
            message
        );
    }
);


clearButton.addEventListener(
    "click",
    async function () {

        try {

            const response =
                await fetch(
                    "/clear",
                    {
                        method: "POST"
                    }
                );


            if (!response.ok) {

                throw new Error(
                    "Unable to clear conversation."
                );
            }


            chatContainer.innerHTML =
                `
                <div class="welcome-message">
                    <h2>Conversation Cleared</h2>
                    <p>
                        Start a new conversation.
                    </p>
                </div>
                `;


            showStatus("");

        } catch (error) {

            showStatus(
                error.message
            );
        }
    }
);


messageInput.addEventListener(
    "keydown",
    function (event) {

        if (
            event.key === "Enter"
            && !event.shiftKey
        ) {

            event.preventDefault();


            chatForm.requestSubmit();
        }
    }
);


messageInput.addEventListener(
    "input",
    function () {

        this.style.height =
            "auto";

        this.style.height =
            Math.min(
                this.scrollHeight,
                150
            )
            + "px";
    }
);