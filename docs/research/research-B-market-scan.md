# Research B — US Freight Marketplace Scan (excluding DAT, Truckstop, Loadhunt)

Prepared 2026-10-30 for "AI Loadboard" (direct shipper↔carrier marketplace, AI-first, US, demo stage).
Scope: competitors other than DAT / Truckstop / Loadhunt (covered by another agent; used only as reference points).

Conventions: **(unverified)** = single weak / vendor-only / aggregator source or my own background knowledge not re-confirmed this session. "Not public" = searched, nothing reliable found. All vendor scale numbers are self-reported marketing claims unless stated otherwise.

---

## 0. Selected companies (9) and why

| # | Company | Why it made the cut |
|---|---|---|
| 1 | **Doft** | Closest analog to us: free direct shipper↔carrier load board marketed as "no broker markup", plus AI rate forecast and an AI calling dispatcher. |
| 2 | **Amazon Relay** | The largest real-world "shipper posts, carrier books directly, no broker" board (single shipper: Amazon). Proves the direct model works when the shipper is big and pays reliably. |
| 3 | **Uber Freight** | Benchmark digital broker: instant-book app, fixed prices, 30+ AI agents, ~125k carriers. The UX bar carriers compare everyone to. |
| 4 | **Loadsmart** | Digital broker that opened a *marketplace* (ShipperGuide Marketplace, 2025) where shippers match to brokers/carriers via a pricing engine; shipped 11 AI agents in 2026. |
| 5 | **Highway** (incl. Trusted Freight Exchange) | Fraud/identity leader that launched its own verified-only freight exchange (2025). Trust is our planned differentiator; Highway is the incumbent there. |
| 6 | **HappyRobot** | Unicorn AI voice/text agent layer (negotiation, carrier sales, check calls) used by 8 of top-10 US brokers. Direct reference for our planned negotiation agent. |
| 7 | **FleetWorks** | YC/First Round-backed AI dispatcher/matching startup ($17M Series A, Oct 2025). Represents the "AI agent books trucks" wave, broker-side. |
| 8 | **Parade (now Mudflap)** | AI capacity/matching (CoDriver) for brokers, acquired by carrier fintech Mudflap (Apr 2026) — shows carrier networks + AI matching converging. |
| 9 | **TruckSmarter** (shut down Sep 2026) | Free carrier load board + AI "Dispatch", 500k+ carriers, $16M raised in 2025 — then acquired and shut down. Key cautionary tale for a free/AI-first board. |

---

## 1. Comparison table

