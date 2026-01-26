# Architecture Decision Records (ADRs)

This directory contains Architecture Decision Records for the torrent-dl project.

## Purpose

ADRs capture important architectural decisions made during the development of this project. Each ADR describes:
- The context and problem being addressed
- The decision made and its rationale
- The consequences (positive and negative) of the decision

## Why ADRs Matter

- **Historical Context**: Understand why decisions were made
- **Knowledge Transfer**: New team members can quickly understand past decisions
- **Prevent Regression**: Avoid revisiting solved problems
- **AI Agent Guidance**: AI agents MUST check this directory before proposing architectural changes

## Naming Convention

ADRs are numbered sequentially: `NNNN-title-of-decision.md`

- `0000-template.md` - Template for new ADRs
- `0001-use-libtorrent.md` - First actual ADR (example)

## Creating a New ADR

1. Copy `0000-template.md` to a new file with the next number
2. Fill in all sections
3. Get the ADR reviewed before implementation
4. Update status as the decision evolves

## For AI Agents

**Before proposing any architectural change:**
1. Read all existing ADRs in this directory
2. Check if a similar decision has been made
3. If proposing a new approach, create a new ADR first
4. Reference relevant ADRs in your implementation
