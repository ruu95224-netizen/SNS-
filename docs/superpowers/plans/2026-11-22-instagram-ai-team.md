# Instagram AI社員チーム（28人） Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 設計書どおりの28人の担当定義・運用ルール・手順書（スキル）・テンプレートをこのリポジトリに作り、「リール作って」「ネタ出して」「会議して」「ルール追加：」で動くようにする。

**Architecture:** 担当は Claude Code サブエージェント（`.claude/agents/NN-slug.md`）、工程は スキル（`.claude/skills/*/SKILL.md`）、ルールは `rules/*.md`。サブエージェントは他のサブエージェントを呼べないため、**メインセッションが進行管理（00）を演じ**、スキルの手順に沿って各担当を順に呼び出す。成果物は `projects/<日付-テーマ>/` に担当ごとのファイルで残す。構造は `scripts/check_team.py` で検証する。

**Tech Stack:** Markdown（日本語）、Claude Code subagents / skills、Python 3 標準ライブラリのみ（検証スクリプト）。

**Spec:** `docs/superpowers/specs/2026-11-22-instagram-ai-team-design.md`（元資料：`docs/ruru-strategy.md`）

## Global Constraints

- 文書はすべて日本語。本人向けの文はやさしい言葉で書く。
- 実績表記は「施術約10,000件」。「10,000人」は禁止。
- 「治る」「改善する」の断定禁止。「ラクになりやすい」程度にとどめる。
- 根拠のない数値・事実は書かない。不明は「不明」、確認が必要なら「要確認」と明記して本人に質問する。
- 承認が必要：企画採用（★承認1）／台本確定（★承認2）／完成版確定（★承認3）／画像生成など外部ツールでの生成・書き込み／投稿／返信送信／ルール変更。
- 投稿ボタン・コメント/DM返信は本人。AIは下書きまで。
- トーン：落ち着いた語り口。AI音声用の話し言葉。専門用語には読みがな。
- 主指標：第1段階＝プロフィールアクセス数、第2段階＝リンククリック数（切替は本人決定、基準値は実績後）。
- 頻度：週2本。ブランドカラー：#1F3A5F／#F7F3E8／#6FA58A（薄 #8DBBA3）。テーマ配分：肩こり40・姿勢30・予防20・仕組み10。
- 企画NG：副神経の滑走アプローチ、姿勢矯正ベルト・磁気ネックレス・低周波治療器などの医療機器、「正しい姿勢を保て」型の主張、診断・治療を示す内容。
- アフィリエイトを含む投稿・キャプションには必ず「PR」表記。
- 差し戻しは最大2回、3回目は本人に相談。台本レビューは90点以上で合格。

## Review Focus

1. 事実確認で根拠が見つからない主張 → 台本から外すか「要確認」として本人に質問し、承認2の前に必ず提示される（fact-check と reel-production に明記、check で文字列検証）。
2. 本人が最初の依頼でテーマや「2日連続の何日目か」を言わない → 進行管理が不足情報を質問してから着手する（reel-production の Step 0、check で「不足情報」検証）。
3. 本人が承認せずに「次へ」と言う／承認を返さない → 承認ゲートを飛ばさず、承認待ちとして止まる（reel-production に「承認なしで次の工程に進まない」、check で検証）。
4. ルール変更の依頼が既存ルールと矛盾する → rule-update が矛盾を示して本人に選ばせ、反映後に CHANGELOG へ日付・内容・理由を記録する（check で CHANGELOG 書式検証）。
5. 担当の責任範囲の重複（例：CTA設計とキャプション作成） → 全担当に「やらないこと」節があり空でない（check で検証）。

---

## File Structure

| パス | 責任 |
|---|---|
| `scripts/check_team.py` | 構造検証（担当28人・必須見出し・ルール・スキル・承認ゲート文字列） |
| `CLAUDE.md` | 入口：チームの使い方、メインセッション＝進行管理、参照ルール一覧、合言葉 |
| `rules/brand.md, tone.md, ng-expressions.md, ng-planning.md, evidence.md, metrics.md, approval.md, CHANGELOG.md` | 運用ルール（更新可能） |
| `templates/handoff.md, script.md, canva-brief.md, caption.md, analysis.md, idea.md, meeting.md` | 成果物の共通書式 |
| `.claude/agents/00-progress-manager.md` … `27-improvement-proposal.md` | 28人の担当定義 |
| `.claude/skills/reel-production/SKILL.md` | 「リール作って」全工程 |
| `.claude/skills/idea-generation/SKILL.md` | 「ネタ出して」 |
| `.claude/skills/planning-meeting/SKILL.md` | 「会議して：○○」 |
| `.claude/skills/rule-update/SKILL.md` | 「ルール追加：○○」 |
| `ideas/backlog.md`, `projects/README.md`, `meetings/README.md` | 作業置き場 |

