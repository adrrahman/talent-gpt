import os


from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import (
    JsonOutputParser,
)
from langchain_core.prompts import PromptTemplate
from langchain_openai import AzureChatOpenAI
from opik.integrations.langchain import OpikTracer
from talent_gpt.schema import Experience
from langchain.chains import LLMChain

load_dotenv()


def extract_experience(resume_content: str):
    opik_tracer = OpikTracer()
    llm = AzureChatOpenAI(
        model=os.getenv("AZURE_OPENAI_MODEL_NAME"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        temperature=0,
        # callbacks=[opik_tracer],
    )
    parser = JsonOutputParser(pydantic_object=Experience)

    prompt_template = """
    Extract the experience from the following resume content: \n\n{resume_content}
    with the following format \n\n{format_instructions}
    """

    prompt = PromptTemplate(
        template=prompt_template,
        input_variables={
            "resume_content",
        },
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )

    chain = prompt | llm | parser

    response = chain.invoke(
        {
            "question": "Extract the experience from the following resume content",
            "resume_content": resume_content,
        },
        config={"callbacks": [opik_tracer]},
    )
    return response


if __name__ == "__main__":
    path_file = "data/txt/CV 1.txt"
    data = TextLoader(path_file).load()
    extract_experience(data)
