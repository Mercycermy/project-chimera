# Project Chimera — Meta Specification

> **Version**: 1.0  
> **Status**: Draft  
> **Source**: SRS 1.0 (`file1.md`)

---

## 1. Vision
Project Chimera transitions AiQEM from automated content scheduling to an **Autonomous Influencer Network**. We are building a fleet of "Chimeras" — sovereign digital entities capable of perception, reasoning, creative expression, and economic agency.

Unlike static bots, these agents:
- **Think** before acting (Planner-Worker-Judge architecture).
- **Own** their resources (Non-custodial crypto wallets).
- **Evolve** over time (Long-term semantic memory).

---

## 2. Core Objectives
1.  **Autonomous Operation**: Enable a "Single-Orchestrator Model" where one human manages thousands of agents via "Management by Exception."
2.  **Universal Connectivity**: Use **Model Context Protocol (MCP)** as the standard interface for all external interactions (Social, News, Crypto).
3.  **Economic Agency**: Grant agents the ability to earn, spend, and manage assets on-chain via **Agentic Commerce**.

---

## 3. Constraints

### Technical Constraints
*   **Architecture**: MUST use the **FastRender Swarm Pattern** (Planner → Worker → Judge).
*   **Integration**: Direct API calls from agent core logic are **PROHIBITED**. All I/O must go through MCP Tools/Resources.
*   **Concurrency**: State updates must use **Optimistic Concurrency Control (OCC)** to prevent race conditions.
*   **Protocol**: All MCP tool definitions must include JSON Schema validation (`$schema` reference).

### Safety Constraints
*   **HITL Mandatory**: Human-in-the-Loop review required for actions with confidence < 0.70.
*   **Transparency**: All external content must be labeled as AI-generated where platform features allow. No "none" disclosure mode.
*   **Wallet Security**: Financial transactions require CFO Judge approval and daily budget limits.

### Timeline Constraints
*   **Phase 1 (MVP)**: Core swarm architecture + 3 skills operational
*   **Phase 2**: Full MCP server integration + HITL dashboard
*   **Phase 3**: OpenClaw network integration + Agentic Commerce

### Resource Constraints
*   **Compute**: Kubernetes cluster with auto-scaling (min 3 pods, max 50)
*   **Budget**: Daily transaction limit per agent ($50 default)
*   **API Costs**: Image generation capped at 100 requests/day/agent

---

## 4. Out of Scope

The following are explicitly **NOT** part of Project Chimera v1.0:

*   **Multi-Model Orchestration**: Single LLM provider per deployment (no ensemble models)
*   **Cross-Chain Transactions**: Base/Ethereum only; no bridge operations
*   **Real-Time Video Streaming**: Pre-rendered content only; no live streaming
*   **Language Localization**: English-only for MVP
*   **Self-Replicating Agents**: Agents cannot spawn new agents autonomously

---

## 5. Success Criteria

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| **Agent Uptime** | > 99.5% | Prometheus monitoring |
| **Content Approval Rate** | > 85% first-pass HITL approval | Dashboard analytics |
| **Response Latency** | < 10s for high-priority tasks | P95 latency tracking |
| **Cost Efficiency** | < $0.50 per published content | Budget tracking system |
| **Character Consistency** | > 90% visual similarity score | LoRA validation checks |

---

## 6. Key Definitions
*   **Chimera Agent**: A sovereign digital entity with a unique persona (SOUL.md) and wallet.
*   **MCP**: Standard protocol for connecting AI models to tools and resources.
*   **Swarm**: The internal coordination of Planner, Worker, and Judge roles.
*   **Agentic Commerce**: Autonomous on-chain financial capability.