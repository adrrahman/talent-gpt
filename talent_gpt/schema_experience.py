from pydantic import BaseModel

class Experience(BaseModel):
    title: str
    company: str
    start_date: str
    end_date: str
    location: str
    description: str

def extract_experience(resume_content):
    raise NotImplementedError("This function is not implemented yet.")
