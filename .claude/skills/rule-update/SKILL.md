---
name: rule-update
description: 「ルール追加：○○」「ルール変更：○○」と言われたとき、または改善提案でルール変更が必要になったときに、変更案を示して本人の承認後に rules/ に反映し、CHANGELOG に記録する。
---
# ルール更新（rule-update）

**本人の承認なしにルールファイルを書き換えない。**

## 手順
1. 本人の言葉を、どのルールファイルの話か判断する：
   - トーン・話し方 → `rules/tone.md`
   - 使ってはいけない表現 → `rules/ng-expressions.md`
   - 企画のNG → `rules/ng-planning.md`
   - 根拠の扱い → `rules/evidence.md`
   - 指標 → `rules/metrics.md`
   - 承認 → `rules/approval.md`
   - 発信者・カラー・配分・頻度・構成の型 → `rules/brand.md`
   - 担当の作業内容 → `.claude/agents/NN-*.md`
2. 同じ値・記述のコピーを Grep で探す（`CLAUDE.md`、`.claude/agents/`、`.claude/skills/`、`templates/`）。例：施術約10,000件、承認一覧、テーマ配分、ブランドカラー、90点の合格ライン。見つかった箇所は影響範囲として変更案に含め、承認後に同時に更新する。
   既存のルールと矛盾しないか確認する。矛盾する場合は、矛盾する箇所を示し、どちらを優先するか本人に選んでもらう。
3. 変更案を本人に見せる：対象ファイル／変更前／変更後／理由／影響する担当。
4. 本人が承認したら反映し、ファイル冒頭の「最終更新」の日付を更新する。
5. `rules/CHANGELOG.md` の表の一番上（ヘッダの直下）に `| 日付 | 内容 | 理由 |` の形式で1行追加する。
6. 構造を変えた場合は `python3 scripts/check_team.py` を実行して `OK: all checks passed` を確認する。
7. 本人に「どこを・どう変えたか」を1〜2行で報告する。
