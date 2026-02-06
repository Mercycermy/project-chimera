# Skill: Fetch Trends

> **Version**: 1.0.0  
> **Status**: Active  
> **Category**: Perception

## Purpose
Aggregates trending topics from social platforms and news sources to inform content strategy.

---

## MCP Tool Definition

```json
{
  "name": "fetch_trends",
  "description": "Fetches trending topics from social platforms and news sources.",
  "inputSchema": {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "properties": {
      "platform": {
        "type": "string",
        "enum": ["twitter", "tiktok", "google_news"],
        "description": "The source platform for trends"
      },
      "niche": {
        "type": "string",
        "description": "Specialized topic filter (e.g., crypto, fashion)"
      },
      "limit": {
        "type": "integer",
        "default": 10,
        "minimum": 1,
        "maximum": 50,
        "description": "Maximum results to return"
      }
    },
    "required": ["platform"]
  }
}
```

---

## Input Contract

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `platform` | string | Yes | The source platform (`twitter`, `tiktok`, `google_news`) |
| `niche` | string | No | Specialized topic filter (e.g., `crypto`, `fashion`) |
| `limit` | integer | No | Max results to return (default: 10, max: 50) |

---

## Output Contract

```json
{
  "trends": [
    {
      "topic": "Agentic AI",
      "volume": 15000,
      "sentiment": "positive",
      "summary": "Rising interest in autonomous coding agents."
    }
  ],
  "timestamp": "2026-02-05T12:00:00Z",
  "platform": "twitter",
  "request_id": "uuid-v4"
}
```

---

## Error Handling

| Code | Name | Description | Recovery |
|------|------|-------------|----------|
| `E001` | `InvalidPlatformError` | Unsupported platform specified | Check platform enum |
| `E002` | `RateLimitExceeded` | API rate limit hit | Retry after 60s |
| `E003` | `APIUnavailable` | Platform API down | Queue for later |
| `E004` | `AuthenticationFailed` | Invalid API credentials | Alert operator |

---

## Usage Examples

### Twitter Tech Trends
```json
{
  "platform": "twitter",
  "niche": "tech",
  "limit": 5
}
```

### TikTok Fashion Trends
```json
{
  "platform": "tiktok",
  "niche": "fashion",
  "limit": 20
}
```
