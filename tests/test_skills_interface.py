"""
Tests for the Skills Interface.
Validates all skills follow defined input/output contracts.
"""

from __future__ import annotations

import importlib
from typing import Literal

import pytest
from pydantic import BaseModel, Field


class FetchTrendsInput(BaseModel):
    platform: Literal["twitter", "tiktok", "google_news"]
    niche: str | None = None
    limit: int = Field(default=10, ge=1, le=50)


class GenerateImageInput(BaseModel):
    prompt: str
    aspect_ratio: Literal["1:1", "16:9", "9:16", "4:3"] = "1:1"
    character_reference_id: str
    negative_prompt: str | None = None
    quality: Literal["draft", "standard", "premium"] = "standard"


class PostContentInput(BaseModel):
    platform: Literal["twitter", "instagram", "threads"]
    text: str = Field(max_length=280)
    media_urls: list[str] | None = None
    confidence_score: float = Field(ge=0.70, le=1.0)
    disclosure_mode: Literal["automated", "human_assisted"]
    content_hash: str


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


def test_fetch_trends_accepts_valid_params():
    fetch_trends = _load_skill_function("skills.skill_fetch_trends", "fetch_trends")
    payload = FetchTrendsInput(platform="twitter", niche="tech", limit=5).model_dump()
    result = fetch_trends(payload)
    assert isinstance(result, dict)


def test_generate_image_accepts_valid_params():
    generate_image = _load_skill_function("skills.skill_generate_image", "generate_image")
    payload = GenerateImageInput(
        prompt="A clean studio portrait of an android in soft light.",
        character_reference_id="ref-1234",
        aspect_ratio="1:1",
        quality="standard",
    ).model_dump()
    result = generate_image(payload)
    assert isinstance(result, dict)


def test_post_content_accepts_valid_params():
    post_content = _load_skill_function("skills.skill_post_content", "post_content")
    payload = PostContentInput(
        platform="twitter",
        text="Hello from Chimera.",
        media_urls=["https://example.com/image.png"],
        confidence_score=0.95,
        disclosure_mode="automated",
        content_hash="b" * 64,
    ).model_dump()
    result = post_content(payload)
    assert isinstance(result, dict)


class TestSkillsInterface:
    """Ensure all skills have consistent interfaces."""

    def test_skill_has_execute_method(self):
        """All skills must have an 'execute' method."""
        # from skills.skill_fetch_trends import FetchTrendsSkill
        # skill = FetchTrendsSkill()
        # assert hasattr(skill, "execute")
        assert False, "Skill implementation not found"

    def test_skill_returns_dict(self):
        """All skills must return a dictionary result."""
        assert False, "Skill implementation not found"

    def test_skill_includes_metadata(self):
        """All skill results must include execution metadata."""
        expected_fields = ["execution_time", "skill_name", "success"]
        result = {}

        for field in expected_fields:
            assert field in result, f"Result must contain '{field}'"

    def test_generate_image_skill_contract(self):
        """Image generation skill must follow its contract."""
        assert False, "Image skill implementation not found"

    def test_post_content_skill_contract(self):
        """Post content skill must follow its contract."""
        assert False, "Post content skill implementation not found"
