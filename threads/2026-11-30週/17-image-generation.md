# 17 画像生成｜Threads週次投稿 2026-11-30週｜12/1・12/4の添え画像（任意）

- 作成日：2026-11-23
- 担当：17 画像生成
- 入力：`threads/2026-11-30週/08-structure-design.md`（12/1・12/4の骨組み）、`threads/2026-11-30週/10-script-writer.md`（v3の本文）、`rules/brand.md`、`rules/approval.md`
- **この資料はプロンプト（指示文）だけ。生成はしていない。** 生成は、本人が「ツール」と「プロンプト」を見て承認したあとに、1枚ずつ行う（`rules/approval.md`：外部ツールでの生成は実行前に毎回承認）。
- 画像は**任意**。付けなくても投稿は成り立つ（本文だけで1本完結）。

---

## 0. 2枚に共通する条件

| 項目 | 決めたこと | 理由 |
|---|---|---|
| 人物 | **顔を描かない**。後ろ姿か、斜め後ろ。性別が目立たない、髪は短めのボブくらい、無地の服 | `rules/brand.md`（顔出しなし）。本人と見まちがわれないよう写真風にしない |
| キャラクター | **今回は使わない**。ruruのアイコン（A正面キャラクター／Bストレッチ／Cロゴタイプ）が**未決定**のため。2枚とも「同じ顔なしの人物・同じ絵柄」でそろえる | `docs/ruru-strategy.md`（アイコン未決定）、リール#1と同じ判断（顔なし後ろ姿イラスト）。`rules/brand.md` にはキャラクターの決まりが書かれていない |
| 絵柄 | フラットなイラスト、線は細め、影は少なめ。写真風・3D風にしない | 本人の写真と誤解されない／Canvaで文字を重ねやすい |
| 色 | 背景アイボリー #F7F3E8、人物の服・机はネイビー #1F3A5F、小物にグリーン #6FA58A、面に薄いグリーン #8DBBA3。**この4色＋白・薄いグレーだけ** | `rules/brand.md` ブランドカラー |
| サイズ | **4:5（1080×1350）を第1案**、1:1（1080×1080）を予備 | 依頼の条件（1:1か4:5）。Threadsでの表示の切れ方は**不明**（未確認）→上下に余白を多めにとる |
| 文字 | **画像の中に文字を入れない**（日本語・英語・数字とも）。画面・キーボードにも文字や記号を描かない | あとでCanvaで日本語を入れる前提。AIは文字がくずれやすい |
| 余白 | 画像の上側1/4ほどを無地のアイボリーにしておく | Canvaで見出しを入れる場所 |
| 物 | ノートPC・スタンド・キーボードは**形だけの汎用品**。ロゴ・ブランド名・特徴的なデザイン（りんごマーク等）を描かない | 依頼の条件。12/4はPR投稿なので、特定の商品に見えないほうが誤解がない |
| 体の描き方 | 筋肉・骨・患部を描かない。光る・赤くなる・波線・痛みマーク・「治る」方向の矢印・ビフォーアフターなし | 依頼の条件、`rules/ng-expressions.md`（効果の断定）。図解（比較・仕組み）は18の範囲 |

### 共通のネガティブ指定（ツールに「入れたくないもの」の欄があれば貼る）
```
text, letters, words, numbers, watermark, logo, brand name, apple logo, face, facial features, eyes, mouth, realistic photo, 3D render, anatomy, muscles, bones, skeleton, glowing body parts, red pain marks, pain lines, arrows, before and after, medical equipment, doctor, white coat, clipboard
```

---

## 1. プロンプト一覧

| シーン | 目的 | プロンプト | サイズ | 使うツール（案） | 承認状況 |
|---|---|---|---|---|---|
| 12/1 ノートPCを机にそのまま置いた場面 | 本文の「ノートPCは画面とキーボードがひとつ／手元に合わせると画面は低くなる」を、ひと目で場面として見せる（1行目の「置き方」に目を向けさせる） | 下の「1-1」 | 4:5（1080×1350）。予備1:1 | Canvaの画像生成（Magic Media など。無料プランで使える回数は**不明・要確認**）／代替：2章のCanva素材の組み合わせ | **未承認**（本人の返事待ち。生成していない） |
| 12/4 画面は上へ、キーボードは手元へ | 本文の「画面は上へ、キーボードは手元へ。セットで考える」を、配置の絵として見せる（商品の宣伝にしない） | 下の「1-2」 | 4:5（1080×1350）。予備1:1 | 同上 | **未承認**（本人の返事待ち。生成していない） |

### 1-1 12/1（火）ノートPCを机にそのまま置いた場面

