# Competitor deep-dive A: DAT, Truckstop, Loadhunt

Research date: 2026-10-30. Prices are monthly USD and exclude taxes unless noted. Vendor-reported figures are marked as such. Anything I could not confirm is marked **(unverified)**.

**What "Loadhunt" turned out to be.** The freight player is **LoadHunt Corp.** (loadhunt.ai; its Chrome extension is "LoadHunter", formerly loadhunter.io). It is a small US dispatcher-tooling startup. Its main product is a Chrome extension that sits **on top of** DAT One, Truckstop and Super Dispatch, plus a young TMS. It is **not a load board or marketplace**, so it does not compete with DAT and Truckstop head-on. It depends on them. Other companies with similar names are listed in section 3.

---

## 1. Comparison table

| Dimension | DAT (DAT One / Convoy) | Truckstop | LoadHunt (LoadHunter extension + huntTMS) |
|---|---|---|---|
| 1. Identity | DAT Freight & Analytics. Founded 1978 as Dial-A-Truck. HQ Portland/Beaverton, OR (also Denver). Business unit of Roper Technologies (NASDAQ: ROP). Revenue is not broken out. | Truckstop (Internet Truckstop Group). Founded 1995 by Scott Moscrip. HQ Boise, ID. ICONIQ has been majority owner since 2019. Moscrip has been back as CEO since June 2025. | LoadHunt Corp. (Delaware registered-agent address). Small and early-stage. Team named on its token site: CEO Dino Nour. No disclosed funding. Has a Solana memecoin ($LHUNT). |
| 2. Model / broker in loop? | Load board plus an automated digital-matching marketplace (Convoy Platform) plus data (DAT iQ), tracking (Trucker Tools) and factoring (Outgo). **Brokers post most loads.** Shippers can also post (custom pricing). Carriers search. | Load board plus broker software (RMIS onboarding, TMS, Carrier Hub) plus factoring. **Brokers are the main posters.** Shipper plans also exist. | Overlay or productivity tool for dispatchers and small carriers. It holds **no freight of its own**. Users work broker-posted loads on DAT and Truckstop. |
| 3. Pricing | Carrier: $59 / $149 / $169 / $259 / $339. Broker: $159 / $319 / $449. Combo: $339 / $469. Shipper: by quote. Convoy is free for carriers. | Carrier: $42 / $135 / $159, Heavy Haul $299. Dry van: $35 / $129. Broker: $109 / $239 / $369. Shipper: $109 / $175 / $239. $35–42 application fee. | Extension: Basic $8.99–9.99, Standard ~$13.49, Pro ~$26.99 per dispatcher seat, Enterprise by quote. 14-day trial with no card. |
| 4. Scale | Over 700k daily load posts. 291M loads and trucks posted per year. 1.6–1.7M trucks in the network. Generally seen as #1 by volume. | "Hundreds of thousands of loads each day" (2026). No user count published. | Vendor claims: 7k+ users (Chrome Web Store shows 7,000), 1.8M loads reviewed, 3,100+ trucks dispatched in huntTMS. |
| 5. Core features | Search, rate data at every tier (DAT iQ), broker credit score and days-to-pay, Book Now / Priority Booking, TriHaul, tracking (Trucker Tools), factoring (Outgo, 4-hour pay), TMS/FTP integrations, mobile app. | Search, Rate Insights (with FreightWaves SONAR on some plans), Book It Now, Credit Stop, broker ratings, FuelDesk, free TMS, factoring, mobile app (Truckstop Go), APIs and an MCP server. | Load ranking and filters, profit and RPM calculator, spot-rate context, broker card with factoring check, one-click and automatic broker emails, Telegram alerts, route map. huntTMS adds dispatch timeline, driver app and BOL/POD. |
| 6. AI/ML (live vs marketed) | **Live:** Load Recommendations in DAT One (ML ranking of best-fit loads; mobile, June 2026), DAT iQ rate analytics, Convoy automated matching and auto-bidding. **Talk only:** agentic AI for tenders and back office. No NL search or negotiation agent found. | **Live:** AVA voice assistant (July 2026; voice load search, rates, call the broker), Rate Insights Advanced with AI explanations, Broker Assistant extension, Risk Factors carrier risk scoring, Document Audit (rate con / POD / invoice mismatches), Predictive Carrier Sourcing, AI-drafted shipper outreach, MCP server. | Very little. Gmail replies are processed through the OpenAI API. "AI emailing" and "AI Planify" are listed as coming soon. Planned huntOS would answer natural-language business questions. The token site lists a "FleetHunt AI dispatcher" and an "AI rate-con reader" Telegram bot **(unverified)**. |
| 7. Trust & fraud | MFA plus Verosint identity risk scoring. Network Governance team. Contact details stripped from free-text load fields. CarrierWatch carrier monitoring. DAT Assurance credit ($250–1,000) for unpaid freight. Still hit by large fake-load incidents (March 2025: 19k fake TQL loads). | Selfie plus driver's license check at sign-up, MFA, human review. RMIS onboarding (ID-to-selfie, W-9/TIN, OFAC). Risk Factors scoring. Blocked about 13k entities in 2024 and 70k+ in total. Customer survey claims 57% less fraud. | Shows FMCSA/MC data and factoring ratings for brokers on each load. Inherits the host boards' vetting. Nothing of its own. |
| 8. Sentiment | Praised for load volume and rate data. Criticized for renewal price hikes, fake or duplicate loads, fraud, and cost for owner-operators. | Praised for ease of use, price and support. Criticized for a dated UI, stale or duplicate loads, factoring payment problems (Denim era), and billing/cancellation friction. | Few reviews, all positive: Trustpilot 4.4 (11 reviews), Chrome Web Store 4.6 (30 ratings). Praise centers on dispatcher time saved and support. No independent coverage. |
| 9. Strengths / weaknesses | **S:** network effects and data moat, full stack (board, automation, tracking, pay). **W:** brokers are its core, fraud keeps recurring, pricing irritates carriers, little consumer-grade AI. | **S:** cheaper, ahead of DAT on AI features (voice, document audit, risk scoring), strong broker vetting (RMIS). **W:** #2 in volume, leadership churn, UI and factoring complaints. | **S:** cheap, fast iteration, works on top of the incumbents. **W:** depends on DAT/Truckstop page structure and ToS, tiny, crypto token attached, unverified claims. |
| 10. Relevance to us | Owns liquidity. Its Convoy Platform is the nearest thing to our automated booking, but it is still **broker-centric**. | Its AI roadmap (voice, document audit, risk scoring) overlaps with our planned document intelligence and trust scoring. Its loads are broker-posted too. | Shows dispatchers will pay for an AI/UX layer on top of the boards. Not a marketplace competitor. Its feature list (profit calculator, broker card, auto-email) is a useful checklist. |

