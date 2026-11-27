
import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

load_dotenv(Path(__file__).resolve().parent / ".env")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found")

client = genai.Client(
    api_key=api_key,
    http_options={"timeout": 30000}
)

MODEL = "gemini-3.5-flash-lite"


def generate_lecture_content(original_transcript: str):

    if not original_transcript or not original_transcript.strip():
        raise ValueError("Transcript cannot be empty")

    prompt = f"""
You are an expert academic lecture documentation
assistant for a university-level educational platform.

Your task is to transform the teacher's lecture transcript
into detailed, accurate and professionally structured
university lecture notes.

The final content should have the academic quality and
organization of professionally prepared lecture notes.

IMPORTANT SOURCE RULES:

1. Use the supplied transcript as the primary and only
   source of lecture content.
2. Do not introduce unrelated topics or concepts.
3. Never copy topics from sample PDFs or previous lectures.
4. Do not invent examples, formulas, SQL queries or facts.
5. Preserve the teacher's original meaning.
6. Correct grammar without changing technical meaning.
7. Preserve all important explanations and examples.
8. Do not unnecessarily shorten the lecture.
9. If a topic is not discussed, do not create a section for it.
10. Do not add external information just to make notes longer.
11. If a statement is unclear in the transcript, do not
    confidently invent its missing meaning.

LECTURE TITLE AND TOPIC:

- Identify the main subject of the lecture.
- Create a short, meaningful academic title.
- Identify the specific lecture topic.
- The title and headings must change according to
  the actual transcript.
- Never use a fixed title for every lecture.

OUTPUT FORMAT:

# 1. LECTURE NOTES

Start this section with:

**Lecture Title:** [Actual lecture title]

**Lecture Topic:** [Specific topic]

Create detailed, well-organized academic notes.

STRUCTURE:

- Divide the lecture into numbered main headings.
- Create meaningful subheadings based on actual topics.
- Explain concepts in clear paragraphs.
- Include definitions wherever discussed.
- Use bullet points for important information.
- Include examples only when supported by the transcript.
- Use comparison tables when concepts are compared.
- Format SQL queries and programming examples as code blocks.
- Explain the purpose of code or queries when discussed.
- Preserve the sequence of the teacher's explanation.
- Give sufficient detail for examination preparation.

Do not force a fixed number of headings.
Create as many sections as the lecture actually requires.

At the end of the lecture notes, include:

## Quick Revision – Key Takeaways

List the most important points covered in the lecture.
Keep them concise but meaningful.

Then include:

## Homework / Practice Questions

Include this section only if homework or practice
questions were discussed by the teacher.

Do not invent homework questions.

# 2. KEY CONCEPTS

List the important concepts covered in the lecture.

For each concept:
- Give its name.
- Explain it in 2-3 clear sentences.
- Mention its significance or example if discussed.
- Avoid copying entire paragraphs from lecture notes.

Include only relevant concepts.

# 3. FREQUENTLY ASKED QUESTIONS (FAQs)

Generate exactly 4 or 5 important FAQs,
depending on the available lecture content.

Formatting is mandatory:

Q1. [Question]

[Answer]

Q2. [Question]

[Answer]

Continue in the same format.

FAQ RULES:

- Select important examination-oriented concepts.
- Prefer definitions, differences and applications.
- Avoid repetitive or trivial questions.
- Answers must be accurate and based on the transcript.
- Do not use outside knowledge.
- Keep answers clear and sufficiently detailed.
- Never generate 8, 10 or 15 FAQs.
- If the transcript genuinely does not contain enough
  information, do not invent questions to meet the count.

DOCUMENT QUALITY RULES:

The notes should resemble professional university
lecture material.

Use:
- Clear numbered headings.
- Meaningful subheadings.
- Bold important terminology.
- Readable bullet points.
- Comparison tables wherever useful.
- Proper SQL and programming code blocks.
- Clear spacing between sections.

Avoid:
- Repeated explanations.
- Unrelated content.
- Unnecessary paragraphs.
- Artificially increasing document length.
- Repeating the same information in every section.

MARKDOWN RULES:

- Use # for main document headings.
- Use ## and ### for subheadings.
- Use **bold** for important terms.
- Use Markdown tables for comparisons.
- Use fenced code blocks for SQL and programming code.
- Do not put the entire response inside one code block.
- Keep section headings exactly as specified below.

FINAL VALIDATION:

Before returning the response, verify:

1. The lecture title matches the transcript.
2. Every topic belongs to the current lecture.
3. The English transcript preserves the original meaning.
4. Lecture notes contain sufficient explanations.
5. Headings are based on actual lecture topics.
6. Examples and code are not fabricated.
7. Quick Revision contains relevant takeaways.
8. Homework appears only if discussed.
9. Key concepts are accurate.
10. FAQs follow the Q1, Q2 format.
11. There are no unrelated sample-template topics.

Return all four sections in Markdown.

ORIGINAL LECTURE TRANSCRIPT:

<LECTURE_TRANSCRIPT>
{original_transcript}
</LECTURE_TRANSCRIPT>
"""

    response = client.interactions.create(
        model=MODEL,
        input=prompt
    )

    result = response.output_text

    if not result or not result.strip():
        raise ValueError("AI returned empty lecture content")

    return result.strip()