**担当一覧（番号・slug・日本語名）** — 全タスクでこの名前を使う：

```
00 progress-manager 進行管理      14 fact-check 事実確認
01 market-research 市場調査       15 expression-check 表現チェック
02 competitor-research 競合調査   16 material-collection 素材収集
03 post-collection 投稿収集       17 image-generation 画像生成
04 trend-research トレンド調査    18 diagram-design 図解作成
05 audience-analysis 視聴者分析   19 subtitle-writer 字幕作成
06 theme-selection テーマ選定     20 video-editing 動画編集
07 planning 企画立案              21 audio-adjustment 音声調整
08 structure-design 構成設計      22 quality-check 品質確認
09 hook-writer フック作成         23 post-management 投稿管理
10 script-writer 台本作成         24 caption-writer キャプション作成
11 title-writer タイトル作成      25 comment-analysis コメント分析
12 cta-design CTA設計             26 metrics-analysis 数値分析
13 script-review 台本レビュー     27 improvement-proposal 改善提案
```

**担当ファイルの書式（全28ファイル共通）：**

```markdown
---
name: <slug>
description: <日本語名>。<いつ呼ぶか1文>
tools: <必要なツールのみ。例：Read, Write, Glob, Grep / 調査系は WebSearch, WebFetch を追加>
---
# NN <日本語名>
## 目的
## 入力情報
## 作業手順
## 出力形式
## 完了条件
## 引き継ぎ事項
## やらないこと
## 参照ルール
```

---

### Task 1: 構造検証スクリプト

**Files:**
- Create: `scripts/check_team.py`

**Interfaces:**
- Produces: `python3 scripts/check_team.py` → 問題なしで `OK: all checks passed` と exit 0、問題ありで `NG: <理由>` を1行ずつ出し exit 1。後続タスクはこのコマンドで検証する。

- [ ] **Step 1: `scripts/check_team.py` を作成**し、以下を検査する関数を持たせる（標準ライブラリのみ）：
  - `check_agents()`：`.claude/agents/` に上記28ファイル名がちょうど存在。各ファイルのfrontmatterに `name:`（＝slug）と `description:`、8つの必須見出し（`## 目的`〜`## 参照ルール`）があり、`## やらないこと` 節が空でない。
  - `check_rules()`：`rules/` の8ファイルが存在。`ng-expressions.md` に `10,000人` と `治る` を含む。`CHANGELOG.md` に `| 日付 | 内容 | 理由 |` ヘッダ行。
  - `check_skills()`：4スキルの SKILL.md が存在し frontmatter に `name:` と `description:`。`reel-production` に `★承認1` `★承認2` `★承認3` `不足情報` `承認なしで次の工程に進まない` `要確認` を含む。
  - `check_files()`：`CLAUDE.md`, `templates/` 7ファイル, `ideas/backlog.md`, `projects/README.md`, `meetings/README.md` が存在。`agents/14-fact-check.md` に `不明` と `要確認` を含む。
- [ ] **Step 2: 実行して失敗を確認** — Run: `python3 scripts/check_team.py` / Expected: `NG:` 行が複数、exit 1。
- [ ] **Step 3: Commit** — `git add scripts && git commit -m "Add team structure checker"`

### Task 2: 運用ルールと CLAUDE.md

**Files:**
- Create: `rules/*.md`（8ファイル）, `CLAUDE.md`

**Interfaces:**
- Produces: 各担当の `## 参照ルール` が指すファイル名（上記8つ）。

