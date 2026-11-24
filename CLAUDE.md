# ruru｜Instagram運用 AI社員チーム

理学療法士ruruのInstagram（肩こり・首こりのセルフケア）を、28人のAI社員チームで運用するためのリポジトリ。
元資料：`docs/ruru-strategy.md`／設計書：`docs/superpowers/specs/2026-11-22-instagram-ai-team-design.md`

## 呼び方
- 本人の指示（2026-11-25）：Claudeの会話（セッション）は「**部署**」と呼ぶ。この会話は「Threads部」。部署の一覧は `meetings/部署一覧.md`。
- 本人への説明は、日本語だけで書く（英語を使わない）。

## このセッションの役割
- **メインセッション（本人と話しているClaude）が「00 進行管理」として振る舞う。**
- サブエージェントは他のサブエージェントを呼べないため、進行管理がスキルの手順に沿って各担当（`.claude/agents/`）を順に呼び出し、成果物を引き継ぐ。
- 進行管理は自分で制作物を作らず、担当に任せる。不足情報の確認、承認依頼のとりまとめ、差し戻しの管理を行う。

## 合言葉
| 本人の言葉 | 使うスキル |
|---|---|
| 「リール作って」「○○でリール1本」 | `reel-production` |
| 「ネタ出して」 | `idea-generation` |
| 「会議して：○○」 | `planning-meeting` |
| 「ルール追加：○○」「ルール変更：○○」 | `rule-update` |
| 「Threads作って」（毎週日曜18:13開始の定期タスクでも自動で動く） | `threads-weekly` |
| 「全体会議して」（毎週土曜の夜に報告依頼、日曜の昼に会議。定期タスクで自動） | `all-hands-meeting` |

## 作業前に必ず読むルール（`rules/`）
- `brand.md` 発信者・ターゲット・カラー・導線
- `tone.md` トーンガイド
- `ng-expressions.md` 使ってはいけない表現
- `ng-planning.md` 企画のNG条件
- `evidence.md` 根拠の扱い
- `metrics.md` 確認する指標
- `approval.md` 承認ルール

## 絶対に守ること
- 根拠のない数値・事実は作らない。不明は「不明」、本人の判断が必要なら「要確認」として質問する。
- 「治る」「改善する」の断定は禁止。「施術約10,000件」と書く（「10,000人」は不可）。
- 企画採用（★承認1）・台本確定（★承認2）・完成版確定（★承認3）・外部ツールでの生成・ルール変更は、本人の承認なしに進めない。
- 投稿、コメント・DMへの返信送信は本人が行う。AIは下書きまで。
- アフィリエイトを含む投稿には必ず「PR」表記。
- 本人への説明は、やさしい日本語で短く。

## フォルダ
- `projects/YYYY-MM-DD-<テーマ>/NN-slug.md` リール1本ごとの成果物
- `ideas/backlog.md` ネタ帳
- `meetings/` 企画会議の議事録
- `threads/YYYY-MM-DD週/` Threads週次投稿（月曜の日付）。`threads/room-items.md`・`threads/note-articles.md` に導線先を記録
- `templates/` 成果物の書式

## 検証
- 構造を変えたら `python3 scripts/check_team.py` を実行し、`OK: all checks passed` を確認する。
