import pytest
from talent_gpt.extract.experience import extract_experience, NotFoundError
from talent_gpt.schema import Experience


def test_extract_experience_success():
    resume_content = """
    ## Experience
    Software Engineer ABC Corp 2020-01 2022-01
    - Developed software solutions
    - Collaborated with team members

    Data Scientist XYZ Inc 2018-06 2019-12
    - Analyzed data
    - Built machine learning models
    """
    experiences: list[Experience] = extract_experience(resume_content)

    assert len(experiences) == 2

    assert experiences[0].title == "Software Engineer"
    assert experiences[0].company == "ABC"
    assert experiences[0].start_date == "2020-01"
    assert experiences[0].end_date == "2022-01"

    assert experiences[1].title == "Data Scientist"
    assert experiences[1].company == "XYZ"
    assert experiences[1].start_date == "2018-06"
    assert experiences[1].end_date == "2019-12"


def test_extract_experience_not_found():
    resume_content = """
    ## Education
    Bachelor of Science in Computer Science
    """
    with pytest.raises(NotFoundError):
        extract_experience(resume_content)


def test_extract_experience_empty():
    resume_content = """
    ## Experience
    """
    experiences: list[Experience] = extract_experience(resume_content)
    assert len(experiences) == 0


def test_extract_experience_incomplete_block():
    resume_content = """
    ## Experience
    Software Engineer ABC Corp 2020-01
    """
    experiences: list[Experience] = extract_experience(resume_content)
    assert len(experiences) == 1

    assert experiences[0].title == "Software Engineer"
    assert experiences[0].company == "ABC"
    assert experiences[0].start_date == "2020-01"
    assert experiences[0].end_date == None
    assert experiences[0].description == ""