- [ ] **Step 1: ルール8ファイルを作成**。内容は Global Constraints と `docs/ruru-strategy.md` の2・3・7・9・11章、設計書5・11章から転記・整理する。各ファイル冒頭に「最終更新日」と「変更は rule-update スキル経由・本人承認後」。
  - `tone.md`：落ち着いた語り口、やわらかい断定、フックは意外な事実や問いで引く（例「肩こり、マッサージしてもすぐ戻りませんか？」）、1画面1メッセージ、AI音声用の話し言葉と読みがな。「参考台本なし。最初の数本の後に本人の感想で更新」と明記。
  - `ng-expressions.md`：表で「NG表現｜理由｜言い換え」。
  - `evidence.md`：根拠の強さ（公的統計・システマティックレビュー／個別研究／臨床の視点＝本人確認）の区別、出典の書き方、「不明」「要確認」の使い方。
  - `metrics.md`：段階別指標（設計書5章の表どおり）、補助指標、数値は本人がインサイトから共有。
  - `approval.md`：承認が必要な作業一覧と各承認で本人に見せるもの。
  - `CHANGELOG.md`：`| 日付 | 内容 | 理由 |` 表に初版行（2026-11-22｜初版作成｜設計書に基づく）。
- [ ] **Step 2: `CLAUDE.md` を作成**：プロジェクト概要、**メインセッションが進行管理（00）として振る舞う**こと、合言葉（「リール作って」→reel-production、「ネタ出して」→idea-generation、「会議して：○○」→planning-meeting、「ルール追加：／ルール変更：」→rule-update）、作業前に `rules/` を読むこと、Global Constraints の要点。
- [ ] **Step 3: 実行** — `python3 scripts/check_team.py` / Expected: rules 関連の NG が消える。
- [ ] **Step 4: Commit** — `git commit -m "Add operating rules and CLAUDE.md"`

### Task 3: テンプレートと作業置き場

**Files:**
- Create: `templates/handoff.md, script.md, canva-brief.md, caption.md, analysis.md, idea.md, meeting.md`, `ideas/backlog.md`, `projects/README.md`, `meetings/README.md`

- [ ] **Step 1: テンプレートを作成**：
  - `handoff.md`：`## 渡すもの` `## 未解決事項（不明・要確認）` `## 次の担当への注意` `## 参照した根拠`。
  - `script.md`：表「シーン｜秒数｜ナレーション（読みがな付き）｜画面テキスト｜素材｜根拠ID」＋ 根拠一覧 ＋ 要確認リスト。
  - `canva-brief.md`：サイズ1080×1920、ブランドカラー、シーン別タイムライン、字幕位置、音声ファイル名、BGM指示。
  - `caption.md`：本文／導線文／ハッシュタグ／PR表記チェック欄。
  - `analysis.md`：投稿日・テーマ・本人共有の数値（空欄は「未共有」）・段階別指標評価・仮説（断定しない）。
  - `idea.md`：一言テーマ／想定する悩み／臨床視点の切り口の方向／配分カテゴリ／出どころ（本人・AI＋担当名）／状態（候補・採用・保留）。
  - `meeting.md`：議題／参加担当／各担当の意見と根拠／案ごとの利点・弱点／推奨／検証方法／本人の決定。
- [ ] **Step 2: `ideas/backlog.md`**（idea.md形式の表、空）、`projects/README.md`（フォルダ命名 `YYYY-MM-DD-<テーマ>`、ファイル `NN-slug.md`）、`meetings/README.md`（第1回議題：リールの構成の型 A〜D を記載、未開催）。
- [ ] **Step 3: 実行・Commit** — check で該当 NG が消えること。`git commit -m "Add templates and workspaces"`

### Task 4: 担当定義 00〜07（進行管理・リサーチ・企画）

**Files:** Create: `.claude/agents/00-progress-manager.md` 〜 `07-planning.md`

- [ ] **Step 1: 8ファイルを共通書式で作成**。責任範囲と「やらないこと」は設計書7章の表をそのまま使う。
  - 00：依頼受付→不足情報確認→引き継ぎ→承認とりまとめ→差し戻し管理（最大2回）→会議司会。「自分では制作物を作らない」。
  - 01〜05：tools に WebSearch, WebFetch。手順に「確認できた情報のみ、出典URLを付ける。確認できない数値は不明と書く」。05 は 25 の結果も入力に含む。
  - 06：①ネタの優先度づけ ②ネタ出し支援（候補5〜10個を `ideas/backlog.md` に idea.md 形式で追加）。
  - 07：企画案3つ（狙い・切り口・臨床視点・導線・配分カテゴリ・企画NG照合結果）。出力は ★承認1 用。
