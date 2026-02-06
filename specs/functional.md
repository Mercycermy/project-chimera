# Functional Specification — Project Chimera

> **Source**: SRS Section 4 (Functional Requirements)

---

## 1. Cognitive Core (Persona)

| ID | Actor | User Story | Acceptance Criteria |
|----|-------|------------|---------------------|
| **FR-1.0** | Agent | As an agent, I need to instantiate my personality from a `SOUL.md` file so that I maintain a consistent character. | - Parses YAML frontmatter (Voice, Values)<br>- Injects "Backstory" into system prompt |
| **FR-1.1** | Agent | As an agent, I need to retrieve past memories before acting so that I don't repeat myself or hallucinate. | - Fetches episodic memory (Redis, last 1h)<br>- Queries semantic memory (Weaviate) for relevant history |
| **FR-1.2** | Judge | As a Judge, I need to summarize high-engagement interactions so that the agent "learns" and evolves. | - Writes successful interactions to Weaviate long-term memory |

---

## 2. Perception System (Data Ingestion)

| ID | Actor | User Story | Acceptance Criteria |
|----|-------|------------|---------------------|
| **FR-2.0** | Planner | As a Planner, I need to poll MCP Resources (e.g., `twitter://mentions`) so that I can react to the world. | - Connects to configured MCP servers via Stdio/SSE<br>- Polls at defined intervals |
| **FR-2.1** | Planner | As a Planner, I need to filter incoming data using a "Relevance Score" so that I don't get distracted by noise. | - Passes content through lightweight LLM filter<br>- Only creates Tasks for items with score > 0.75 |
| **FR-2.2** | Worker | As a Trend Spotter, I need to analyze `news://` resources to detect emerging topics. | - Clusters news items<br>- Alerts Planner if a cluster exceeds threshold |

---

## 3. Creative Engine (Content Generation)

| ID | Actor | User Story | Acceptance Criteria |
|----|-------|------------|---------------------|
| **FR-3.0** | Worker | As a Worker, I need to use MCP Tools to generate media so that I am not limited to text. | - Calls `mcp-server-midjourney` for images<br>- Calls `mcp-server-runway` for video |
| **FR-3.1** | System | As the System, I must enforce a "Character Consistency Lock" on all image generation. | - Injects `character_reference_id` or LoRA into every image tool call |
| **FR-3.2** | Planner | As a Planner, I need to choose between "Tier 1" (Image-to-Video) and "Tier 2" (Full Video) generation based on budget. | - Checks available daily budget before selecting high-cost tools |

---

## 4. Action System (Social Interface)

| ID | Actor | User Story | Acceptance Criteria |
|----|-------|------------|---------------------|
| **FR-4.0** | Worker | As a Worker, I need to publish content via MCP Tools (e.g., `twitter.post_tweet`) so that implementation details are abstracted. | - No direct HTTP calls<br> - All posts go through `post_content` tool<br>- Human approval required before publishing |
| **FR-4.1** | System | As the System, I need to support a full "Ingest-Plan-Generate-Act-Verify" loop for replies. | - End-to-end latency < 10s for high priority<br>- Judge verifies before `Act` step |

---

## 5. Agentic Commerce

| ID | Actor | User Story | Acceptance Criteria |
|----|-------|------------|---------------------|
| **FR-5.0** | Agent | As an Agent, I need a non-custodial crypto wallet to hold assets. | - Wallet initialized via Coinbase AgentKit<br>- Private keys in secure env vars |
| **FR-5.1** | Worker | As a Worker, I need to execute `native_transfer` or `deploy_token` actions on-chain. | - Can send ETH/USDC via MCP Tool |
| **FR-5.2** | CFO Judge | As a "CFO", I need to review every transaction against a daily budget limit. | - Rejects any tx > Daily Limit ($50 example)<br>- Rejects suspicious patterns |

---

## 6. Swarm Governance (Orchestrator)

| ID | Actor | User Story | Acceptance Criteria |
|----|-------|------------|---------------------|
| **FR-6.0** | Planner | As a Planner, I need to decompose goals into atomic Tasks in a Queue. | - Pushes JSON tasks to Redis `task_queue` |
| **FR-6.1** | Judge | As a Judge, I need to use Optimistic Concurrency Control (OCC) when committing results. | - Checks `state_version` before write<br>- Fails/Retries if state has drifted |

---

## 7. HITL Governance

| ID | Actor | User Story | Acceptance Criteria |
|----|-------|------------|---------------------|
| **FR-7.0** | HITL Reviewer | As a reviewer, I need a dashboard showing pending content for approval so that I can manage the review queue. | - Displays content with confidence scores<br>- Shows original task context |
| **FR-7.1** | HITL Reviewer | As a reviewer, I need to approve, reject, or request edits on content so that quality is maintained. | - One-click approve/reject<br>- Edit suggestions returned to Worker |
| **FR-7.2** | System | As the System, I need to escalate content below 0.70 confidence automatically so that high-risk content is always reviewed. | - Auto-routes to HITL queue<br>- Blocks publication until approved<br>- Publishing always requires human approval regardless of confidence |
| **FR-7.3** | Network Operator | As an operator, I need override controls for emergency content takedown so that harmful content can be removed immediately. | - Emergency stop button<br>- Audit log of all overrides |

---

## 8. Memory Management

| ID | Actor | User Story | Acceptance Criteria |
|----|-------|------------|---------------------|
| **FR-8.0** | Agent | As an agent, I need short-term memory (Redis) for recent context so that I maintain coherence within conversations. | - 1-hour TTL for episodic memory<br>- Automatic cleanup |
| **FR-8.1** | Agent | As an agent, I need long-term memory (Weaviate) for learned patterns so that I evolve over time. | - Vector embeddings stored per agent<br>- Semantic search capability |
| **FR-8.2** | Judge | As a Judge, I need to mark high-performing content for memory consolidation so that successful patterns are retained. | - Engagement threshold triggers consolidation<br>- Creates summary embeddings |
| **FR-8.3** | Planner | As a Planner, I need to query past memories before task creation so that I avoid repetitive content. | - Similarity check against last 30 days<br>- Blocks duplicates above 0.85 similarity |
