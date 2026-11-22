#!/usr/bin/env python3
"""AI社員チームの構造を検証する。

使い方: python3 scripts/check_team.py
問題がなければ "OK: all checks passed" を出して終了コード0。
問題があれば "NG: <理由>" を1行ずつ出して終了コード1。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

AGENTS = [
    "00-progress-manager", "01-market-research", "02-competitor-research",
    "03-post-collection", "04-trend-research", "05-audience-analysis",
    "06-theme-selection", "07-planning", "08-structure-design",
    "09-hook-writer", "10-script-writer", "11-title-writer", "12-cta-design",
    "13-script-review", "14-fact-check", "15-expression-check",
    "16-material-collection", "17-image-generation", "18-diagram-design",
    "19-subtitle-writer", "20-video-editing", "21-audio-adjustment",
    "22-quality-check", "23-post-management", "24-caption-writer",
    "25-comment-analysis", "26-metrics-analysis", "27-improvement-proposal",
]
AGENT_HEADINGS = [
    "## 目的", "## 入力情報", "## 作業手順", "## 出力形式",
    "## 完了条件", "## 引き継ぎ事項", "## やらないこと", "## 参照ルール",
]
RULES = [
    "brand.md", "tone.md", "ng-expressions.md", "ng-planning.md",
    "evidence.md", "metrics.md", "approval.md", "CHANGELOG.md",
]
SKILLS = ["reel-production", "idea-generation", "planning-meeting", "rule-update"]
REEL_REQUIRED = [
    "★承認1", "★承認2", "★承認3", "不足情報",
    "承認なしで次の工程に進まない", "要確認",
    "『次へ』『OK』だけでは承認とみなさない",
]
TEMPLATES = [
    "handoff.md", "script.md", "canva-brief.md", "caption.md",
    "analysis.md", "idea.md", "meeting.md",
]
OTHER_FILES = ["CLAUDE.md", "ideas/backlog.md", "projects/README.md", "meetings/README.md"]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def frontmatter(text: str) -> dict:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    return out


def section_body(text: str, heading: str) -> str:
    m = re.search(re.escape(heading) + r"\n(.*?)(?=\n## |\Z)", text, re.S)
    return m.group(1).strip() if m else ""


def check_agents() -> list:
    errs = []
    d = ROOT / ".claude" / "agents"
    found = sorted(p.stem for p in d.glob("*.md")) if d.exists() else []
    for name in AGENTS:
        if name not in found:
            errs.append(f"agent missing: {name}.md")
    for extra in set(found) - set(AGENTS):
        errs.append(f"unexpected agent file: {extra}.md")
    for name in AGENTS:
        p = d / f"{name}.md"
        if not p.exists():
            continue
        text = read(p)
        fm = frontmatter(text)
        slug = name.split("-", 1)[1]
        if fm.get("name") != slug:
            errs.append(f"{name}: frontmatter name must be '{slug}'")
        if not fm.get("description"):
            errs.append(f"{name}: frontmatter description missing")
        for h in AGENT_HEADINGS:
            if h not in text:
                errs.append(f"{name}: heading missing '{h}'")
        if "## やらないこと" in text and not section_body(text, "## やらないこと"):
            errs.append(f"{name}: 'やらないこと' is empty")
    for name in AGENTS:
        p = d / f"{name}.md"
        if p.exists() and "templates/handoff.md" not in section_body(read(p), "## 出力形式"):
            errs.append(f"{name}: 出力形式 must require templates/handoff.md")
    qc = d / "22-quality-check.md"
    if qc.exists():
        body = section_body(read(qc), "## 入力情報")
        for w in ("00", "24"):
            if w not in body:
                errs.append(f"22-quality-check: 入力情報 must include {w}")
    fc = d / "14-fact-check.md"
    if fc.exists():
        t = read(fc)
        for w in ("不明", "要確認"):
            if w not in t:
                errs.append(f"14-fact-check: must mention '{w}'")
    return errs


def check_rules() -> list:
    errs = []
    d = ROOT / "rules"
    for r in RULES:
        if not (d / r).exists():
            errs.append(f"rule missing: rules/{r}")
    ng = d / "ng-expressions.md"
    if ng.exists():
        t = read(ng)
        for w in ("10,000人", "治る"):
            if w not in t:
                errs.append(f"ng-expressions.md: must contain '{w}'")
    cl = d / "CHANGELOG.md"
    if cl.exists() and "| 日付 | 内容 | 理由 |" not in read(cl):
        errs.append("CHANGELOG.md: header '| 日付 | 内容 | 理由 |' missing")
    return errs


def check_skills() -> list:
    errs = []
    for s in SKILLS:
        p = ROOT / ".claude" / "skills" / s / "SKILL.md"
        if not p.exists():
            errs.append(f"skill missing: {s}/SKILL.md")
            continue
        text = read(p)
        fm = frontmatter(text)
        if fm.get("name") != s:
            errs.append(f"skill {s}: frontmatter name must be '{s}'")
        if not fm.get("description"):
            errs.append(f"skill {s}: frontmatter description missing")
        if s == "rule-update":
            for w in ("Grep", "CLAUDE.md", "templates"):
                if w not in text:
                    errs.append(f"rule-update: must search copies ('{w}')")
        if s == "reel-production":
            for w in REEL_REQUIRED:
                if w not in text:
                    errs.append(f"reel-production: must contain '{w}'")
    return errs


def check_files() -> list:
    errs = []
    for t in TEMPLATES:
        if not (ROOT / "templates" / t).exists():
            errs.append(f"template missing: templates/{t}")
    for f in OTHER_FILES:
        if not (ROOT / f).exists():
            errs.append(f"file missing: {f}")
    return errs


def main() -> int:
    errs = check_agents() + check_rules() + check_skills() + check_files()
    if errs:
        for e in errs:
            print(f"NG: {e}")
        return 1
    print("OK: all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
