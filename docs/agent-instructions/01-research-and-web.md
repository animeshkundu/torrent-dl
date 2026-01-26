# 01: Research and Web Protocols

This document defines how AI agents must use research and internet resources when working on this repository.

---

## 🌐 Internet is First-Class

> **RESEARCH BEFORE IMPLEMENTATION**

The internet is not a fallback—it is a primary tool. AI agents MUST use web search to:
- Find current best practices
- Verify library versions and compatibility
- Discover security advisories
- Learn from existing implementations

### When to Research

| Situation | Research Action |
|-----------|-----------------|
| Adding a new library | Search for alternatives, security issues, compatibility |
| Implementing a pattern | Search for current best practices |
| Fixing a bug | Search for similar issues and solutions |
| API integration | Search for official documentation and examples |
| Security concerns | Search for CVEs and security advisories |

---

## ✅ Validation Protocol

### Library Validation

Before adding or updating any dependency:

```
1. Search: "[library name] security vulnerabilities 2024"
2. Search: "[library name] Python compatibility"
3. Search: "[library name] vs alternatives"
4. Check: PyPI for latest stable version
5. Check: GitHub issues for known problems
```

### Pattern Validation

Before implementing a coding pattern:

```
1. Search: "[pattern] Python best practices"
2. Search: "[pattern] common mistakes"
3. Search: "[pattern] [library] example"
4. Verify: Pattern is still recommended (not deprecated)
```

### API Validation

Before using any external API:

```
1. Find: Official documentation
2. Check: API version compatibility
3. Search: "[API] rate limits"
4. Search: "[API] error handling best practices"
```

---

## 🎯 Information Saturation

> **Research until you cannot find new relevant information**

### The Saturation Protocol

1. **Initial Search**: Broad query to understand the landscape
2. **Focused Search**: Narrow queries on specific aspects
3. **Cross-Reference**: Verify information from multiple sources
4. **Saturation Check**: When searches return information you've already seen

### Example Research Flow

Task: Implement a new caching mechanism

```
Search 1: "Python caching best practices 2024"
  → Learn about functools.lru_cache, redis, memcached

Search 2: "Python lru_cache vs redis when to use"
  → Understand tradeoffs

Search 3: "Python caching for torrent applications"
  → Find domain-specific patterns

Search 4: "Python redis security best practices"
  → Learn security considerations

Search 5: Similar results to previous → SATURATION REACHED
```

---

## 🚫 Anti-Hallucination Protocol

> **NEVER INVENT APIs, METHODS, OR PARAMETERS**

### When Uncertain

If you cannot verify something through research:

1. **State uncertainty explicitly**: "I could not verify if this API exists"
2. **Provide alternatives**: "Consider using [verified alternative]"
3. **Ask for clarification**: Request human verification
4. **Do NOT**: Invent plausible-sounding APIs

### Verification Checklist

Before using any API or method:

- [ ] I found this in official documentation
- [ ] I verified the version compatibility
- [ ] I checked the method signature
- [ ] I understand the return type

### Red Flags

⚠️ Warning signs that research is needed:
- "I think this method exists..."
- "This should work..."
- "I believe the API is..."

✅ Verified statements:
- "According to [source], this method..."
- "The official docs show..."
- "Version X.Y.Z introduced..."

---

## 📚 Source Hierarchy

When researching, prioritize sources in this order:

1. **Official Documentation**: Primary source of truth
2. **Official GitHub Repositories**: Issues, PRs, discussions
3. **Reputable Tech Blogs**: Real Python, official company blogs
4. **Stack Overflow**: Community-verified answers (check votes and dates)
5. **Personal Blogs**: Use with caution, cross-reference

### Evaluating Sources

| Quality Indicator | Trust Level |
|-------------------|-------------|
| Official docs | High |
| Dated within 2 years | Medium-High |
| Multiple upvotes/stars | Medium |
| Single source only | Low (cross-reference) |
| Outdated (>3 years) | Very Low |

---

## 🔒 Security Research

### Always Check

Before using any external code or library:

1. **CVE Database**: Search for known vulnerabilities
2. **GitHub Security**: Check repository security advisories
3. **Snyk/Dependabot**: Check for vulnerability reports
4. **Recent Activity**: Is the project maintained?

### Security Search Template

```
Search: "[library] CVE vulnerability"
Search: "[library] security advisory"
Search: "[library] site:github.com security"
Search: "[library] dependency vulnerability"
```

---

## 📝 Documenting Research

When research informs a decision:

1. **Reference Sources**: Include links in comments or docs
2. **Record Rationale**: Explain why you chose this approach
3. **Note Alternatives**: Document what was considered and rejected
4. **Timestamp**: Note when research was conducted (for future validation)

### Example Documentation

```python
# Using functools.lru_cache for in-memory caching
# Decision based on research (2024-01):
# - Official docs: https://docs.python.org/3/library/functools.html
# - Performance comparison: Real Python article showed 10x improvement
# - Alternatives considered: redis (overkill for single-process), 
#   cachetools (less standard library integration)
```

---

*Research is not optional. It is the foundation of quality engineering. Always research, always verify, never assume.*