---

## 2. Detailed profiles

### 2.1 DAT Freight & Analytics

**Identity**
- Founded in 1978 as Dial-A-Truck, a Jubitz Corporation subsidiary. Now a business unit of Roper Technologies (NASDAQ: ROP). [Wikipedia](https://en.wikipedia.org/wiki/DAT_Solutions), [DAT MATS 2026 release](https://www.dat.com/company/news-events/news-releases/dat-brings-new-business-tools-expertise-to-mats-2026)
- HQ is given as Portland, OR in the 2026 boilerplate. Other sources say Beaverton, OR with a co-HQ in Denver. Headcount estimates range from about 700 (Built In) to 1,001–2,000 (Prospeo) **(unverified)**. [Built In](https://www.builtincolorado.com/company/dat)
- Revenue is not public. Roper does not break DAT out. [Transport Intelligence](https://ti-insight.com/briefs/dat-acquires-convoy-platform-in-freight-techs-biggest-shakeup-of-2025/)
- Acquisitions:
  - Trucker Tools (GPS tracking; closed 2024-12-17). [TT News / privsource](https://www.privsource.com/acquisitions/deal/B6SO6x)
  - Outgo (factoring; 2025-05-15). [Business Wire](https://www.businesswire.com/news/home/20250515100034/en/DAT-redefines-freight-payments-with-Outgo-acquisition)
  - Convoy Platform from Flexport (announced 2025-07-28; reportedly about $250M **(unverified)**). [Business Wire](https://www.businesswire.com/news/home/20250728801115/en/DAT-to-Acquire-the-Convoy-Platform-from-Flexport)
- On 2026-08-13 leadership was reorganized around customer segments, with a shared technology org tasked with integrating AI. [DAT news](https://www.dat.com/company/news-events/news-releases/dat-aligns-leadership-around-customer-segments-and-shared-technology)

**Business model.** DAT is a classic load board where brokers post and carriers search. It adds:
- **Convoy Platform:** automated matching where the broker sets a maximum buy rate and Convoy runs the bidding. Carriers either accept the target price or bid. The app is free to carriers, and carriers pay only when a load is digitally booked and delivered. Convoy handled about 100k loads per year, 98% automated, per a 2025 report **(older figure)**. [loadstop.com summary](https://loadstop.com/blog/convoy-automated-freight-matching-booking-for-brokers), [DAT support FAQ](https://one.support.dat.com/9-resources-52e74931/dat-acquisition-of-the-convoy-platform-d137c2d4)
- **Shipper plans** exist ("Contact for pricing"; a network of 668k trucks). Even so, the marketplace is broker-intermediated. **A broker is in the loop on the large majority of loads.**

**Pricing** (from [dat.com/load-boards](https://www.dat.com/load-boards), fetched 2026-10-30)

| Segment | Plan | Price/month | What it adds |
|---|---|---|---|
| Carrier | Standard | $59 | 15-day average spot rates, 2 search tabs |
| Carrier | Enhanced | $149 | 7-day rates, TriHaul, prefer/block companies |
| Carrier | Pro | $169 | "Best available" rates, 10 tabs, $250 DAT Assurance credit |
| Carrier | Select | $259 | Market Conditions map, $500 Assurance |
| Carrier | Office | $339 | Workgroups, Premium LaneMakers, $1,000 Assurance |
| Broker | Express | $159 | Post loads, 30-day spot rate |
| Broker | Select | $319 | Spot plus contract rates, alerts, TMS integration |
| Broker | Office | $449 | LaneMakers, team management |
| Combo | Select / Office | $339 / $469 | Broker and carrier features together |

- The carrier page mentions up to 500 load searches per month.
- Third-party sites list lower figures ($54 / $119 / $169 / $239 / $329; [CostBench, June 2026](https://costbench.com/software/trucking-tms/dat-freight/)). These are probably older prices or promotions.
- No free tier for the board. Convoy is free to carriers.

**Scale**
- More than 700k daily load posts and a database of over $1T in freight transactions. [DAT MATS 2026 release](https://www.dat.com/company/news-events/news-releases/dat-brings-new-business-tools-expertise-to-mats-2026)
- 291M loads and trucks posted per year. [dat.com/load-boards](https://www.dat.com/load-boards)
- 1.6–1.7M trucks in the network. The site gives both figures. [dat.com/load-boards](https://www.dat.com/load-boards)
- Brokers pay in 28 days on average, with an average credit score of 94/100. [dat.com/load-boards](https://www.dat.com/load-boards)

**Core features.** Search tabs and alerts, spot and contract rates (DAT iQ), broker credit score and days-to-pay, DAT directory and reviews, Book Now / Priority Booking, TriHaul, LaneMakers, Market Conditions Index, TMS/FTP integration and automated posting, the DAT One mobile app with an iPhone widget, Trucker Tools tracking, and Outgo factoring (approved invoices paid within 4 hours; loads with a blue checkmark are eligible).
- Convoy has a full AscendTMS integration (January–April 2026).
- Convoy shows reload options before the carrier books (June 2026).
- Sources: [Business Wire Outgo](https://www.businesswire.com/news/home/20250515100034/en/DAT-redefines-freight-payments-with-Outgo-acquisition), [Convoy reloads (Finviz/Yahoo)](https://finance.yahoo.com/sectors/technology/articles/dat-convoy-platform-now-shows-140000496.html)

**AI/ML**
- **Live:**
  - **Load Recommendations** in the DAT One mobile app, launched 2026-06-25. It "learns how the user operates" and ranks best-fit loads with no setup. [GlobeNewswire](https://www.globenewswire.com/news-release/2026/06/25/3317680/0/en/dat-introduces-load-recommendations-to-help-carriers-find-freight-faster-in-dat-one.html)
  - **DAT iQ** rate analytics and forecasting. A shipper-focused DAT iQ line was shown at Gartner in May 2026. [GlobeNewswire](https://www.globenewswire.com/news-release/2026/05/04/3286843/0/en/DAT-Brings-Shipper-Focused-Freight-Intelligence-to-Gartner-Supply-Chain-Symposium-Xpo.html)
  - **Convoy** automated matching and auto-bidding.
- **Marketed or talked about only:** AI agents for tender monitoring and rerouting (executive commentary), and agentic BI (a job posting, July 2026). [DAT 2026 Freight Focus](https://www.tmcnet.com/usubmit/-dat-2026-freight-focus-gradual-recovery-expected-transportation-/2025/12/10/10303653.htm)
- **Not found:** NL or conversational search, a negotiation agent, or document-AI products.
- DAT's own load board page does not use the word "AI".

**Trust & fraud**
- MFA plus Verosint identity and device-risk scoring.
- Contact info removed from free-text load fields to block spoofing.
- Network Governance team.
- [DAT blog: what's new in DAT's fight against fraud](https://www.dat.com/blog/whats-new-in-dats-fight-against-fraud)
- CarrierWatch monitoring and DAT Assurance credit appear in the plan tables. [dat.com/load-boards](https://www.dat.com/load-boards)
- Major incidents:
  - Hacked accounts produced thousands of "impossible" $20/mile load posts. [Overdrive](https://www.overdriveonline.com/business/article/15677875/dat-hacks-lead-to-thousands-of-impossible-20mile-load-posts)
  - About 19k fake loads posted under TQL's name (March 2025). [smallfleethq](https://smallfleethq.com/reviews/dat-load-board) **(aggregator)**

**Sentiment**
- Praise: largest volume, rate data. [G2](https://www.g2.com/products/dat-load-board/reviews), [Capterra](https://capterra.com/p/265434/DAT-Load-Board/reviews/)
- Complaints:
  - Renewal price increases of 25–45% **(aggregator claim, unverified)**.
  - Repeated fraud incidents. One G2 reviewer called it "the 3rd time".
  - Duplicate loads ("365 results, 30 unique").
  - Bait-and-switch brokers.
  - Polarized Trustpilot ratings: about 35% 5-star and 30% 1-star **(unverified)**. [smallfleethq](https://smallfleethq.com/reviews/dat-load-board)

**Strengths.** Liquidity and data moat. A vertically integrated stack: board, rates, automated booking, tracking, factoring. Corporate backing from Roper.

**Weaknesses.** Built for brokers. Recurring fraud. Carriers resent the price. AI is incremental, mainly ranking and analytics.

**Relevance to us**
- DAT is the liquidity benchmark. Do not try to out-volume it.
- **Copy:**
  - Broker credit score and days-to-pay, applied to shippers in our case.
  - An Assurance-style payment guarantee.
  - Reloads at the drop-off point.
  - The rate context DAT shows on every listing.
- **Gap:** DAT never removes the broker. Even Convoy's automation sits under broker buy rates. NL search and a negotiation agent are white space at DAT as of October 2026.

### 2.2 Truckstop

**Identity**
- Founded in 1995 by Scott Moscrip. HQ Boise, Idaho (press releases are datelined Boise).
- ICONIQ Capital (ICONIQ Growth) became majority shareholder in April 2019, buying out Bregal Sagemount's 2016 minority stake. Moscrip and management kept significant stakes. **No later ownership change found (2019 data).** [FreightWaves](https://www.freightwaves.com/news/iconiq-acquires-majority-stake-in-truckstop-com), [Idaho Business Review](https://idahobusinessreview.com/2019/04/03/monster-trucks-truckstop-com-gets-major-investment/)
- CEO Kendra Tucker (from April 2022) stepped down in June 2025. Moscrip returned as interim CEO, a permanent search was announced, and no permanent CEO had been found as of October 2026. [Truckstop PR](https://truckstop.com/press-releases/interim-ceo-to-lead-next-chapter/), [TT News](https://www.ttnews.com/articles/truckstop-tucker-moscrip)
- Revenue is not public.

**Business model**
- A load board with three sides (carrier, broker, shipper) plus a broker software suite: RMIS onboarding and compliance, Carrier Hub, Truckstop TMS, Shipper Hub.
- Factoring is Truckstop Factoring, previously branded Denim by Truckstop.
- **Brokers are the dominant posters.** Shippers can post on dedicated shipper plans.
- Distribution deal with Trucker Path (2026-04-14): the Truckstop load feed now appears inside the TruckLoads app (Trucker Path cites more than 1M drivers). [HDT/truckinginfo](https://www.truckinginfo.com/news/trucker-path-truckstopcom-expand-load-access-partnership)
- Heavy Haul Load Board Pro launched in January 2026. [CCJ](https://www.ccjdigital.com/technology/video/15815596/truckstopcom-launches-heavy-haul-load-board-pro)

**Pricing** (from [truckstop.com/product/load-board/pricing](https://truckstop.com/product/load-board/pricing/), fetched 2026-10-30; per user, excluding fees and taxes)

| Segment | Plan | Price/month | Notes |
|---|---|---|---|
| Carrier | Basic | $42 | Unlimited search, truck posting, private loads, free TMS. Up to 3 users. |
| Carrier | Advanced | $135 | Broker ratings, faster booking (Book It Now), fuel and routing, **AVA** |
| Carrier | Pro | $159 | Rate Insights, live loads, lane planning, load comparison |
| Carrier | Heavy Haul Pro | $299 | Permit and escort quotes |
| Carrier (dry van) | Basic / Pro | $35 / $129 | Per 3 users. Pro adds SONAR Insights, Book It Now, FuelDesk. |
| Carrier (reefer) | Basic / Pro | $42 / $159 | Per 3-user block |
| Broker | Basic | $109 | Posting, Broker Assistant AI, Load Boost at $1 each |
| Broker | Pro | $239 | Carrier Hub Basic, Rate Insights, Book It Now posting |
| Broker | Premium | $369 | Carrier Hub Advanced, **Predictive Carrier Sourcing** |
| Shipper | Basic / Advanced / Pro | $109 / $175 / $239 | Advanced adds Credit Stop and Rate Insights |

- A non-refundable application fee applies: $42 (or $35 for dry van), credited to the first month if approved.
- No standing free trial. Promotions are sometimes reported, for example 20% off for 6 months **(unverified)**.
- RMIS Lite starts at about $340/month **(third-party, unverified)**. [Tekpon](https://tekpon.com/software/truckstop-rmis/reviews/)
- Older articles cite Pro at $79–99 and Premium at $149–175. Those prices are out of date.

**Scale**
- "Hundreds of thousands of loads each day." [AVA press release, 2026-07-07](https://truckstop.com/press-releases/truckstop-launches-ava-voice-assistant/)
- 413 G2 reviews.
- No published user or carrier count found.

**Core features.** Load search and posting, Rate Insights (Advanced shows paid vs. posted rates), Book It Now (instant booking at the posted rate, for preferred carriers; vendor claims +$200 per load), Credit Stop, broker ratings, FuelDesk, Truckstop Go mobile app, free TMS, factoring, and APIs plus an MCP server. [Book It Now](https://truckstop.com/product/load-board/book-it-now/)

**AI/ML** ([truckstop.com/ai](https://truckstop.com/ai/), all listed as live)
- **AVA (Advanced Voice Assistant):** launched 2026-07-07. Hands-free voice load search, rate context, connects the driver to the load owner, finds fuel and parking. Included on Advanced and Pro plans. It does **not** book autonomously; the carrier chooses. [Press release](https://truckstop.com/press-releases/truckstop-launches-ava-voice-assistant/), [FreightWaves](https://www.freightwaves.com/news/truckstop-com-launches-industrys-first-voice-native-carrier-assistant)
- **Rate Insights Advanced:** AI-generated explanation of how a rate is built, plus adjustments for the specific load. Announced in late October 2026. [TheTrucker.com](https://www.thetrucker.com/trucking-news/business/truckstop-bets-against-point-solutions-with-new-platform-updates) (summary via search; page returned 403 to the fetcher)
- **Document Audit:** compares the rate con, POD and carrier invoice against job details and flags mismatches. **This directly overlaps our planned document intelligence.**
- **Risk Factors:** High/Medium/Low carrier risk score from VoIP, VIN, IP and FMCSA signals across Truckstop and RMIS data. Available through an extension, an Outlook add-in or the API. **Overlaps our planned trust scoring.**
- **Broker Assistant:** a Chrome/Edge side panel for posting and market conditions.
- **Predictive Carrier Sourcing:** broker Premium tier.
- **Shipper Hub Smart Search:** AI-drafted outreach.
- **Truckstop MCP Server:** exposes load and capacity data to AI tools.
- **Not found:** an autonomous negotiation or booking agent, or NL text search. AVA is voice search, the closest equivalent.

**Trust & fraud**
- Selfie plus driver's license verification at account creation, MFA, human review. [FreightWaves, 2024-04-24](https://www.freightwaves.com/news/truckstop-ceo-industry-uniting-in-fight-against-load-board-fraud)
- Blocked about 13k entities that failed ID checks in 2024 and 70k+ overall. A customer survey reported 57% less fraud year over year. [FreightWaves, 2025-04-15](https://www.freightwaves.com/news/freight-fraud-everywhere-but-truckstop-ceo-asks-is-anybody-going-to-jail)
- RMIS onboarding: ID-to-selfie, W-9/TIN checks against the IRS, OFAC screening, continuous monitoring. [Truckstop blog](https://truckstop.com/blog/rmis-helps-brokers-combat-fraud/), [enhanced security PR](https://truckstop.com/press-releases/truckstop-introduces-enhanced-security-measures-to-further-safeguard-against-fraud/)
- Highway: I found **no Truckstop–Highway partnership**. Highway's partners are Tai, Transfix, Carrier1, Qued and others. Truckstop uses its own RMIS instead.

**Sentiment**
- G2: praise for ease of use and load availability. Complaint: the app looks dated. [G2](https://www.g2.com/products/truckstop-load-board/reviews)
- Trustpilot: factoring payments late or missing after the move to Denim, cancellation friction, an account ended over a selfie/ID re-verification request. [Trustpilot](https://www.trustpilot.com/review/truckstop.com)
- TrustRadius 7.2/10: users migrate to DAT, and specialized freight is thin. [TrustRadius](https://www.trustradius.com/products/truckstop-com-load-board/reviews)
- SoftwareFinder 3.3: stale or duplicate loads, missing RPM or destination on some listings. [SoftwareFinder](https://softwarefinder.com/supply-chain-management/truckstop-load-board)

**Strengths.** Cheaper than DAT. The most aggressive AI rollout of the three (voice, document audit, risk scoring, MCP). Strong broker vetting and onboarding through RMIS. New distribution through Trucker Path.

**Weaknesses.** #2 in liquidity. Leadership churn. Factoring and support complaints. Still broker-centric.

**Relevance to us**
- Truckstop is the competitor most likely to ship our planned AI features first. It already has document audit and risk scoring, and an MCP server could let third-party agents (like our negotiation agent) plug in.
- **Copy:**
  - AI rate explanations ("why this price"), which suits our dynamic pricing.
  - A voice interface as an extension of NL search.
  - ID-to-selfie onboarding as the baseline for trust scoring.
- **Gap:** still a broker-mediated board. Nothing lets a shipper hand a load directly to a vetted carrier with AI pricing and negotiation.

### 2.3 LoadHunt

**Which company this is.** Candidates found:

1. **LoadHunt Corp. (loadhunt.ai)**, the **most likely match**. A suite for small US trucking operations: the LoadHunter Chrome/Firefox extension (live) and huntTMS (live). huntDRIVE (ELD), huntPAY (invoicing and settlements) and huntOS (command layer with NL questions) are planned. The legal line reads "© 2026 LoadHunt Corp." [loadhunt.ai](https://loadhunt.ai/)
   - loadhunter.io now redirects with a 308 to extension.loadhunt.ai. [extension.loadhunt.ai](https://extension.loadhunt.ai/)
   - Chrome Web Store developer listing: "loadhunt", 600 N Broad St, Middletown, DE 19709. That is a common Delaware registered-agent address, so the real HQ is not disclosed. Phone numbers have a 312 (Chicago) area code. [Chrome Web Store](https://chromewebstore.google.com/detail/loadhunter/ogepjnnfghfpkpjjieenkcppifhmmcdg?hl=en)
   - Team named on its token site: Dino Nour (CEO), Fedorenco Iaroslav (CFO), Igor Mocalet (CTO), Antony Schastlivii (CMO). The names suggest an Eastern European team **(inference)**. The roadmap mentions "a YC application for FleetHunt". [coin.loadhunt.ai](https://coin.loadhunt.ai/)
   - Has launched a **$LHUNT utility token on Pump.fun** (1B supply, 7% to the team). This is a material reputational red flag.
   - No funding, revenue or founding date disclosed.
2. **The Load Hunter (theloadhunter.com).** A tiny carrier-facing PWA with a database of about 3,100 FMCSA brokers, a mini load board where brokers post for free, and a CRM. Freemium: free Scout tier with a 1.5% success fee capped at $25; Hunter $39; Hunter Pro $99 (adds "AI rate insights and negotiation drafting"); Fleet $189. The operator is anonymous. Interesting because it is AI-plus-negotiation positioned, but it is obscure. [theloadhunter.com](https://theloadhunter.com/)
3. **Load Hunter (loadhunter.net, Miami):** a dispatch service company. [Crunchbase](https://www.crunchbase.com/organization/load-hunter)
4. **Load Hunter Logistics Inc (Elburn, IL):** a 1-truck carrier. [CarrierSource](https://www.carriersource.io/carriers/load-hunter-logistics-inc)

Not relevant: Freight Hunt (freighthunt.us, a broker) and J.B. Hunt.

The rest of this section covers **#1, LoadHunt Corp.**

**Business model.** A productivity overlay for dispatchers, small carriers (1–50 trucks) and independent dispatch services.
- The extension "reads the row already on your screen" on DAT One, Power DAT, Truckstop, Super Dispatch and TruckSmarter. It has no freight of its own.
- The loads users work are broker-posted on the host boards, so **a broker is always in the loop**.
- It explicitly disclaims affiliation with DAT and Truckstop.
- A "huntOne" load board is on the roadmap (Phase 2 beta) **(unverified, token-site roadmap)**.

**Pricing** ([extension.loadhunt.ai](https://extension.loadhunt.ai/), 2026-10-30; per dispatcher seat)

| Plan | Price | Notes |
|---|---|---|
| Basic | $8.99/month billed yearly, $9.99 month to month | The hero section says "from $7.99", which is inconsistent |
| Standard | about $13.49/month yearly | Adds auto-emailing and Telegram alerts |
| Pro | about $26.99/month yearly | Adds SmartBoard. "AI emailing" and "AI Planify" are coming soon. |
| Enterprise | Contact sales | |

- Annual billing is 10% off. Team discounts start at 3 seats.
- 14-day free trial, no card required.
- huntTMS pricing is not listed separately ("From $9.99/mo" in a comparison table).

**Scale** (vendor claims, unverified)
- 7k+ users. The Chrome Web Store shows "7,000 users", and ExtScope earlier showed about 6,000.
- 1.8M loads reviewed.
- 3,100+ trucks dispatched in huntTMS.
- Case studies: "2.3x loads per hour" (a 6-truck Texas carrier) and "11 hours/week saved" (a 22-truck Illinois fleet).
- Chrome extension v3.1.0, updated 2026-10-27, so it is actively maintained.
- Sources: [loadhunt.ai](https://loadhunt.ai/), [ExtScope](https://www.extscope.org/extension/ogepjnnfghfpkpjjieenkcppifhmmcdg)

**Core features**
- Load ranking and filters (RPM+, deadhead, equipment, date).
- Profit calculator (fuel and tolls).
- Spot-rate range next to each load.
- Route map.
- Broker card (MC, FMCSA verification, factoring rating).
- Broker reviews from other dispatchers.
- One-click and automatic broker emails with templates, Gmail integration.
- Telegram load alerts.
- huntTMS: trip timeline, fleet status, driver app with BOL/POD capture, navigation and live location, shared tracking for brokers.
- No public API advertised.

**AI/ML**
- **Live:** minimal. Gmail replies are processed through the OpenAI API.
- **Marketed or coming soon:**
  - "AI emailing" and "AI Planify" (Pro).
  - huntOS natural-language questions and a rules engine.
  - "FleetHunt AI dispatcher" and a Telegram "AI rate-confirmation reader" plus a broker factoring-check bot, listed on the token site without a status **(unverified)**.
  - "AI forecasting" in roadmap Phase 4.
- Overall the marketing leans on "AI trucking", but the shipped product is mostly deterministic UI tooling.

**Trust & fraud.** Only surfaces public FMCSA/MC data and factoring ratings for each broker. Relies on the host boards' vetting. No identity verification of its own.

**Sentiment**
- Trustpilot: 4.4, 11 reviews, all 5-star, dated August 2025 to July 2026. The profile was claimed in August 2025 and the company replies to reviews. [Trustpilot](https://www.trustpilot.com/review/loadhunter.io)
- Chrome Web Store: 4.6 from 30 ratings.
- One 5.0 review on G2: one-click email and maps that work alongside DAT and Truckstop. [G2](https://www.g2.com/sellers/loadhunt)
- No Reddit, FreightWaves or Overdrive coverage found. The sample is small and possibly curated.

**Strengths.** Very cheap. Solves a real dispatcher pain: triaging hundreds of board rows and emailing brokers. Ships quickly. Expanding into TMS and payments around one shared load record.

**Weaknesses**
- Platform risk: it scrapes the DAT and Truckstop DOM, so a UI change or a ToS decision can break it. DAT and Truckstop also sell their own extensions, such as Truckstop's Broker Assistant.
- No liquidity of its own.
- Tiny and opaque: no disclosed HQ or founders on the main site, inconsistent claims.
- The crypto token undermines B2B trust.

**Relevance to us**
- Not a marketplace competitor today. If "huntOne" launches it could become a small one.
- It validates that small carriers and dispatchers pay for **decision support layered on loads**: profit per load, deadhead, a broker trust card, one-click outreach.
- These map onto our matching, ETA and planned pricing and trust features. Worth copying as UX:
  - net-profit and RPM-after-fuel per load
  - a counterparty card with payment reliability
  - templated one-click contact or booking.

---

## 3. Sources

DAT
- https://www.dat.com/load-boards
- https://www.dat.com/company/news-events/news-releases/dat-brings-new-business-tools-expertise-to-mats-2026
- https://www.dat.com/company/news-events/news-releases/dat-aligns-leadership-around-customer-segments-and-shared-technology
- https://www.globenewswire.com/news-release/2026/06/25/3317680/0/en/dat-introduces-load-recommendations-to-help-carriers-find-freight-faster-in-dat-one.html
- https://www.globenewswire.com/news-release/2026/05/04/3286843/0/en/DAT-Brings-Shipper-Focused-Freight-Intelligence-to-Gartner-Supply-Chain-Symposium-Xpo.html
- https://www.businesswire.com/news/home/20250728801115/en/DAT-to-Acquire-the-Convoy-Platform-from-Flexport
- https://www.businesswire.com/news/home/20250515100034/en/DAT-redefines-freight-payments-with-Outgo-acquisition
- https://www.privsource.com/acquisitions/deal/B6SO6x
- https://ti-insight.com/briefs/dat-acquires-convoy-platform-in-freight-techs-biggest-shakeup-of-2025/
- https://finance.yahoo.com/sectors/technology/articles/dat-convoy-platform-now-shows-140000496.html
- https://one.support.dat.com/9-resources-52e74931/dat-acquisition-of-the-convoy-platform-d137c2d4
- https://loadstop.com/blog/convoy-automated-freight-matching-booking-for-brokers
- https://www.dat.com/blog/whats-new-in-dats-fight-against-fraud
- https://www.overdriveonline.com/business/article/15677875/dat-hacks-lead-to-thousands-of-impossible-20mile-load-posts
- https://www.tmcnet.com/usubmit/-dat-2026-freight-focus-gradual-recovery-expected-transportation-/2025/12/10/10303653.htm
- https://en.wikipedia.org/wiki/DAT_Solutions
- https://www.builtincolorado.com/company/dat
- https://costbench.com/software/trucking-tms/dat-freight/
- https://www.g2.com/products/dat-load-board/reviews
- https://capterra.com/p/265434/DAT-Load-Board/reviews/
- https://smallfleethq.com/reviews/dat-load-board

Truckstop
- https://truckstop.com/product/load-board/pricing/
- https://truckstop.com/ai/
- https://truckstop.com/press-releases/truckstop-launches-ava-voice-assistant/
- https://www.freightwaves.com/news/truckstop-com-launches-industrys-first-voice-native-carrier-assistant
- https://www.thetrucker.com/trucking-news/business/truckstop-bets-against-point-solutions-with-new-platform-updates
- https://truckstop.com/product/load-board/book-it-now/
- https://truckstop.com/press-releases/interim-ceo-to-lead-next-chapter/
- https://www.ttnews.com/articles/truckstop-tucker-moscrip
- https://www.freightwaves.com/news/iconiq-acquires-majority-stake-in-truckstop-com
- https://idahobusinessreview.com/2019/04/03/monster-trucks-truckstop-com-gets-major-investment/
- https://www.truckinginfo.com/news/trucker-path-truckstopcom-expand-load-access-partnership
- https://www.ccjdigital.com/technology/video/15815596/truckstopcom-launches-heavy-haul-load-board-pro
- https://www.freightwaves.com/news/truckstop-ceo-industry-uniting-in-fight-against-load-board-fraud
- https://www.freightwaves.com/news/freight-fraud-everywhere-but-truckstop-ceo-asks-is-anybody-going-to-jail
- https://truckstop.com/blog/rmis-helps-brokers-combat-fraud/
- https://truckstop.com/press-releases/truckstop-introduces-enhanced-security-measures-to-further-safeguard-against-fraud/
- https://tekpon.com/software/truckstop-rmis/reviews/
- https://www.g2.com/products/truckstop-load-board/reviews
- https://www.trustpilot.com/review/truckstop.com
- https://www.trustradius.com/products/truckstop-com-load-board/reviews
- https://softwarefinder.com/supply-chain-management/truckstop-load-board

LoadHunt and similar names
- https://loadhunt.ai/
- https://extension.loadhunt.ai/ (loadhunter.io redirects here)
- https://coin.loadhunt.ai/
- https://chromewebstore.google.com/detail/loadhunter/ogepjnnfghfpkpjjieenkcppifhmmcdg?hl=en
- https://www.extscope.org/extension/ogepjnnfghfpkpjjieenkcppifhmmcdg
- https://www.trustpilot.com/review/loadhunter.io
- https://www.g2.com/sellers/loadhunt
- https://theloadhunter.com/
- https://www.crunchbase.com/organization/load-hunter
- https://www.carriersource.io/carriers/load-hunter-logistics-inc

---

## 4. Gaps and uncertainties

- **"Loadhunt" identity.** LoadHunt Corp. (loadhunt.ai) is my best match. If the user meant theloadhunter.com, the AI-rate and negotiation-drafting freemium board, that is a different and even smaller company. Worth confirming with the user.
- **LoadHunt company facts.** HQ, founding date, funding and team are not disclosed on the main site. Team names come only from the token page. All usage numbers are vendor-reported.
- **Revenue.** Not public for DAT (inside Roper) or Truckstop (private, ICONIQ). The Convoy price of about $250M is reported, not confirmed.
- **Truckstop ownership after 2019.** No newer change found, but not ruled out. The permanent CEO is still unannounced as of the latest found sources.
- **DAT pricing variance.** Official site prices ($59 to $339) differ from aggregator prices ($54 to $329). Probably time-dependent or promotional.
- **Truckstop's late-October 2026 announcement** (Rate Insights Advanced and others): known only through a search summary, because TheTrucker.com blocked the fetch.
- **Daily load volumes are not comparable.** DAT counts "load posts" including duplicates. Truckstop says "hundreds of thousands" with no exact figure.
- **Review data is thin and noisy.** DAT price-hike percentages and Trustpilot distributions come from aggregator sites. LoadHunt has very few reviews, all 5-star, with replies from the vendor.
- **No Truckstop–Highway partnership found**, despite it being suggested in the brief. Truckstop relies on its own RMIS for carrier identity and vetting.
