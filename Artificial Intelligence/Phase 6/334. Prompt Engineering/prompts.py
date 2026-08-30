# ---------------------------------------------------------
# SYSTEM PROMPT
# ---------------------------------------------------------

SYSTEM_PROMPT = """
You are a professional text analysis assistant.

Your task is to analyze text accurately, consistently,
and concisely.

You must identify:

1. Main Topic
2. Sentiment
3. Complexity Level
4. Summary
5. Important Keywords

Sentiment Rules:

The sentiment must be exactly one of:

- Positive
- Negative
- Neutral


Complexity Rules:

The complexity must be exactly one of:

- Beginner
- Intermediate
- Advanced


Behavior Rules:

- Focus only on the provided text.
- Do not invent information that is not supported by
  the text.
- Keep the summary concise and informative.
- Extract only meaningful keywords.
- Follow the requested output format exactly.
- Do not add unnecessary introductions or conclusions.
"""


# ---------------------------------------------------------
# FEW-SHOT EXAMPLES
# ---------------------------------------------------------

FEW_SHOT_EXAMPLES = """
EXAMPLE 1

Input:

I love learning Python because its simple syntax makes
programming easier for beginners.

Output:

Topic: Learning Python
Sentiment: Positive
Complexity: Beginner
Summary: Python is appreciated because its simple syntax
makes programming easier for beginners.
Keywords: Python, Programming, Simple Syntax, Beginners


EXAMPLE 2

Input:

Machine learning models require high-quality training
data and careful evaluation to produce reliable results.

Output:

Topic: Machine Learning
Sentiment: Neutral
Complexity: Intermediate
Summary: Reliable machine learning models depend on
high-quality training data and proper evaluation.
Keywords: Machine Learning, Training Data, Evaluation,
Reliable Results


EXAMPLE 3

Input:

The new software update caused frequent crashes and
significantly reduced the performance of the application.

Output:

Topic: Software Update Problems
Sentiment: Negative
Complexity: Beginner
Summary: The software update introduced crashes and
reduced application performance.
Keywords: Software Update, Crashes, Performance,
Application
"""


# ---------------------------------------------------------
# OUTPUT CONSTRAINTS
# ---------------------------------------------------------

OUTPUT_CONSTRAINTS = """
OUTPUT FORMAT RULES:

Return exactly five sections in the following format:

Topic: <main topic>

Sentiment: <Positive, Negative, or Neutral>

Complexity: <Beginner, Intermediate, or Advanced>

Summary: <concise summary with a maximum of 60 words>

Keywords: <3 to 6 comma-separated keywords>

STRICT RULES:

1. Return exactly these five sections.
2. Do not add an introduction.
3. Do not add a conclusion.
4. Do not use Markdown.
5. Do not use bullet points.
6. Do not use code blocks.
7. Do not add extra fields.
8. The sentiment must be exactly:
   Positive, Negative, or Neutral.
9. The complexity must be exactly:
   Beginner, Intermediate, or Advanced.
10. The summary must not exceed 60 words.
11. Extract between 3 and 6 meaningful keywords.
12. Use the exact field names shown in the output format.
"""


# ---------------------------------------------------------
# PROMPT BUILDER
# ---------------------------------------------------------

def build_analysis_prompt(user_text):
    """
    Build the complete prompt sent to the LLM.

    The prompt combines:

    - Few-shot examples
    - Output constraints
    - User input
    """

    prompt = f"""
{FEW_SHOT_EXAMPLES}

{OUTPUT_CONSTRAINTS}


NOW ANALYZE THE FOLLOWING TEXT:

Input:

{user_text}


Return the analysis using the exact required format.
"""

    return prompt