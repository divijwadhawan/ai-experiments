import os
from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine

from dotenv import load_dotenv
load_dotenv()

# In the line below make sure a local PostgreSQL Database server is running locally generally port 5432
# Enter the user credentials in the string below
print(os.getenv("POSTGRE_STRING"))
engine = create_engine(os.getenv("POSTGRE_STRING"))
db = SQLDatabase(engine)


print(db.get_usable_table_names())
print(db.dialect)


from langchain.chains import create_sql_query_chain
from langchain_openai import AzureChatOpenAI

# You will need API Key from Azure Open AI
llm = AzureChatOpenAI(
    openai_api_key = os.getenv("OPENAI_API_KEY"), #Important to put API Key here TBD
    azure_endpoint = "https://genai-nexus.api.corpinter.net/apikey/",
    model_name = "gpt-4o",
   # azure_deployment = os.getenv("OPENAI_API_KEY"),
    openai_api_version = "2024-10-21",
    model_version = "2024-08-06",
    temperature = 0,
    max_retries = 3
)

#This is the key funtion that makes llm understand db
chain = create_sql_query_chain(llm,db)

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# This System below does something like templating

system = """Double check the user's {dialect} query for common mistakes, including:
- Only return SQL Query not anything else like ```sql ... ```
- Using NOT IN with NULL values
- Using UNION when UNION ALL should have been used
- Using BETWEEN for exclusive ranges
- Data type mismatch in predicates
- Using the correct number of arguments for functions
- Casting to the correct data type
- Using the proper columns for joins

If there are any of the above mistakes, rewrite the query.
If there are no mistakes, just reproduce the original query with no further commentary.

Output the final SQL query only."""

prompt = ChatPromptTemplate.from_messages(
    [("system", system), ("human", "{query}")]
).partial(dialect=db.dialect)
validation_chain = prompt | llm | StrOutputParser()

full_chain = {"query": chain} | validation_chain

response = full_chain.invoke({"question": "Which Products have most pending status"})
response

db.run(response)