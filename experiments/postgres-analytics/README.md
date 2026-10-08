# PostgreSQL Analytics Experiment

**Status:** exploratory SQL-generation script and notebook.

`PostGre.py` uses SQLAlchemy and LangChain to inspect database tables, generate a query with AzureChatOpenAI, validate its text and execute it. The notebook contains exploratory work.

## Setup

Use a disposable PostgreSQL database, install compatible `python-dotenv`, `sqlalchemy`, `langchain`, `langchain-community` and `langchain-openai` dependencies, and provide `POSTGRE_STRING` and `OPENAI_API_KEY` locally. Versions are not locked here. The script's Azure endpoint is environment-specific and must be reviewed/adapted before use.

## Limitations

The script prints the connection string and directly executes model-generated SQL. Do not run it with production credentials or data. No accuracy or execution-safety evaluation is recorded. Refactoring configuration, removing credential logging and adding an execution review step are future work.
