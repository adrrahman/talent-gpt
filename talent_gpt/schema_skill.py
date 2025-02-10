from pydantic import BaseModel

class Skill(BaseModel):
    name: str
    proficiency: str


def extract_skill(resume_content):
    raise NotImplementedError("This function is not implemented yet.")