**日本語の意味（本人確認用）**：アイボリーの背景。顔の見えない人が、斜め後ろから見た姿で机に座っている。ノートPCは机にそのまま置かれ、画面は低い位置。人は少しうつむき、頭がやや前に出ている（大げさにしない）。痛みの表現・矢印なし。上の1/4は空けておく。

```
Flat vector illustration, minimal and calm. A person seen from behind at a three-quarter back angle, sitting at a simple plain desk, working on a laptop placed directly flat on the desk. The laptop screen is low, so the person is looking slightly downward with the head a little forward. Subtle, natural posture, not exaggerated. No face visible, short bob hair, plain long-sleeve top in navy #1F3A5F. Desk and chair in navy #1F3A5F and light green #8DBBA3, a small plant or mug in green #6FA58A. Plain ivory background #F7F3E8. Use only these colors plus white and light gray. Generic laptop with blank screen, no logo, no keys with letters. Leave the top quarter of the image as empty ivory space. Thin lines, soft minimal shading, no text anywhere. Vertical 4:5 aspect ratio, 1080x1350.
```

- 注意：頭が前に出すぎる、首が不自然に曲がる、背中が極端に丸い絵は使わない（「姿勢が悪い人」を責める絵にしない。本文は「姿勢より置き方」）。
- 1:1にするとき：最後の行を `Square 1:1 aspect ratio, 1080x1080.` に替え、「top quarter」を「top fifth」に。

### 1-2 12/4（金）画面は上へ、キーボードは手元へ

**日本語の意味（本人確認用）**：1-1と同じ人・同じ絵柄・同じ色。ノートPCは無地のシンプルなスタンドにのせて画面が目の高さ近く（目より上にしない）。手元には外付けのキーボード。肩は力が抜けて下がっている。ロゴなし、光る演出・矢印なし。上の1/4は空けておく。

```
Flat vector illustration, minimal and calm, same style and same person as a previous image. A person seen from behind at a three-quarter back angle, sitting at a plain desk. The laptop is raised on a simple plain laptop stand so the top edge of the screen is about at eye level or slightly below, never above eye level. A separate external keyboard sits on the desk close to the person's hands, with forearms resting naturally and shoulders relaxed and down. No face visible, short bob hair, plain long-sleeve top in navy #1F3A5F. Desk, chair and stand in navy #1F3A5F and light green #8DBBA3, a small plant or mug in green #6FA58A. Plain ivory background #F7F3E8. Use only these colors plus white and light gray. Generic unbranded laptop, stand and keyboard: no logos, no brand-like shapes, blank screen, keys without letters. No glow, no sparkles, no arrows. Leave the top quarter of the image as empty ivory space. Thin lines, soft minimal shading, no text anywhere. Vertical 4:5 aspect ratio, 1080x1350.
```

- 注意：画面の上の端が**目より上**になっている絵は使わない（G3「目の高さとほぼ同じか、やや下」から外れる）。AIは高さを正確に描けないことがあるので、生成後に本人が目で確認する。
- 注意：スタンド・キーボードが**実在の商品に似た形**（特徴的な脚の形・刻印など）になったら使わない。
- 注意：「same person as a previous image」は、ツールが前の画像を覚えていないと効かない。そろわないときは、1-1の人物の説明（髪・服・色）をそのまま使っているので、近い絵柄にはなる。それでもそろわなければ2章の代替案へ。
- 1-1と1-2を並べて「ビフォーアフター」にしない（比較の図は18の範囲。効果の約束に見えるため）。
- 12/4は通常版（PR）・差し替え版Bのどちらでも同じ画像でよい（商品名・ロゴがないため。PRの要否は本文で判断済み：15）。

### 生成後の確認（本人が見る）
- 顔・文字・ロゴ・数字が入っていないか（入っていたら使わない）
- 手・指・机の脚がくずれていないか
- 2枚の人物・絵柄・色がそろっているか（そろわなければ2章の代替案に切り替え）
- 体が不自然に曲がっていないか、痛みを示す表現がないか

---

## 2. Canva無料プラン内でできる代替案（生成しない）

画像生成を使わず、Canvaの**無料素材（王冠マークのないもの）**を組み合わせる。外部での生成をしないので、生成の承認はいらない（素材を選んで置くのは本人の作業）。

