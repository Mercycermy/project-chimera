# Skill: Generate Image

> **Version**: 1.0.0  
> **Status**: Active  
> **Category**: Creation

## Purpose
Creates high-fidelity visual assets using generative AI models, enforcing character consistency.

---

## MCP Tool Definition

```json
{
  "name": "generate_image",
  "description": "Generates images using AI models with character consistency enforcement.",
  "inputSchema": {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "properties": {
      "prompt": {
        "type": "string",
        "description": "Detailed visual description for generation"
      },
      "aspect_ratio": {
        "type": "string",
        "enum": ["1:1", "16:9", "9:16", "4:3"],
        "default": "1:1",
        "description": "Output image aspect ratio"
      },
      "character_reference_id": {
        "type": "string",
        "description": "REQUIRED: Consistency LoRA/Reference Image ID"
      },
      "negative_prompt": {
        "type": "string",
        "description": "Elements to exclude from generation"
      },
      "quality": {
        "type": "string",
        "enum": ["draft", "standard", "premium"],
        "default": "standard"
      }
    },
    "required": ["prompt", "character_reference_id"]
  }
}
```

---

## Input Contract

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `prompt` | string | Yes | Detailed visual description |
| `aspect_ratio` | string | No | e.g., `16:9`, `1:1` (default: `1:1`) |
| `character_reference_id` | string | **Yes** | **CRITICAL**: Consistency LoRA/Reference Image ID |
| `negative_prompt` | string | No | Elements to exclude |
| `quality` | string | No | `draft`, `standard`, `premium` |

---

## Output Contract

```json
{
  "image_url": "https://storage.googleapis.com/chimera-assets/gen_123.png",
  "seed": 49238423,
  "confidence_score": 0.95,
  "model_used": "midjourney-v6",
  "generation_time_ms": 12500,
  "request_id": "uuid-v4"
}
```

---

## Model Selection

| Model | Cost/Image | Quality | Speed | Use Case |
|-------|------------|---------|-------|----------|
| **Midjourney v6** | $0.05 | Highest | Slow | Hero content |
| **Ideogram** | $0.02 | High | Medium | Social posts |
| **SDXL** | $0.01 | Good | Fast | Draft/testing |

---

## Character Consistency Lock

> **CONSTRAINT**: The Agent Core MUST inject `character_reference_id` from GlobalState into every call.

The tool **WILL REJECT** requests missing this field to ensure visual brand consistency.

---

## Error Handling

| Code | Name | Description | Recovery |
|------|------|-------------|----------|
| `E001` | `MissingCharacterRef` | No character_reference_id | Fetch from GlobalState |
| `E002` | `ContentPolicyViolation` | Prompt violates safety | Log and reject |
| `E003` | `QuotaExceeded` | Daily generation limit | Alert operator |
| `E004` | `ModelUnavailable` | AI service down | Fallback to alternate model |