| Dimension | Doft | Amazon Relay | Uber Freight | Loadsmart | Highway / TFX | HappyRobot | FleetWorks | Parade (Mudflap) | TruckSmarter |
|---|---|---|---|---|---|---|---|---|---|
| **1. Identity / status** | Place Stars, Inc.; "since 2016"; CEO Dmitri Fedorchenko; active | Amazon; active | Uber Technologies segment; Chicago; active, revenue growing again in 2026 | Chicago (unverified); ~$384M raised (Tracxn); active | Dallas; founded 2022; FTV-led growth round 2025; active | San Francisco; $150M Series C at $1.22B (Aug 2026); active | YC + First Round; $17M Series A (Oct 2025); active | Founded 2015 SF; acquired by Mudflap Apr 2026 | Acquired by unnamed buyer, app shut 2026-09-04 |
| **2. Model** | Direct marketplace / load board (shippers + brokers post); no per-load broker cut | Closed single-shipper direct board | Digital broker (asset-light 3PL) + TMS/managed transport | Digital broker + shipper TMS + marketplace | Trust/identity SaaS for brokers + verified exchange | AI agent tool layer (broker/shipper side) | AI agent tool layer (broker side) | AI capacity SaaS for brokers | Free carrier load board (aggregated broker freight) + AI dispatch |
| **Broker in loop?** | Optional — shippers post direct; AI dispatcher calls brokers | No | Uber *is* the broker | Loadsmart is broker; marketplace also routes to brokers | Yes — brokers are the customers | Yes — sold to brokers | Yes | Yes | Yes (brokered freight) |
| **3. Pricing** | Shipper free; carrier Basic $0, Premium $19.99/mo; $0.99 booking fee; AI calls $1.29–2.29/answered call; factoring 2.49% | Free for carriers (no subscription/fees) | Free for carriers; margin on loads; quick pay terms disputed | Free for carriers; broker margin; AI agents free PoC, pay-for-results | Brokers $150–$500/mo tiers; carriers free; TFX free for qualified carriers | Enterprise; ~$250k min annual spend (reported) | Not public | Not public (enterprise SaaS) | Board free; Dispatch paid (price not found) |
| **4. Scale (claims)** | 360k+ vetted carriers; 150k–200k+ loads/day | Not public (Amazon volume) | ~$20B freight under mgmt; 125k+ carriers; Q2'26 freight rev ≈$1.58B | ~80k carriers (old, unverified) | 1,050+ brokers incl. 70 of top 100; 280k+ carriers analyzed | 150+ customers; 10M+ interactions/mo | 10k+ carriers, 15+ top-100 brokers in 6 months | $40B cumulative freight; Mudflap 515k drivers / 100k carriers | 500k+ carriers at shutdown |
| **5. Core features** | Search, post truck, alerts, one-click book, bidding, rate cons, factoring, Doft Dispatch TMS, iOS/Android | Book, tracking, Amazon payment; app | Instant book, fixed price, quick pay, tracking, TMS, app | Instant book/bid, ShipperGuide TMS, tracking required, partner-board syndication | Carrier vetting, onboarding, monitoring, Load Lock, TFX exchange + LoadPay payments | Voice/SMS/email/WhatsApp agents; TMS & phone-system integrations | AI dispatcher (calls/email/SMS) | Capacity mgmt, carrier matching, TMS integrations | Load search, AI Dispatch, factoring partner |
| **6. AI/ML** | AI rate forecast ($/mi, live); AI Calls voice agent negotiates with brokers (live, priced); auto matching | Algorithmic tendering (unverified) | 30+ agents, Insights AI, proprietary logistics LLM (shipper side, live); carrier-side AI not described | 11 AI agents (live, Sep–Oct 2026); ML instant quotes | Identity engine (rules/ML, no explicit AI claims) | Core product = LLM agents (live, at scale) | Core product = AI dispatcher (live) | CoDriver gen-AI agent: email, trucklists, inbound voice (live) | AI Dispatch (live until shutdown) |
| **7. Trust & fraud** | FMCSA authority/insurance/safety checks; shippers verified before posting | Strict onboarding (DOT/MC, $1M liability, CSA) | Tighter onboarding; claims fraud incidents −20% (Q1 2026) | Onboarding; mandatory tracking | Category leader: identity, ELD-connected carriers, broker credit via Triumph | Not a trust product | Vetting not core | Relies on Mudflap verified network | Not found |
| **8. Sentiment** | Google Play 4.7/5 (~1.6k reviews); almost no independent reviews | Mixed: rates said $200–300 below broker freight | Mixed/negative on detention and rates (mostly 2019–20 forum posts) | App ~4.2/5 (80 ratings US); shipper side: glitches, rate accuracy | No independent reviews found; "expensive for small brokers" | Strong broker adoption; no carrier-sentiment data | Not found | Not found | Users stranded by sudden shutdown |
| **9. Strength / weakness** | + closest model, cheap, AI live / − tiny brand, unverifiable volume | + guaranteed freight, free / − one shipper, low rates | + scale, UX, data / − is a broker, take-it-or-leave-it rates | + full stack, AI agents / − broker margin, shipper-enterprise focus | + trust moat, broker network / − broker-centric, not a marketplace for shippers | + best-in-class agents / − enterprise-only, sells to brokers | + fast traction / − single-function | + data, carrier network now / − broker-only | + huge free user base / − no durable revenue → shut down |
| **10. Relevance to us** | **Direct competitor**; copy rate forecast + AI calls pricing | Proof direct works; we must make it work for *many* SMB shippers | UX bar (instant book, fixed price, fast pay) | Shows "marketplace + agents" convergence | Partner or copy: verified-only access as product | Reference for negotiation agent; carriers will face these bots | Same | Matching design reference | Warning: free board + AI isn't a business by itself |

---

## 2. Detailed profiles

