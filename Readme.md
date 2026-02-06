# Project Chimera

Autonomous Influencer Network: a spec-driven system for AI agents that perceive trends, generate content, and act through MCP tools with human-in-the-loop governance.

## Status

Research and contract-first phase. Tests are intentionally failing until skill implementations match their defined contracts.

## Core Architecture

- Hierarchical Swarm: Planner -> Worker -> Judge
- MCP-only external interactions
- HITL enforcement for public-facing content
- Spec-driven development with JSON Schema contracts

## Project Layout

- Specs and contracts: [specs/_meta.md](specs/_meta.md), [specs/functional.md](specs/functional.md), [specs/technical.md](specs/technical.md)
- Skill definitions: [skills/README.md](skills/README.md) and per-skill README files
- Research notes: [research/architecture_strategy.md](research/architecture_strategy.md)
- Tests: [tests](tests)

## Quick Start (uv)

Prerequisites: Python 3.11+, [uv](https://github.com/astral-sh/uv)

```bash
uv pip install --system fastapi "pydantic>=2.0" "pytest>=9.0.2" redis black flake8
pytest -q
```

## Make Targets

```bash
make setup
make test
make test-cov
make lint
make spec-check
```

## Docker

```bash
docker build -t project-chimera:latest .
docker run --rm project-chimera:latest
```

## Testing Notes

- Contract tests are defined for skills and must pass before a skill is considered active.
- Tests currently fail if skill entry points or contract-compliant outputs are missing.

## References

- [Model Context Protocol](https://modelcontextprotocol.io/docs/learn/architecture)
- [Coinbase AgentKit](https://docs.cdp.coinbase.com/agent-kit/)
- [The Trillion Dollar AI Code Stack (a16z)](https://a16z.com/the-trillion-dollar-ai-software-development-stack/)
- [OpenClaw & MoltBook (The Conversation)](https://theconversation.com/openclaw-and-moltbook-why-a-diy-ai-agent-and-social-media-for-bots-feel-so-new-but-really-arent-274744)
