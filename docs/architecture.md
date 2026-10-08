# Architecture

The repository contains independent experiments, not a single deployable service. `experiments/postgres-analytics` combines a PostgreSQL connection with a LangChain SQL-generation and validation chain. The agent bootstrap and chatbot template contain configuration/Docker assets but their entry points only call `load_dotenv()`.

`scripts/create-agent.py` invokes Cookiecutter against an external template repository. `dashboard-agents` is an empty placeholder retained from the original repository.
