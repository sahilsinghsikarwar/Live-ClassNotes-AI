
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ai_service import generate_lecture_content

router = APIRouter(
    prefix="/lectures",
    tags=["Lectures"]
)


class TranscriptRequest(BaseModel):
    original_transcript: str


@router.post("/generate-content")
async def generate_content(request: TranscriptRequest):

    if not request.original_transcript.strip():
        raise HTTPException(
            status_code=400,
            detail="Transcript cannot be empty"
        )

    try:
        result = generate_lecture_content(
            request.original_transcript
        )

        return {
            "status": "success",
            "original_transcript": request.original_transcript,
            "generated_content": result
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
