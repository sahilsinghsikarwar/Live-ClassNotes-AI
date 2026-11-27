
from ai_service import generate_lecture_content

sample_transcript = """
Today we discussed artificial intelligence.
AI helps machines perform tasks that normally require human intelligence.
Machine learning is a subset of artificial intelligence.
It learns patterns from data and makes predictions.
"""

result = generate_lecture_content(sample_transcript)

print("\n===== GENERATED LECTURE CONTENT =====\n")
print(result)