### 2.1 Doft — closest direct analog
1. **Identity.** doft.com, product of Place Stars, Inc., "trusted since 2016" ([doft.com](https://doft.com/)). CEO/co-founder Dmitri Fedorchenko; Getloaded.com co-owner David Gee joined in 2017 ([FleetOwner](https://www.fleetowner.com/technology/article/21696071/trucktech-pioneer-joins-startup-doft)). HQ and funding: not public. Active.
2. **Model.** Freight matching platform + load board. Shippers post manually, via CSV/bulk, or Doft crawls their site; carriers search and book. Marketed as "no broker markup" / "no hidden per-load broker cuts" ([doft.com](https://doft.com/)). Brokers also post (carriers can filter "by broker or shipper") ([pricing](https://loadboard.doft.com/pricing-driver)) — so it is hybrid, not broker-free.
3. **Pricing.** Shippers: no subscription plans, most premium features free ([shipper pricing](https://loadboard.doft.com/pricing-shipper)); auto transport $99 flat booking fee ([doft.com](https://doft.com/)). Carriers: Basic $0/mo; Premium $19.99/mo (up-front rates on 10–30% of loads, 24/7 bidding, 20 parallel AI calls, one-click booking, backhaul matching); $0.99 load booking fee ([driver pricing](https://loadboard.doft.com/pricing-driver)). Factoring flat 2.49% ([doft.com](https://doft.com/)). AI Calls: $1.29 per answered call (≤5 min), $0.20/min after, capped $2.29; first 3 free ([AI dispatcher](https://www.doft.com/ai-dispatcher/)).
4. **Scale.** 360,000+ vetted carriers, "200,000+ loads a day" ([doft.com](https://doft.com/)); another Doft listing says 150,000 loads/day (unverified; inconsistent with the above). Live counters failed to render on our capture.
5. **Features.** Search, map/mileage, live feed, lane alerts, post-a-truck, one-click booking, bidding, digital rate cons, factoring, separate Doft Dispatch TMS (documents, tracking, invoicing), iOS/Android for both sides ([doft.com](https://doft.com/), [App Store shipper app](https://apps.apple.com/us/app/-/id1495014488)). No public API found.
6. **AI.** (a) Free AI rate forecast ($/mi) per load "trained on millions of shipments" — live. (b) AI rate benchmark for carriers. (c) **AI Calls**: voice agent phones up to 5 (or 10/20 on premium) brokers in parallel, asks load questions, counters offers within carrier-set rules, handles callbacks/texts and check calls, returns transcripts; flags "Needs your decision" — live and metered ([AI dispatcher](https://www.doft.com/ai-dispatcher/)). No published outcome metrics; example data labeled "representative".
7. **Trust.** Every carrier checked against FMCSA authority, insurance, safety rating, crash history; shippers verified before posting ([doft.com](https://doft.com/)).
8. **Sentiment.** Google Play ~4.7/5 from ~1,566 reviews (via third-party aggregator); one complaint about vague payment terms ([grand-screen](https://grand-screen.com/apps/doft-load-board-truck-loads/reviews/)). No r/Truckers / forum discussion found — low mindshare.
9. **S/W.** + Already ships much of our roadmap (direct posting, AI pricing, AI negotiation calls) at very low price. − Very low brand awareness, unverifiable volume claims, small company, AI agent points *carriers at brokers* (reinforces the broker channel rather than replacing it).
10. **Relevance.** Most direct competitor. Copy: transparent per-call metered pricing for AI agent; free shipper side. Exploit: Doft's AI is carrier-side and broker-facing; nobody yet offers an agent that negotiates **shipper↔carrier directly** on-platform with escrowed/verified payment.

### 2.2 Amazon Relay — direct model at scale (single shipper)
1. relay.amazon.com, Amazon. Active.
2. Closed board: only Amazon-approved carriers see/book Amazon freight; Amazon does not tender via third-party boards ([DejaOffice, Sep 2026](https://www.dejaoffice.com/blog/2026/09/15/how-amazon-relays-load-board-actually-works/)). No broker.
3. No subscription or per-load fees ([Small Fleet HQ, May 2026](https://smallfleethq.com/load-boards/amazon-relay)).
4. Volume not public; refreshes ~30s, roughly doubles in peak (DejaOffice — unverified).
5. Dry van, reefer, power-only; 53'/28' trailers, some 26' box ([truckinfo.net](https://www.truckinfo.net/guide/amazon-relay)).
6. AI: not publicly detailed (unverified).
7. Onboarding requires active DOT/MC, $1M auto liability, clean CSA; authority <90 days often manual review ([LoadWorkHub](https://www.loadworkhub.com/post/how-to-get-amazon-relay-loads-as-a-cargo-van-driver)).
8. Rates reported ~$200–300 below comparable broker freight (vendor blog, unverified) ([truckdispatchexperts](https://truckdispatchexperts.com/resources/amazon-relay-review-2026/)).
9. + Reliable payer, free, no broker. − One shipper, rate pressure, carrier dependency.
10. Proves carriers will use a direct, fee-free, instant-book board **when the shipper is creditworthy**. Our challenge: replicate that trust for many SMB shippers (shipper credit checks / payment guarantees).

### 2.3 Uber Freight — the digital-broker benchmark
1. uberfreight.com; Chicago dateline ([press](https://www.uberfreight.com/en-US/newsroom/uber-freight-launches-industry-first-ai-logistics-network-at-scale-ushering)); segment of Uber. Q2 2026 freight revenue ≈$1.58B, +~26% YoY; gross bookings +25% ([Uber Q2 2026](https://investor.uber.com/news-events/news/press-release-details/2026/Uber-Announces-Results-for-Second-Quarter-2026/default.aspx), [prepared remarks](https://s23.q4cdn.com/407969754/files/doc_earnings/2026/q2/transcript/Uber-Q2-26-Prepared-Remarks.pdf)). Uber cut ~10% of company-wide staff (Sep 2026); Freight-specific impact not disclosed ([Logistics Viewpoints](https://logisticsviewpoints.com/2026/09/02/ubers-restructuring-shows-where-ai-in-logistics-is-really-going/)).
2. Digital broker + managed transportation/TMS. Uber is the broker; shippers tender to Uber.
3. Carriers free; revenue = broker margin + TMS/managed services. Quick pay: App Store says "paid in 4 days or less, free quick pay" ([App Store](https://apps.apple.com/app/uber-freight/id1183931851)); an aggregator claims a 2.5% quick-pay fee now (unverified) ([checkthat.ai](https://checkthat.ai/brands/uber-freight/reviews)).
4. ~$20B freight under management; 1 in 3 Fortune 500 ([press, May 2025](https://www.uberfreight.com/en-US/newsroom/uber-freight-launches-industry-first-ai-logistics-network-at-scale-ushering)); 125,000+ truckload carriers (Uber Freight blog, Mar 2026, via search snippet — unverified) ([Uber Freight resources](https://www.uberfreight.com/en-US/resources/the-2026-guide-to-transportation-management)).
5. One-tap booking at a fixed shown price, no negotiation; approved carriers only ([App Store](https://apps.apple.com/app/uber-freight/id1183931851)); tracking; TMS; last-mile via Better Trucks stake ([Supply Chain Dive](https://www.supplychaindive.com/news/uber-freight-better-trucks-investment-stake-partnership/805331/)).
6. 30+ AI agents across procurement/execution/tracking/payments, Insights AI, proprietary logistics LLM; $1.6B freight moved through AI infra in prior year (May 2025) — shipper-facing, live. No carrier-facing AI described ([press](https://www.uberfreight.com/en-US/newsroom/uber-freight-launches-industry-first-ai-logistics-network-at-scale-ushering)). 2026 focus: document validation, shipment-inquiry automation ([Logistics Viewpoints](https://logisticsviewpoints.com/2026/09/02/ubers-restructuring-shows-where-ai-in-logistics-is-really-going/)).
7. Claims fraud incidents −20% after tighter onboarding/monitoring (Q1 2026 market update, unverified snippet) ([Uber Freight blog](https://www.uberfreight.com/en-US/blog/freight-market-update)).
8. Carrier complaints: detention pay hard to collect, take-it-or-leave-it rates ([Business Insider 2019](https://www.businessinsider.in/uber-freight-has-altered-the-fine-print-in-how-truckers-are-paid-for-detention-and-drivers-are-frustrated-with-the-change/articleshow/70968428.cms), [TruckersReport forum](https://www.thetruckersreport.com/truckingindustryforum/posts/9970049)); fast pay praised. Mostly dated.
9. + Scale, enterprise shipper base, polished app. − It's a broker (margin), carrier distrust of accessorial handling.
10. Sets the carrier UX bar: **instant book at a fixed price + pay within days**. Our direct model must match that without a balance sheet → needs payment guarantee/escrow partner.

### 2.4 Loadsmart
1. loadsmart.com; HQ Chicago (unverified); Series D $200–250M at $1.3B valuation (2022; sources differ), ~$384M total ([Tracxn](https://tracxn.com/d/companies/loadsmart/__mQn6jvcGrJmWOagWgIYS2keLYKEWWcn8lh0jGr1ZwgE), [Loadsmart press](https://www.prnewswire.com/news/loadsmart/)). Active; no 2026 round found.
2. Hybrid: digital brokerage + ShipperGuide TMS + **ShipperGuide Marketplace** (Feb 25, 2025) where brokers/carriers set pricing and service conditions and a pricing engine auto-matches shipments ([Loadsmart blog](https://blog.loadsmart.com/announcing-shipperguide-marketplace)).
3. Carriers free. AI agents: free PoC on one workflow, no payment if agent doesn't do the work ([Morningstar/PRN, Sep 2026](https://www.morningstar.com/news/pr-newswire/20260917cg47995/loadsmart-launches-ai-agents-that-come-with-freight-operators-behind-them)).
4. "80K+ carriers" (old, undated) ([123Loadboard release](https://www.123loadboard.com/press-releases/123loadboard-partners-with-loadsmart/)); no current figure.
5. Carrier loadboard with instant booking, preferred lanes, recommendations; mandatory tracking ([loadsmart.com/carrier](https://loadsmart.com/carrier/), [CCJ](https://www.ccjdigital.com/business/article/14932367/no-time-to-negotiate-carriers-brokers-use-tech-to-move-loads-quickly)); loads syndicated to Trucker Path and 123Loadboard ([FreightWaves](https://www.freightwaves.com/news/trucker-path-partners-with-loadsmart-to-provide-more-capacity)).
6. ML instant quotes (long-standing); Sep 2026 launched 6 AI agents "with freight operators behind them", ~80% resolved without a human (company claim); expanded to 11 agents Oct 20, 2026 (PO follow-up, detention, dock, yard, warehouse CS) ([PRN](https://www.prnewswire.com/news-releases/loadsmart-ai-adds-dock-yard-and-gate-agents-to-its-logistics-ai-platform-for-enterprise-shippers-302913091.html)). Live per press releases.
7. Onboarding + tracking requirement; no distinct fraud product found.
8. Carrier app ~4.2/5 (80 US ratings) ([appfollow](https://apps.appfollow.io/ios/loadsmart-loads/1256783942?country=us)); shipper-side complaints about glitches/rate accuracy via aggregators (low reliability).
9. + Full stack, enterprise shippers, AI agents with human backstop. − Broker economics, enterprise focus.
10. "AI agent + human operator, pay-per-outcome" is a smart go-to-market for trust; the marketplace pivot validates our direction but they keep brokers in it.

### 2.5 Highway (Carrier Identity + Trusted Freight Exchange)
1. highway.com, Dallas; founded 2022 by ex-TriumphPay CEO Jordan Graft; growth equity led by FTV Capital with Lead Edge (2025) ([FreightWaves](https://www.freightwaves.com/news/carrier-identity-platform), [FTV](https://ftvcapital.com/insights/driving-trust-in-trucking-why-we-invested-in-highway/)). CB Insights says Highway acquired Newtrul in Sep 2025 **(unverified, single source)** ([CB Insights](https://www.cbinsights.com/company/newtrul)).
2. Trust SaaS for brokers + **Trusted Freight Exchange (TFX)**, launched Aug 25, 2025 with Triumph: verified, ELD-connected carriers see loads from vetted brokers; fraud checks, rate verification, broker credit assurance and settlement on each transaction ([GlobeNewswire](https://www.globenewswire.com/news-release/2025/08/25/3138427/0/en/Highway-Launches-the-Trusted-Freight-Exchange-Powered-by-the-Triumph-Network.html)). Brokers post (must be Highway Connect customers meeting Triumph credit standards).
3. Highway Connect: Starter $150/mo, Growth $300, Connect Core $500, Load Lock $500, fraud add-ons $500; carriers free ([highway.com/llms.txt](https://highway.com/llms.txt)). TFX free for qualified carriers.
4. 1,050+ brokers incl. 70 of top-100 US ([FreightWaves](https://www.freightwaves.com/news/carrier-identity-platform)); fleet analytics on 280k+ carriers ([llms.txt](https://highway.com/llms.txt)). TFX adoption not public.
5. Vetting, onboarding, continuous monitoring, email/VoIP identity, Load Lock; Highway for Carriers (broker vetting, FMCSA change alerts); TFX payments via Triumph LoadPay. Embedded in Transfix TMS (Jun 2026) and AscendTMS ([Yahoo/Transfix](https://finance.yahoo.com/small-business/articles/transfix-highway-partner-freight-brokers-120000539.html), [TT News](https://www.ttnews.com/articles/ascendtms-partners-highway)).
6. No explicit AI features published; identity engine (ELD/device/behavioral signals).
7. Category leader. Publishes a Freight Fraud Index estimating fraud costs ~$18M/day (May 2026, company claim) ([GlobeNewswire](https://www.globenewswire.com/news-release/2026/05/20/3298585/0/en/highway-positions-identity-verification-as-critical-defense-against-freight-industry-disruption.html)).
8. No independent user reviews found; one analysis notes enterprise pricing is hard for small brokerages ([airframe.ai](https://www.airframe.ai/product/highway-com/analysis)).
9. + Trust moat, broker distribution, Triumph payments. − Broker-centric, no shipper-direct side.
10. Highway has shown the market accepts a **verified-only exchange**. For us: trust scoring should be core, and integrating Highway/FMCSA/ELD signals may be faster than building identity from scratch. Gap: TFX excludes direct shippers.

### 2.6 HappyRobot
1. happyrobot.ai, San Francisco (some sources say Madrid origins); $150M Series C at $1.22B post (Aug 4, 2026; Prysm + Eurazeo), ~$200M total; Series B $44M (2025, Base10) ([Yahoo Finance, Aug 2026](https://finance.yahoo.com/technology/ai/articles/happyrobot-wants-1-2-billion-091952274.html), [Reuters via Yahoo](https://finance.yahoo.com/news/happyrobot-raises-44-million-expand-113532658.html)).
2. AI agent layer sold to brokers/shippers/3PLs. Broker in loop by design.
3. Enterprise; ~\$250k minimum annual spend (article's reading — unverified).
4. 150+ customers incl. DHL, MODE Global; 8 of top-10 US brokers in production; 10M+ interactions/month, 70%+ autonomous resolution (company claims) ([Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/happyrobot-wants-1-2-billion-091952274.html)).
5–6. Voice-first agents across phone, email, SMS, WhatsApp, chat; carrier sales, rate negotiation, check calls, appointment scheduling, payment inquiries; integrates with McLeod, MercuryGate, Tai, RingCentral etc. Live at scale.
7. Not a trust product.
8. Strong broker adoption; advises upfront AI disclosure on calls (~5% opt-out, company claim) ([Dealroom](https://app.dealroom.co/news/note/nine-of-the-top-10-us-freight-brokers-inside-happyrobot-s-agentic-ai-land-grab)). No carrier-sentiment data found.
9. + Best-funded freight agent company. − Enterprise-only pricing; it automates the broker, not disintermediates it.
10. Our planned negotiation agent will compete for the same carrier conversations. Copy: multi-channel, TMS integration, disclosure policy. Opportunity: offer SMB shippers/small carriers an agent at per-use pricing HappyRobot doesn't target.

### 2.7 FleetWorks
1. fleetworks.ai (unverified domain); founder Paul Singer (ex-Uber Freight PM); $17M Series A led by First Round, with YC, Saga, LFX (Oct 2025) ([Yahoo Finance](https://finance.yahoo.com/news/ex-uber-freight-product-manager-173218360.html), [Goodmans](https://www.goodmans.ca/insights/post/goodmans-tech-blog/fleetworks-raises-us-17-million-to-accelerate-ai-driven-freight-matching)). Active.
2. AI dispatcher for brokers: handles carrier calls/emails/texts and matches trucks to loads. Broker in loop.
3. Not public.
4. 10,000+ carriers onboarded and 15+ top-100 brokers within 6 months (company claim) ([Yahoo Finance](https://finance.yahoo.com/news/ex-uber-freight-product-manager-173218360.html)).
5–6. AI matching + conversational booking; live. A FreightCaviar newsletter documented an AI broker call with wrong dates — evidence of agent errors in the wild ([FreightCaviar](https://freightcaviar.com/stories/carrier-calls-fleetworks-ai-freight-broker-with-wrong-dates)).
7–8. Not found.
9. + Fast traction, Uber Freight DNA. − Narrow, broker-dependent; competes with HappyRobot.
10. Shows AI agents are now table stakes on the broker side; also that agent errors are publicly embarrassing → we need guardrails + human handoff.

### 2.8 Parade (acquired by Mudflap)
1. parade.ai; founded 2015 SF; $17M Series B 2023 (I Squared, Menlo); acquired by Mudflap (carrier fuel fintech, 515k drivers / 100k+ verified carriers), announced Apr 15, 2026, terms undisclosed ([FreightWaves](https://www.freightwaves.com/news/mudflap-parade), [Parade](https://www.parade.ai/resources/parade-has-joined-forces-with-mudflap)).
2. Capacity-management SaaS for brokers; broker in loop.
3. Not public.
4. $40B+ cumulative freight transactions (company claim).
5–6. CoDriver gen-AI agent: processes carrier emails/trucklists, inbound voice ("industry's first voice AI for capacity management"), embedded in McLeod PowerBroker and Turvo ([McLeod](https://www.mcleodsoftware.com/why-mcleod/resources/press-releases/parades-codriver-brings-generative-ai-to-mcleod-softwares-powerbroker-tms-users/), [Parade](https://www.parade.ai/resources/the-industry-s-first-voice-ai-for-capacity-management-revolutionizing-how-freight-brokers-communicate)). Live.
7. Leverages Mudflap's verified carrier network.
8. Not found.
9. + Mature matching data + now a big carrier app. − Broker-only.
10. Trend: **carrier-side apps (fuel/payments) buying matching AI** to own the carrier relationship — the carrier app is the distribution moat. Consider partnering with a fuel/factoring app for carrier acquisition.

### 2.9 TruckSmarter — post-mortem
1. trucksmarter.com; $16M Series A led by Socium Ventures with Cox Enterprises (Sep 2025), alongside launch of AI "Dispatch" ([FreightWaves](https://www.freightwaves.com/news/trucksmarter-secures-16m-a-new-era-for-transport-ai)); lifetime funding figures conflict ($60–75M, unverified). Announced Sep 1, 2026 it had been acquired (buyer unnamed) and shut the app Sep 4, 2026 ([TruckersReport](https://www.thetruckersreport.com/news/trucksmarter-shuts-acquisition-leaving-500000-carriers-seeking-alternatives/), [Yahoo](https://finance.yahoo.com/small-business/articles/trucksmarter-shutting-down-124325759.html)).
2. Free carrier load board aggregating brokered freight + paid AI dispatch.
3. Board free; Dispatch paid (price not found).
4. 500k+ carriers at shutdown.
5–6. Load search, AI Dispatch (live until shutdown).
7. Not found.
8. Users stranded with 3 days' notice.
9. + Massive free adoption. − Monetization didn't sustain; dependent on broker freight it didn't own.
10. **Lesson:** user count ≠ business. A free board must monetize transactions (take rate, payments, factoring) early, and own supply (shippers), not just aggregate broker posts.

---

## 3. Also considered

| Name | URL | What it is / why excluded |
|---|---|---|
| 123Loadboard | 123loadboard.com | Classic board; carrier plans $39/$59/$79/mo ([123Loadboard FAQ](https://www.123loadboard.com/faq/123loadboard-cost/), [Capterra](https://www.capterra.com/p/234195/Load-Board/pricing/)). Broker-centric, little AI; similar to DAT/Truckstop reference set. |
| Trucker Path | truckerpath.com | Navigation app + free/paid load board, carrier-first ([FreightWaves](https://www.freightwaves.com/checkpoint/best-load-boards/)). Distribution play, not AI-first marketplace. |
| Direct Freight | directfreight.com | Secondary board, cheap tiers (~$19.99–29.99, 2025, unverified) ([truckingjobsinusa](https://truckingjobsinusa.com/blog/top-10-load-boards-2025)). Legacy, broker freight. |
| Trulos | trulos.com | Free ad-supported board + Dispatch TMS ([Capterra](https://www.capterra.com/p/10033686/Trulos-Dispatch/)). Small, low AI. |
| Newtrul | newtrul.com | Private network for brokers' TMS loads; AI carrier sales books ~20% of loads; carriers free, flat fee per booked load ([newtrul.com](https://newtrul.com/)). Possibly acquired by Highway (unverified). Broker tool. |
| Transfix | transfix.io | Sold brokerage to NFI (2024), now TMS/data only ([Trucking Dive](https://www.truckingdive.com/news/transfix-nfi-acquisition-software-service/718154/)). Lesson in digital-broker retreat. |
| Convoy | — | Shut down Oct 2023; tech bought by Flexport ($16M), then sold to DAT Jul 2025 for ~ $250M (reported) ([GeekWire](https://www.geekwire.com/2025/flexport-is-selling-convoys-technology-to-freight-giant-dat/), [FreightWaves](https://www.freightwaves.com/news/less-than-2-years-after-flexport-bought-convoys-tech-stack-its-being-sold-to-dat)). Covered by DAT agent. |
| RXO / Coyote | rxo.com | RXO bought Coyote for $1.025B (Sep 2024), 3rd-largest NA broker; RXO Connect "AI/ML digital brokerage" ([RXO](https://rxo.com/news/rxo-completes-acquisition-of-coyote-logistics/)). Traditional broker. |
| J.B. Hunt 360 | jbhunt.com | Carrier 360 marketplace since 2017, 600k+ trucks (older figure) ([FreightWaves](https://www.freightwaves.com/news/the-continual-innovation-of-the-j-b-hunt-360-platform-keeps-carriers-top-of-mind)). Asset-based 3PL's digital broker. |
| Echo Global Logistics | echo.com | Large tech-enabled broker (PE-owned) (unverified current details). Broker. |
| Flock Freight | flockfreight.com | Shared truckload; reported Series E 2025 at ~$867M valuation (Tracxn); CEO Pat Dillon (Aug 2026) ([Tracxn](https://tracxn.com/d/companies/flock-freight/__abxEZJbnqKZW9FMbtguaRsIQMDVu_HC-e0j-_ul6xdo), [GlobeNewswire](https://www.globenewswire.com/news-release/2026/08/27/3352085/0/en/study-finds-shared-truckload-delivers-measurable-multiyear-roi-across-business-profiles.html)). Different mode (pooling). |
| Greenscreens.ai | greenscreens.ai | AI rate prediction; acquired by Triumph for $160M (closed May 2025) ([TT News](https://www.ttnews.com/articles/triumph-buys-greenscreens), [SEC](https://www.sec.gov/Archives/edgar/data/1539638/000162828025008153/exhibit99-1_022625.htm)). Pricing reference for our dynamic-pricing feature; broker tool. |
| Vooma | vooma.ai | AI agents for broker order entry/quotes; ~$16.6M (Seed + $13M A, Dec 2024) ([DC Velocity](https://www.dcvelocity.com/startup-gets-16-million-to-fund-its-ai-for-freight-brokers)). Broker back-office. |
| Lanesurf (YC S25) | lanesurf.com | Voice AI booked a load calling 96 carriers in 10 min; claims +$50 margin/load ([FreightWaves](https://www.freightwaves.com/news/this-ai-booked-a-load-in-10-minutes-by-speaking-to-96-carriers-at-the-same-time)). Tiny; broker-side; overlaps FleetWorks. |
| Peer (YC S26) | — | AI-native freight brokerage, SF, ~$125k seed (Dealroom, unverified) ([Dealroom](https://app.dealroom.co/companies/peer_11)). Too early. |
| Oway (YC) | — | AI "rideshare freight" for LTL/partial loads, $4M seed Aug 2025, 7 states ([TechCrunch](https://techcrunch.com/2025/08/22/yc-backed-oway-raises-4m-to-build-a-decentralized-uber-for-freight)). LTL focus; worth watching as direct SMB-shipper model. |
| Numeo | numeo.ai | AI dispatch for carriers, Chrome extension on DAT, from $9.99/mo ([Numeo FAQ](https://numeo.ai/faq)). Carrier tool on top of boards. |
| Freight Hero / Evos / Nexcade / 5U | — | 2026 seed rounds for broker/forwarder back-office AI ([FinSMEs](https://www.finsmes.com/2026/07/freight-hero-raises-5m-in-seed-funding.html), [Forwarder News](https://www.forwardernews.com/news/2026-10-14-ai-agents-in-the-freight-back-office), [Loadstar](https://theloadstar.com/ls_press_release/nexcade-raises-6m-to-build-ai-agents-for-freight-forwarders/)). Back office, not marketplaces. |
| Mudflap | mudflapinc.com | Covered under Parade. |

---

## 4. Market-level observations

1. **AI agents are already table stakes — on the broker side.** HappyRobot (unicorn, 8 of top-10 brokers), FleetWorks, Lanesurf, Parade CoDriver, Newtrul, Loadsmart's 11 agents, Uber's 30+ agents. Almost all of this capital automates *the broker's* job (carrier sales, check calls, quotes). Very little is aimed at letting a small shipper and a carrier transact without a broker. Implication: "AI negotiation agent" alone is not differentiating; "AI that removes the need for a broker for SMB shippers" still is.
2. **The voice-call layer is turning into bot-vs-bot.** Doft sells carriers an AI that phones brokers ($1.29/call) while brokers deploy HappyRobot/FleetWorks to answer carriers. A marketplace where both sides' agents negotiate via structured API/bids (no phone) is a natural endpoint — and a space where a direct platform has a structural advantage.
3. **Trust is the product.** Fraud is the dominant pain: CargoNet 2025 ≈ $725M losses, 2,646 thefts (+18% YoY) ([Sheer Logistics](https://sheerlogistics.com/blog/cargo-theft-trends-and-stats/)); strategic/fraud-based theft growing as share (30–40%, sources differ) ([CCJ](https://www.ccjdigital.com/business/article/15752847/why-cargo-theft-is-exploding)); ~69% of fraud double-broker-related ([Overdrive](https://www.overdriveonline.com/business/article/15663342/how-load-boards-are-responding-to-fraud-double-brokering)). Highway built a verified-only exchange; Uber claims fraud −20% via onboarding. Every new marketplace will be judged on identity verification first. Note: double brokering is *structurally* reduced in a model with no broker in the middle — a real marketing point for us.
4. **Consolidation and failure are the norm; distribution beats features.** Convoy (failed 2023 → Flexport → DAT 2025), Transfix exited brokerage (2024), RXO bought Coyote (2024), Triumph bought Greenscreens (2025), Mudflap bought Parade (2026), Highway reportedly bought Newtrul (2025, unverified), TruckSmarter acquired and shut (Sep 2026, 500k carriers stranded). Lessons: (a) asset-light brokers burned cash on margin; (b) free boards with big user counts still died without transaction revenue; (c) acquirers are incumbents with distribution (DAT, Triumph, Mudflap) buying tech.
5. **Market timing: capacity is tightening.** The non-domiciled CDL rule (effective Mar 16, 2026) affects ~200k drivers; spot rates hit records (~$3.83/mi NTI, Jun 2026, reported) ([MarketScale](https://www.marketscale.com/industries/transportation/truckload-spot-rates-hit-all-time-record-383-per-mile-as-freight-market-surges), [CCJ](https://www.ccjdigital.com/economic-trends/article/15770679/cdl-enforcement-fallout-spot-rates-spike-as-carriers-exit-highscrutiny-states)). In a tight market shippers struggle to find trucks and brokers' margins compress — a window for direct shipper↔carrier tools, but carriers gain leverage and will pick payers they trust.

**White space for a direct, AI-first marketplace (our positioning):**
- **SMB shippers** (not Fortune 500 — Uber/Loadsmart's focus) who today call brokers: give them instant AI pricing (Doft/Greenscreens-style), verified carriers, and a structured negotiation agent.
- **Payment guarantee / escrow** — the thing that makes Amazon Relay and Uber Freight trustable for carriers. Partner with a factoring/payments provider (Triumph/LoadPay-type, Doft factoring) rather than carry credit risk.
- **Verified-only, both sides** (Highway TFX does carriers+brokers; nobody does verified carriers + verified direct shippers with credit signals).
- **Agent-to-agent negotiation in-platform** (bids/counter-offers via API) instead of phone bots.
- **Monetize per transaction from day one** (TruckSmarter lesson); Doft's $0.99 booking fee + metered AI calls is a concrete reference.

---

## 5. Sources (primary list) and gaps

Key sources: Doft ([home](https://doft.com/), [driver pricing](https://loadboard.doft.com/pricing-driver), [AI dispatcher](https://www.doft.com/ai-dispatcher/)); Uber ([Q2 2026](https://investor.uber.com/news-events/news/press-release-details/2026/Uber-Announces-Results-for-Second-Quarter-2026/default.aspx), [AI network press](https://www.uberfreight.com/en-US/newsroom/uber-freight-launches-industry-first-ai-logistics-network-at-scale-ushering)); Loadsmart ([AI agents](https://www.morningstar.com/news/pr-newswire/20260917cg47995/loadsmart-launches-ai-agents-that-come-with-freight-operators-behind-them), [11 agents](https://www.prnewswire.com/news-releases/loadsmart-ai-adds-dock-yard-and-gate-agents-to-its-logistics-ai-platform-for-enterprise-shippers-302913091.html), [Marketplace](https://blog.loadsmart.com/announcing-shipperguide-marketplace)); Highway ([TFX](https://www.globenewswire.com/news-release/2025/08/25/3138427/0/en/Highway-Launches-the-Trusted-Freight-Exchange-Powered-by-the-Triumph-Network.html), [funding](https://www.freightwaves.com/news/carrier-identity-platform), [llms.txt](https://highway.com/llms.txt)); HappyRobot ([Yahoo Aug 2026](https://finance.yahoo.com/technology/ai/articles/happyrobot-wants-1-2-billion-091952274.html)); FleetWorks ([Yahoo](https://finance.yahoo.com/news/ex-uber-freight-product-manager-173218360.html)); Parade/Mudflap ([FreightWaves](https://www.freightwaves.com/news/mudflap-parade)); TruckSmarter ([TruckersReport](https://www.thetruckersreport.com/news/trucksmarter-shuts-acquisition-leaving-500000-carriers-seeking-alternatives/), [FreightWaves](https://www.freightwaves.com/news/trucksmarter-secures-16m-a-new-era-for-transport-ai)); Convoy→DAT ([GeekWire](https://www.geekwire.com/2025/flexport-is-selling-convoys-technology-to-freight-giant-dat/)); Amazon Relay ([DejaOffice](https://www.dejaoffice.com/blog/2026/09/15/how-amazon-relays-load-board-actually-works/), [Small Fleet HQ](https://smallfleethq.com/load-boards/amazon-relay)). Others inline above.

**Gaps / uncertainties**
- Doft's volume claims (150k vs 200k loads/day) and funding are unverifiable; no independent reviews.
- Uber Freight carrier count (125k+) from a search snippet of its own blog; quick-pay fee status unclear.
- Loadsmart current carrier network size not public.
- Highway→Newtrul acquisition: single source (CB Insights).
- TruckSmarter buyer unknown; TruckersReport page returned 403 to direct fetch (content via search snippets).
- HappyRobot $250k minimum spend is a journalist's reading, not a published price.
- Sentiment data for most AI-agent vendors (HappyRobot, FleetWorks, Parade) from carriers is essentially absent.
- Amazon Relay rate comparisons come from vendor blogs.
- Spot-rate figures for 2026 differ by source/index.