| 日 | 作り方 | 検索語（例） |
|---|---|---|
| 12/1 | 4:5のデザイン → 背景をアイボリー #F7F3E8 → 「デスクワーク 後ろ姿」のフラットイラストを1点 → 机の上にノートPCのアイコンをそのまま置く → 服・机の色をネイビー／薄いグリーンに変更 | 「デスクワーク 後ろ姿 イラスト」「ノートパソコン 作業 イラスト」「working at desk back view」「laptop flat icon」 |
| 12/4 | 12/1と**同じデザインを複製**し、人物はそのまま → ノートPCの下に四角の図形（ネイビー）を足してスタンドに見立てる → 手元にキーボードのアイコンを1つ置く | 「キーボード アイコン」「keyboard flat icon」。スタンドは図形（長方形・台形）で作る |

- よい点：0円のまま。2枚の人物が必ず同じになる。色を変えられる単色・線画の素材を選べばブランドカラーにそろう。
- 気をつける点：素材の画面・キーボードに文字やロゴが描かれていないものを選ぶ。人物は顔の描かれていないもの。素材の商用利用の条件は**不明**（Canvaの規約を本人が確認：リール#1と同じ扱い）。
- リール#1の16（素材収集）で使った後ろ姿イラストと同じ作者の素材があれば、それを使うと絵柄がそろう（あるかは**不明**）。

---

## 3. 本人への承認のお願い（00がとりまとめ）

次のどれかを選んでください。
1. Canvaの画像生成で、1-1と1-2を作る（無料プランで使える回数は要確認）
2. 生成はせず、2章のCanva素材で作る
3. 今週は画像なし（本文だけで投稿）

1を選ぶ場合は、上のプロンプトのままでよいか、直したいところ（人物の髪型・服の色など）があるかも教えてください。

---
## 引き継ぎシート（17 画像生成 → 00 進行管理・23 投稿管理）

## 渡すもの
- 12/1・12/4の添え画像のプロンプト2本（英語の指示文＋日本語の意味）、共通のネガティブ指定、サイズ（4:5第1案・1:1予備）
- Canva無料プラン内の代替案（生成なし・素材の組み合わせ）
- 生成後の確認ポイント（顔・文字・ロゴ・画面の高さ・体の曲がり方）
- 生成済みの画像：**なし**（未承認のため。ファイル名もまだない）

## 未解決事項（不明・要確認）
- 要確認（本人へ）：画像を付けるか／付けるならCanva生成・Canva素材・画像なしのどれか（3章）。生成する場合はプロンプトの承認
- 要確認（本人へ）：Canva無料プランで画像生成を何回使えるか（このチームでは未確認）
- 要確認（本人へ）：キャラクター（アイコン案A/B/C）は未決定のため今回は使っていない。決まったら、人物をキャラクターに替えるか
- 不明：Threadsで4:5・1:1の画像がどう表示されるか（切れ方）。上下に余白を多めにとって対応
- 不明：Canva素材・生成画像の商用利用の条件（本人がCanvaの規約で確認）
- 不明：生成で「画面の上の端が目の高さ近く」を正確に描けるか（生成後に目で確認）

## 次の担当への注意
- 00：生成は本人の承認後のみ。承認の返事（ツール・プロンプト・回数）を記録してから実行を頼む。1-1と1-2はビフォーアフターとして並べない
- 23：画像は任意。付ける場合は1本目（本文）に添える。12/4は通常版・差し替え版Bどちらでも同じ画像でよい。画像の文字（見出し）はCanvaで本人が入れる。入れる文字は本文の言い回し（12/1「置き方」、12/4「画面は上へ、キーボードは手元へ」）にそろえ、「治る」「効く」「正しい姿勢」は使わない
- 生成済みになったら、ファイル名を `2026-12-01_laptop-flat.png`／`2026-12-04_stand-keyboard.png` の形で記録する（案）

## 参照した根拠
- E1：`threads/2026-11-30週/08-structure-design.md`（12/1・12/4の骨組み・言い回しの分担）（確認日 2026-11-23）
- E2：`threads/2026-11-30週/10-script-writer.md` v3（12/1・12/4の本文、G3の範囲「目の高さとほぼ同じか、やや下」）（確認日 2026-11-23）
- E3：`rules/brand.md`（顔出しなし・ブランドカラー4色・Canva無料プラン・ツール代）、`rules/approval.md`（生成は実行前に毎回承認）（確認日 2026-11-23）
- E4：`docs/ruru-strategy.md`（キャラクター・アイコン案は未決定）、`projects/2026-11-22-肩こりが戻る理由-01/16-material-collection.md`（顔なし後ろ姿イラストの方針・Canva素材の扱い）（確認日 2026-11-23）
- E5：厚生労働省「情報機器作業における労働衛生管理のためのガイドライン」別添5(2)ロ(ロ)（G3。10経由・14が原文確認。17はURLを開いていない）
