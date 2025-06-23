from langchain import OpenAI, LLMChain, PromptTemplate

llm = OpenAI()

prompt = PromptTemplate(
    input_variables=["instruction"],
    template="""
    You are an Agentic AI Web Developer.
    Follow this instruction step-by-step, plan the tasks,
    generate code snippets, and prepare for deployment.

    Instruction: {instruction}
    """,
)

chain = LLMChain(llm=llm, prompt=prompt)

def run_agent(instruction):
    response = chain.run(instruction)
    return response