- [ ] **Step 2: 実行・Commit** — `git commit -m "Add agents 00-07"`

### Task 5: 担当定義 08〜15（台本・レビュー）

**Files:** Create: `.claude/agents/08-structure-design.md` 〜 `15-expression-check.md`

- [ ] **Step 1: 8ファイルを作成**。
  - 08：秒数配分・シーン割り、2日連続時は日ごとの役割（構成の型は会議決定に従う）。
  - 09：フック3〜5案、tone.md 準拠。10：script.md 形式で完成稿、フック・タイトル・CTAを統合、読みがな。11：カバー文字。12：段階1はプロフィール誘導。
  - 13：100点満点で採点（分かりやすさ・離脱ポイント・臨床視点・トーン）、90点未満は差し戻し理由つき。
  - 14：全主張に根拠ID・出典・強さ。根拠なしは削除か「要確認」。「不明」を明示。臨床視点の主張は「本人確認が必要」と印。
  - 15：ng-expressions.md と照合、PR表記、「施術約10,000件」。違反箇所と言い換え案の表。
- [ ] **Step 2: 実行・Commit** — `git commit -m "Add agents 08-15"`

### Task 6: 担当定義 16〜27（素材・編集・品質・投稿・分析）

**Files:** Create: `.claude/agents/16-material-collection.md` 〜 `27-improvement-proposal.md`

- [ ] **Step 1: 12ファイルを作成**。
  - 16：素材リスト・ライセンス確認。17：生成プロンプトまで、「生成の実行は本人承認後」。18：図解の構図・文字・ブランドカラー。19：字幕（1画面1メッセージ・強調語）。
  - 20：canva-brief.md 形式。21：AI音声設定（話速ゆっくりめ・間・読み）・BGM・音量。ツール未決定時は候補比較を本人に提示。
  - 22：全成果物チェックリスト（台本・字幕と音声の一致・読み・図解・ブランド・ルール・PR）→ ★承認3、不合格は該当担当へ差し戻し。
  - 23：週2本の投稿カレンダー、投稿前チェック、投稿記録。「投稿は本人」。24：caption.md 形式、PR表記必須。
  - 25：コメント傾向・返信下書き、「送信は本人」。26：analysis.md 形式、本人共有の数値のみ、段階切替の提案。27：次回企画・台本・ルールの改善案、ルール変更は rule-update 経由。
- [ ] **Step 2: 実行** — `python3 scripts/check_team.py` / Expected: agents 関連の NG がすべて消える。
- [ ] **Step 3: Commit** — `git commit -m "Add agents 16-27"`

### Task 7: スキル4本

**Files:** Create: `.claude/skills/{reel-production,idea-generation,planning-meeting,rule-update}/SKILL.md`

- [ ] **Step 1: `reel-production`**：設計書8章の工程を Step 0〜10 で記述。Step 0 で不足情報（テーマ／狙い／2日連続の何日目か／締切）を質問。各工程で呼ぶ担当 slug、成果物の保存先 `projects/<日付-テーマ>/NN-slug.md`、★承認1〜3で本人に見せるもの、「承認なしで次の工程に進まない」、差し戻しルール、要確認リストを承認2で必ず提示。
- [ ] **Step 2: `idea-generation`**：03・04・05・25 → 06 で候補5〜10個を `ideas/backlog.md` に追加し本人に提示。選ぶのは本人。
- [ ] **Step 3: `planning-meeting`**：議題に応じた参加担当、meeting.md 形式で `meetings/` に保存、効果予測は根拠がなければ「検証が必要」、決定は本人。
- [ ] **Step 4: `rule-update`**：変更案（ファイル・変更前後・理由・既存ルールとの矛盾）を提示 → 本人承認後に反映 → CHANGELOG に行追加。
- [ ] **Step 5: 実行** — `python3 scripts/check_team.py` / Expected: `OK: all checks passed`、exit 0。
- [ ] **Step 6: Commit & push** — `git commit -m "Add workflow skills" && git push`
