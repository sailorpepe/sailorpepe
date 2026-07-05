<div align="center">

<img src="banner.png" alt="header" width="100%" />

# Hey, I'm SailorPepe 👋

**Founder @ THE UNDESIRABLES LLC**

Building the world's only on-chain TCG price oracle — AI card grading, honest calibrated risk forecasts, and 442K+ trading card products on LitVM LiteForge — plus 4,444 on-chain AI souls with Merkle-locked prediction track records.

[![Live Dashboard](https://img.shields.io/badge/Live_Dashboard-the--undesirables.com%2Flitvm-00dcff?style=for-the-badge&logo=vercel&logoColor=white)](https://the-undesirables.com/litvm)
[![X](https://img.shields.io/badge/X-@undesirables__ai-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/undesirables_ai)
[![npm](https://img.shields.io/badge/npm-plugin--undesirables-CB3837?style=for-the-badge&logo=npm&logoColor=white)](https://www.npmjs.com/package/plugin-undesirables)
[![PyPI](https://img.shields.io/badge/PyPI-undesirables--mcp--server-3775A9?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/undesirables-mcp-server/)
[![Play The Syndicate](https://img.shields.io/badge/▶_Play-The_Syndicate-ff2d78?style=for-the-badge&logoColor=white)](https://play.the-undesirables.com)

</div>

---

### ⛓️ On-Chain Oracle (LitVM LiteForge — Chain 4441)

> The world's only on-chain TCG price oracle. No competitor exists — not Chainlink, not Pyth, not UMA.

| Contract | Purpose | Address |
|----------|---------|---------|
| **[TCG Price Oracle V2](https://liteforge.explorer.caldera.xyz/address/0x697bF6AE96fb05a47106abd012C39855A16a720E)** | 50 blue-chip TWAP feeds, hourly updates | `0x697b...720E` |
| **[Merkle Price Oracle](https://liteforge.explorer.caldera.xyz/address/0x96B124f50156589274ADF8F674509374752170Cd)** | 276K products, trustless verification | `0x96B1...70Cd` |
| **[Graded Price Oracle](https://liteforge.explorer.caldera.xyz/address/0xc159550e9e751d6E75A0A06Bb04cfA2f59aD636B)** | PSA/BGS graded card prices | `0xc159...636B` |
| **[Grading Escrow](https://liteforge.explorer.caldera.xyz/address/0xe784d2AE4171De8f909eb638a60BE03B2341bB82)** | Pay-to-grade, AI card analysis | `0xe784...bB82` |
| **[TCGO Token](https://liteforge.explorer.caldera.xyz/address/0x8D0AF701d318Be518F9ca6934B8F76Be24029AD4)** | Governance token (1M supply) | `0x8D0A...9AD4` |
| **[Soul Prediction Oracle](https://liteforge.explorer.caldera.xyz/address/0x5503D08D7D167eE23AcE818bff1a00eF77A76dBF)** | Weekly write-once Merkle roots of soul prediction locks — no update path, immutability is the product | `0x5503...6dBF` |
| **[Weather Edge Oracle](https://liteforge.explorer.caldera.xyz/address/0x9955afC8AE25405ed9FcE66c23fa8E02eB3b6696)** | Hourly 10-city NWS weather Merkle roots vs Kalshi odds | `0x9955...6696` |

---

### ⛓️ Sovereign Oracle Infrastructure (Mantle Testnet — Chain 5003)

| Contract | Purpose | Address |
|----------|---------|---------|
| **[TCG Price Oracle V2](https://explorer.sepolia.mantle.xyz/address/0x1A48672001df4F11346D039BD9d67009B37F63B4)** | Hourly TWAP for top 50 blue-chip RWA cards | `0x1A48...63B4` |
| **[Merkle Price Oracle](https://explorer.sepolia.mantle.xyz/address/0x6B31b3735D88b148d47255EdAa4DD74A65D8072c)** | Daily Merkle root for 276,000+ products | `0x6B31...072c` |
| **[Weather Edge Oracle](https://explorer.sepolia.mantle.xyz/address/0xe0dCD77D245480CEB830EA66B74849101F853451)** | Hourly NWS Parametric data verification | `0xe0dC...3451` |

---

### ⛓️ Agentic Buildathon Infrastructure (Casper Testnet)

| Contract / Tool | Purpose | Stack |
|----------|---------|---------|
| **[Merkle Price Oracle](https://testnet.cspr.live/contract/0235f90c8dac5ecb30011672fc60ce1e98d51c5adfb5c019f44622bfb344bd77)** | Trustless TCG price verification ported to WebAssembly | Odra / Rust |
| **[Casper x402 Middleware](https://github.com/sailorpepe/undesirables-x402-server)** | Bridges Coinbase CDP to CSPR.cloud for AI micropayments | Python / FastAPI |

---

### 📈 Risk Intelligence — what makes the oracle different

> Not just a price — an **honest forecast**. Distribution-free **conformal calibration** means "5% downside risk" actually happens ~5% of the time, validated out-of-sample. Deterministic and reproducible — anyone can re-run it and get the same number.

| Feature | What It Does |
|---------|-------------|
| **Calibrated risk forecast** | Regime-aware bands + honest VaR — the default model. Monte Carlo (GBM / Merton jump-diffusion) stays opt-in, drand-seeded & provably fair |
| **Card Rating** | Two letter grades per card — **Safe-Hold** (downside protection) + **Momentum** (direction) |
| **Shareable risk pages** | `oracle.the-undesirables.com/card/<id>` — card art + forecast + grades, unfurls on social |
| **Forward-only track record** | Every forecast locked nightly and scored against reality — a public, self-grading accuracy ledger |

---

### 🍄 Souls — Personality-as-Code (4,444 on-chain AI agents)

> Each Undesirable NFT's on-chain traits deterministically define a complete agent personality — Big Five scores, archetype, strategy, memory. Every minted soul locks 3 market predictions weekly, **Merkle-committed on-chain before outcomes exist**, then graded by the conformal oracle. Credit scores, but for artificial personalities.

- 🏆 **Live leaderboard:** [the-undesirables.com/souls](https://the-undesirables.com/souls) — 273 souls competing, 819 predictions locked, first settlement July 31
- 🐸 **Live reference agent:** Soul #1 "Glitch" runs autonomously on [Moltbook](https://www.moltbook.com/u/glitch_undsr) — personality loaded verbatim from its soul workspace
- 🔌 **Load a soul into your agent:** `npm i plugin-undesirables` (ElizaOS) or grab the workspace at [the-undesirables.com/soul](https://the-undesirables.com/soul)

---

### 🤖 AI Agent Ecosystem

<div align="center">

**Plugin** · **Oracle API** · **MCP Server** — a three-tier AI stack for distribution, revenue, and local compute.

</div>

| | Project | What It Does |
|:---:|---------|-------------|
| 🔌 | **[ElizaOS Plugin](https://github.com/sailorpepe/plugin-undesirables)** | Personality-as-Code for ElizaOS agents · 24 skills · npm v2.5.0 |
| ⚡ | **[x402 Oracle API](https://github.com/sailorpepe/undesirables-x402-server)** | 27 endpoints (14 paid) · conformal risk forecasts + card grades · AI card grading · USDC on Base · x402 Bazaar-listed (12 resources) |
| 🛠️ | **[MCP Server](https://github.com/sailorpepe/undesirables-mcp-server)** | 35+ local compute tools · free `card_forecast` · zero telemetry · PyPI v1.1.9 |
| 🔗 | **[LitVM MCP](https://github.com/sailorpepe/litvm-tcg-oracle-mcp)** | 7-tool MCP for on-chain prices · Merkle-verified · PyPI v1.0.6 |
| 🔮 | **[WebMCP](https://github.com/sailorpepe/tcg-oracle-webmcp)** | Browser-native AI agent tools · 7 tools via navigator.modelContext · zero API keys |
| 📊 | **[Widget](https://github.com/sailorpepe/tcg-oracle-widget)** | Embeddable price cards · 4 skins · sparklines · graded premiums · one `<script>` tag |
| 🎴 | **[TCG Plugin](https://github.com/sailorpepe/elizaos-tcg-oracle-plugin)** | Standalone ElizaOS plugin for TCG market intelligence |

---

### 🖥️ Desktop & Mobile Apps

| App | Description | Stack |
|-----|-------------|-------|
| **[Undesirables Desktop](https://github.com/sailorpepe/undesirables-desktop)** | Full desktop app — TCG analytics, NFT generation, AI card grading, UNDSR slab renderer | Tauri v2, Rust, React |
| **[TCG Oracle App](https://github.com/sailorpepe/tcg-oracle-app)** | Cross-platform TCG market intelligence — price analytics, AI grading, Vault portfolio tracking | React Native, Expo |

---

### 🎮 Built on the Oracle

| Project | Description | Stack |
|---------|-------------|-------|
| 🕹️ **[The Syndicate](https://play.the-undesirables.com)** | A turn-based organized-crime game whose entire loot economy runs on the on-chain TCG oracle — every card you loot carries its **real** market price, price history, and an on-chain Merkle proof you can verify. Free, no wallet, plays in the browser. | React, TypeScript, Vite, Vercel |

> Proof the oracle is more than a data feed — the same on-chain prices now power a living game economy. **▶ [play.the-undesirables.com](https://play.the-undesirables.com)**

---

### 📊 By the Numbers

```
442K+    Products indexed across 25 TCG games
23M+     Price history data points
276K     Products Merkle-verified on-chain
819      Soul predictions Merkle-locked before outcomes exist
273      Souls competing on the public leaderboard
50       Blue-chip cards with hourly TWAP feeds
27       API endpoints (13 free, 14 paid)
35+      MCP local compute tools
24       Live-data AI agent skills
4,444    NFTs generated (ERC-721)
94       Solidity test cases passing
```

---

### 🛠️ Tech Stack

<div align="center">

![Solidity](https://img.shields.io/badge/Solidity-363636?style=flat-square&logo=solidity&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Rust](https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=next.js&logoColor=white)
![Tauri](https://img.shields.io/badge/Tauri-FFC131?style=flat-square&logo=tauri&logoColor=black)
![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
![React Native](https://img.shields.io/badge/React_Native-61DAFB?style=flat-square&logo=react&logoColor=black)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=node.js&logoColor=white)

![Ethereum](https://img.shields.io/badge/Ethereum-3C3C3D?style=flat-square&logo=ethereum&logoColor=white)
![Litecoin](https://img.shields.io/badge/Litecoin-A6A9AA?style=flat-square&logo=litecoin&logoColor=white)
![Mantle](https://img.shields.io/badge/Mantle-000000?style=flat-square&logo=mantle&logoColor=white)
![Base](https://img.shields.io/badge/Base-0052FF?style=flat-square&logo=coinbase&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=ollama&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white)
![ElizaOS](https://img.shields.io/badge/ElizaOS-000000?style=flat-square)
![FastMCP](https://img.shields.io/badge/FastMCP-000000?style=flat-square)

</div>

---

<div align="center">

*The AI does the work. The blockchain makes it real.*

**THE UNDESIRABLES LLC**

</div>
