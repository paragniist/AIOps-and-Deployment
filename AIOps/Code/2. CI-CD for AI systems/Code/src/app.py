import instructor  # type: ignore
from fastapi import FastAPI
import vertexai
import asyncio
import uvicorn
from vertexai.generative_models import GenerativeModel
from pydantic import BaseModel

vertexai.init(project="training-projects-430017", location="us-central1")

class UserData(BaseModel):
    query: str

class UserDetail(BaseModel):
    name: str
    age: int

client = instructor.from_vertexai(
    client=GenerativeModel("gemini-1.5-pro-preview-0409"),
    mode=instructor.Mode.VERTEXAI_TOOLS
)
app = FastAPI()

async def query_llm(prompt):
    return await client.chat.completions.create(
        response_model=UserDetail,
        messages=[
            {"role": "user", "content": f"Extract: '{prompt}'"},
        ],
    )

@app.post('/predict', response_model=UserDetail)
async def endpoint_function(data: UserData) -> UserDetail:
    user_detail = await query_llm(data.query)
    return user_detail


if __name__=="__main__":
    uvicorn.run(app,port=8080 , host='0.0.0.0')