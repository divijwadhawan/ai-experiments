# AI Experiments

A collection of exploratory database/AI work and agent bootstrap scaffolds. Each folder records its purpose, configuration and implementation status.

**Status:** experiments and templates; this is not a working multi-agent platform.

## Experiment index
| Folder | Scope | Status |
| --- | --- | --- |
| [PostgreSQL analytics](experiments/postgres-analytics/README.md) | LangChain-assisted SQL generation and execution | Experimental script and notebook |
| [Agent bootstrap](experiments/agent-bootstrap/README.md) | Container/configuration scaffold | Entry point only loads environment variables |
| [Chatbot template](templates/chatbot-bootstrap/README.md) | Generated agent template example | Scaffold, no implemented chatbot workflow |

## Architecture and stack
Python, SQLAlchemy, LangChain/AzureChatOpenAI in the analytics experiment, and Docker/configuration scaffolds for agent templates. Dependencies are experiment-specific.

## Quick start
Read the relevant experiment README before running it. Agent template generation is available through `scripts/create-agent.py`; it downloads an external Cookiecutter template and requires the `cookiecutter` package. Review generated code before executing it.

## Project scope and attribution
The bootstrap examples are generated/adapted templates, not implemented agents. The generator references [Yugen-ai/canso-ai-agent-templates](https://github.com/Yugen-ai/canso-ai-agent-templates). Preserve upstream attribution and check its licence before redistributing template-derived work.

## Validation and limitations
No experiments were executed against databases or external model services during restructuring. The PostgreSQL script uses environment-specific configuration and directly executes generated SQL. Use only a disposable database and appropriately restricted credentials while evaluating it.

Tracked local environment files and notebook checkpoints have been removed from the current tree. Their historical copies may remain; any real credentials previously committed must be rotated.

## Documentation and license
[Architecture](docs/architecture.md) · [Setup](docs/setup.md)

No root licence file is currently provided. Refer to upstream licences for template-derived content.
