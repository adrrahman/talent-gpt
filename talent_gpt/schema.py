from pydantic import BaseModel


class Experience(BaseModel):
    title: str
    company: str
    start_date: str
    end_date: str
    location: str
    description: str


class Skill(BaseModel):
    name: str
    proficiency: str
