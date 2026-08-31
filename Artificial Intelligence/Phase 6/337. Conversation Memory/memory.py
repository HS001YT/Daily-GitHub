from collections import defaultdict


# ---------------------------------------------------------
# MEMORY CONFIGURATION
# ---------------------------------------------------------

MAX_MESSAGES = 20


# ---------------------------------------------------------
# CONVERSATION STORAGE
# ---------------------------------------------------------

conversation_memory = defaultdict(
    list
)


# ---------------------------------------------------------
# ADD MESSAGE
# ---------------------------------------------------------

def add_message(
    session_id,
    role,
    content
):

    conversation_memory[
        session_id
    ].append(
        {
            "role": role,
            "content": content
        }
    )


    trim_memory(
        session_id
    )


# ---------------------------------------------------------
# GET CONVERSATION
# ---------------------------------------------------------

def get_conversation(
    session_id
):

    return conversation_memory.get(
        session_id,
        []
    )


# ---------------------------------------------------------
# CLEAR CONVERSATION
# ---------------------------------------------------------

def clear_conversation(
    session_id
):

    conversation_memory.pop(
        session_id,
        None
    )


# ---------------------------------------------------------
# TRIM MEMORY
# ---------------------------------------------------------

def trim_memory(
    session_id
):

    history = conversation_memory.get(
        session_id
    )


    if not history:

        return


    if len(history) > MAX_MESSAGES:

        conversation_memory[
            session_id
        ] = history[
            -MAX_MESSAGES:
        ]


# ---------------------------------------------------------
# MEMORY COUNT
# ---------------------------------------------------------

def get_memory_count(
    session_id
):

    return len(
        get_conversation(
            session_id
        )
    )