from __future__ import annotations

import importlib
from datetime import datetime
from typing import Literal
from uuid import UUID

import pytest
from pydantic import BaseModel


class TrendItem(BaseModel):
    topic: str
    volume: int
    sentiment: str
    summary: str


class TrendResponse(BaseModel):
    trends: list[TrendItem]
    timestamp: datetime
    platform: Literal["twitter", "tiktok", "google_news"]
    request_id: UUID


def _load_skill_function(module_name: str, func_name: str):
    try:
        module = importlib.import_module(module_name)
    except ModuleNotFoundError as exc:
        pytest.fail(
            f"Missing module '{module_name}'. Implement the skill to satisfy the spec.",
            pytrace=False,
        )
        raise exc

    func = getattr(module, func_name, None)
    if func is None:
        pytest.fail(
            f"Missing function '{func_name}' in '{module_name}'. Implement the skill to satisfy the spec.",
            pytrace=False,
        )
    return func


def test_fetch_trends_returns_contract():
    fetch_trends = _load_skill_function("skills.skill_fetch_trends", "fetch_trends")
    payload = {"platform": "twitter", "niche": "tech", "limit": 5}
    result = fetch_trends(payload)

    assert isinstance(result, dict)
    TrendResponse.model_validate(result)
