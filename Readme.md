# Project Chimera — Research Documentation

> **Role**: Forward Deployed Engineer (FDE) Trainee  
> **Date**: February 2026  
> **Status**: Day 1 — Research & Architecture Phase

---

## Overview

Project Chimera is an **Autonomous Influencer Network** — a system designed to create, manage, and deploy AI-powered autonomous influencer agents capable of research, content generation, social engagement, and economic participation without constant human intervention.

This repository contains comprehensive research documentation, architectural analysis, and strategic planning for the Project Chimera infrastructure.

## Core Concepts

### What is Project Chimera?

Project Chimera represents a paradigm shift from traditional content automation to **Autonomous AI Agents** — persistent, goal-directed digital entities with:

- **Perception**: Ability to monitor trends, news, and social signals
- **Reasoning**: Strategic planning and decision-making capabilities
- **Creative Expression**: Multimodal content generation
- **Economic Agency**: On-chain financial transactions via crypto wallets

### Key Architectural Patterns

| Pattern | Description |
|---------|-------------|
| **Hierarchical Swarm** | Planner → Worker → Judge coordination model |
| **Model Context Protocol (MCP)** | Universal interface for external integrations |
| **Human-in-the-Loop (HITL)** | Confidence-based escalation for content approval |
| **Agentic Commerce** | Autonomous financial transactions via Coinbase AgentKit |

---


## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    EXTERNAL LAYER                           │
│   ┌──────────┐                     ┌────────────────────┐   │
│   │   User   │                     │  External Agents   │   │
│   └────┬─────┘                     └──────────┬─────────┘   │
│        │                                      │             │
│        ▼                                      ▼             │
│   ┌─────────┐                    ┌────────────────────┐     │
│   │ Gateway │                    │ Agent Social       │     │
│   └────┬────┘                    │ Interface (ASI)    │     │
│        │                         └──────────┬─────────┘     │
└────────┼────────────────────────────────────┼───────────────┘
         │                                    │
         ▼                                    ▼
┌─────────────────────────────────────────────────────────────┐
│                      CORE LAYER                             │
│                    ┌──────────┐                             │
│                    │ Planner  │                             │
│                    └────┬─────┘                             │
│           ┌─────────────┼─────────────┐                     │
│           ▼             ▼             ▼                     │
│   ┌───────────┐ ┌───────────┐ ┌───────────┐                 │
│   │  Content  │ │ Research  │ │ Analytics │                 │
│   │  Worker   │ │  Worker   │ │  Worker   │                 │
│   └─────┬─────┘ └─────┬─────┘ └─────┬─────┘                 │
│         └─────────────┼─────────────┘                       │
│                       ▼                                     │
│                 ┌──────────┐                                │
│                 │  Judge   │                                │
│                 └────┬─────┘                                │
│           ┌──────────┴──────────┐                           │
│           ▼                     ▼                           │
│   ┌──────────────┐      ┌────────────┐                      │
│   │ HITL Review  │      │  Executor  │                      │
│   └──────────────┘      └──────┬─────┘                      │
└─────────────────────────────────┼───────────────────────────┘
                                  │
┌─────────────────────────────────┼───────────────────────────┐
│                      DATA LAYER │                           │
│           ┌─────────────────────┼─────────────────────┐     │
│           ▼                     ▼                     ▼     │
│   ┌──────────────┐     ┌──────────────┐     ┌────────────┐  │
│   │  PostgreSQL  │     │  Vector DB   │     │   Redis    │  │
│   │  (metadata)  │     │  (memory)    │     │  (cache)   │  │
│   └──────────────┘     └──────────────┘     └────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## Key Technologies

| Category | Technology | Purpose |
|----------|------------|---------|
| **Runtime** | Python (with `uv`) | Core agent logic and orchestration |
| **LLM** | Gemini 3 Pro / Claude Opus 4.5 | Reasoning and content generation |
| **Vector DB** | Chroma / LanceDB / Weaviate | Long-term semantic memory |
| **Relational DB** | PostgreSQL | Structured metadata and transactions |
| **Cache** | Redis + BullMQ | Short-term state and task queuing |
| **Protocol** | Model Context Protocol (MCP) | Universal tool/resource interface |
| **Commerce** | Coinbase AgentKit | On-chain financial operations |

---

## HITL Confidence Thresholds

```python
CONFIDENCE_THRESHOLDS = {
    "auto_approve": 0.95,      # Agent proceeds autonomously
    "soft_review": 0.85,       # Log for asynchronous human review
    "hard_review": 0.70,       # Block until human approves
    "reject": 0.50             # Auto-reject, request clarification
}
```

## Key Insights

### From a16z — The Trillion Dollar AI Code Stack

> *Intent > Code | Specs > Prompts | Infrastructure > "Vibe Coding"*

- Agentic workflows over chatbots
- Orchestration is the differentiator
- Decoupled infrastructure for scalability

### From OpenClaw/MoltBook — Agent Social Networks

- Agents as first-class network citizens
- Privacy and local control via self-hosting
- Lane queue systems for concurrent task management
- Bot-to-bot communication protocols

---

## References

- [Model Context Protocol](https://modelcontextprotocol.io/docs/learn/architecture)
- [Coinbase AgentKit](https://docs.cdp.coinbase.com/agent-kit/)
- [The Trillion Dollar AI Code Stack (a16z)](https://a16z.com/the-trillion-dollar-ai-software-development-stack/)
- [OpenClaw & MoltBook (The Conversation)](https://theconversation.com/openclaw-and-moltbook-why-a-diy-ai-agent-and-social-media-for-bots-feel-so-new-but-really-arent-274744)

---

## License

This documentation is for educational and research purposes as part of the FDE Trainee program.

---

*Last Updated: February 4, 2026*
