"""
AI generation pipeline.

  1. Scrape — gather raw content for the topic in the time window
  2. Summarise — call Claude to produce a digest
  3. Render — return HTML + plain-text versions
"""

from __future__ import annotations

import logging
from datetime import datetime

import anthropic
from django.conf import settings

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """You are Paper Boy, an expert newsletter writer.
You receive a list of raw web excerpts on a topic and a time window, and you produce a
clean, well-structured newsletter digest. Use markdown for the content.
Be concise, accurate, and engaging. Do not invent facts not present in the sources."""

USER_TEMPLATE = """Topic: {topic}
Time window: {window_start} to {window_end}

Sources:
{sources}

Write a newsletter digest covering the most important developments within this time window.
Include a brief intro, bullet-point highlights, and a closing note."""


def scrape_sources(topic: str, window_start: datetime, window_end: datetime) -> list[dict]:
    """
    Placeholder scraper — replace with real search/scrape logic.
    Returns a list of dicts: [{title, url, excerpt}]
    """
    logger.info("Scraping sources for topic '%s'", topic)
    # TODO: integrate search API (e.g. SerpAPI, Brave Search) + httpx + BeautifulSoup
    return []


def build_digest(
    topic: str,
    window_start: datetime,
    window_end: datetime,
) -> tuple[str, str, list[dict]]:
    """
    Full pipeline: scrape → summarise → render.
    Returns (html, plain_text, sources).
    """
    sources = scrape_sources(topic, window_start, window_end)

    sources_text = "\n\n".join(
        f"[{i + 1}] {s['title']}\n{s['url']}\n{s['excerpt']}" for i, s in enumerate(sources)
    ) or "No sources found for this time window."

    client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)

    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=2048,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": USER_TEMPLATE.format(
                    topic=topic,
                    window_start=window_start.strftime("%Y-%m-%d %H:%M UTC"),
                    window_end=window_end.strftime("%Y-%m-%d %H:%M UTC"),
                    sources=sources_text,
                ),
            }
        ],
    )

    markdown_content = message.content[0].text
    html = _markdown_to_html(markdown_content)
    return html, markdown_content, sources


def _markdown_to_html(md: str) -> str:
    """Minimal markdown → HTML. Swap for a real library (e.g. mistune) as needed."""
    try:
        import mistune  # type: ignore

        return mistune.html(md)
    except ImportError:
        # Fallback: wrap in <pre> so the email is still readable
        escaped = md.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        return f"<pre style='font-family:sans-serif;white-space:pre-wrap'>{escaped}</pre>"
