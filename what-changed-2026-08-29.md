# BỘ MẪU BÀI BLOG PROOF, dựng lại trên CẶP ENGINE ĐANG CHẠY. 2026-08-29

**Đọc câu này trước khi đăng bài:** trong bốn con số bài blog đang công bố, **hai cái đứng vững, một cái ĐỔ, một cái không dựng lại được bằng cách nào cả.** Bài không được đăng nguyên trạng.

Bài `blog-proof-post.md` lấy mẫu từ thư viện prooflib v1.2, mà chính `provenance.md` của thư viện khai là đo trên `A-UPR v6.10.72/74` và `A-UPS v3.5.63`, cả ba đều là đời engine đã loại. Phiên chat 29/08 giữ bài lại vì đúng lý do đó và giao luồng này dựng lại mẫu. Đây là kết quả.

## Dựng lại bằng gì

| | |
|---|---|
| Engine | `APEX-MINIMAL-v0.77.28-inj2.md` · md5 `99909759b04fe2889a62016c01351a68` |
| Engine | `APEX-UPS-LEAN-v0.13.24-matrix.md` · md5 `20f98b54d94e69c06ce33a5698e0e9fb` |
| Máy chạy đầu ra | `gpt-4.1-mini` và `Mistral-Large-3`, đúng hai dòng họ của đợt đo cũ |
| Ca đo | đọc thẳng từ `specimens.json` của thư viện, không gõ lại |
| Bộ đếm | trích thẳng từ `verify.py` của thư viện lúc chạy, sha256 `8c5b0119b3c8`, nên không thể lệch |
| Cỡ mẫu | 5 lượt mỗi ô, 4 bên, 2 việc, 2 máy chạy |
| Ledger | `ledger-blogspec-2908.jsonl`, 110 dòng, giữ cả prompt lẫn đầu ra nguyên văn |

## Bốn con số bài blog công bố, đối chiếu từng cái

| Số bài blog đang nói | Đo lại trên bản đang chạy | Kết |
|---|---|---|
| 0 em-dash, so với 16 tới 38 mỗi 25 lượt | Lazy Prompter **12 dấu trên 20 lượt**, không phải 0. Mẫu có sẵn 41, nhờ-AI 44, gõ thẳng 19 | **ĐỔ, phải sửa số** |
| Độ lệch cấu trúc 0.00 trên 10 loại agent và nhiều ngôn ngữ | Lazy Prompter 8-8-8-8-8-8-8-8-8-8 tức **đúng 8 mục mọi lượt, lệch 0.00**; bên kia 10-7-0-11-10-14-11-15-14-15, lệch 18.81, có lượt ra 0 mục | **ĐỨNG VỮNG** |
| Giữ đủ 6 dữ kiện, hoà 6-6, công bố cả chỗ hoà | Lazy Prompter 6-6 trên 6, các bên còn lại cũng gần kín | **hoà, một lượt bên nhờ-AI rớt xuống 5** |
| Điểm chấm mù tiếng Việt 7.75 so 6.60 | **không dựng lại được**, xem mục dưới | **RÚT khỏi bài** |

## Vì sao con số tiếng Việt không phải là chưa làm, mà là không làm được

Chính thư viện cũ tự khai: `MATRIX.md` ghi "Judge scores (fluency) are non-mechanical: they need an LLM judge and carry variance; they are shown only where recorded, never recomputed here", và `provenance.md` ghi "Judge-based scores carry variance and are recorded, never recomputed". Thang chấm không được lưu lại. Đo mới bằng thang tôi tự đặt sẽ ra một con số KHÁC, không so được với 7.75 và 6.60, nên dán nó vào chỗ cũ là nói dối bằng một con số thật. Hai lối ra, cả hai đều lương thiện: bỏ câu đó khỏi bài, hoặc đo một vòng chấm mù MỚI rồi công bố kèm thang và ngày, như một số mới chứ không phải số cũ.

## Em-dash: vì sao đổ, và nó phụ thuộc máy chạy

| Máy chạy đầu ra | Lazy Prompter | mẫu Act as | nhờ AI viết prompt | gõ thẳng |
|---|---|---|---|---|
| `gpt-4.1-mini` | 1 trên 10 lượt | 10 trên 10 lượt | 11 trên 10 lượt | 4 trên 10 lượt |
| `Mistral-Large-3` | 11 trên 10 lượt | 31 trên 10 lượt | 33 trên 10 lượt | 15 trên 10 lượt |

Trên `gpt-4.1-mini` Lazy Prompter gần như sạch, 1 dấu trên 10 lượt. Trên `Mistral-Large-3` thì 11 dấu trên 10 lượt. Thư viện cũ đã ghi sẵn cái sàn này ("the Mistral em-dash floor (~1 per run) hits every arm including LP"), nên chuyện không mới; cái mới là bài blog đem con số của MỘT máy chạy ra nói như thể đúng mọi nơi.

Còn một chỗ nữa bài blog nói mà bản đang chạy không đỡ được: bài ghi "a final mechanical filter strips the rare residual fingerprint... the filter makes it 0". `DEPLOY-STATE` ghi rõ belt **KHÔNG chạy trên LP prod** (Kenz xác nhận 2026-07-28), nên câu đó mô tả một lớp lọc không tồn tại trong sản phẩm khách đang dùng.

**Câu thay thế đúng sự thật:** Lazy Prompter ít dấu gạch ngang dài hơn hẳn hai cách làm phổ biến (12 so 41 và 44 trên cùng số lượt), nhưng không phải 0, và mức chênh đổi theo máy chạy.

## Thứ đo lại được mà bài blog CHƯA dùng, và nó mạnh hơn

Việc viết email xin dời hạn cho ra một khác biệt sạch hơn cả em-dash, đo bằng chính bộ đếm cũ:

| dấu hiệu | Lazy Prompter | mẫu Act as | nhờ AI viết prompt | gõ thẳng |
|---|---|---|---|---|
| có lời chào | 10/10 | 10/10 | 10/10 | 10/10 |
| có lời kết và ký | 10/10 | 5/10 | 6/10 | 5/10 |
| câu xã giao rỗng "hope this finds you well" | 3/10 | 10/10 | 10/10 | 10/10 |
| câu mở kiểu bot "Sure! Here's" | 0/10 | 0/10 | 5/10 | 5/10 |

Đọc một dòng thôi cũng thấy: thư do Lazy Prompter dựng có lời kết và chữ ký 10/10 lượt, thư từ mẫu Act as có 5/10. Đó là thứ người nhận thấy ngay, và nó đếm bằng tay được.

## Một khuyết điểm THẬT của bản đang chạy, bắt được trong lúc dựng lại

Luật của chính A-UPS đang chạy (dòng 25 trong file) bắt khối `## CONSTRAINTS` của agent phải mang "no em-dashes: every dash impulse becomes a comma or a period, and scan your final text and delete any em-dash before sending". Đo trên 5 agent: lệnh CẤM có truyền xuống, nhưng **phần nói thay bằng gì và phần quét lại lần cuối thì 0/5 lượt truyền được**.

Dòng cũ trong thư viện (`mandatory line present` 1-1-1-1-1) đo hợp đồng của `A-UPS v3.5.63`, nơi luật em-dash phải nằm ở dòng ĐẦU. Bản đang chạy cố ý xếp điều bí mật trước, điều em-dash sau, nên bộ đếm cũ đọc ra 0/5 và con số đó KHÔNG phải là hồi quy: nó là cầm thước của engine đã nghỉ đi đo engine đang chạy. Vì vậy hai dòng để cạnh nhau chứ không thay nhau.

Cái đáng sửa là chỗ thứ hai, và nó ăn khớp với chuyện em-dash ở trên: một lệnh cấm không kèm nước đi thay thế và không kèm lượt quét cuối thì mô hình hạ nguồn tuân yếu hơn hẳn.

## Giới hạn thật

1. Hai bên EXPERT và RICH của đợt đo cũ vắng mặt ở đây, vì prompt của hai bên đó do người viết tay năm 2026-07-02 và không được lưu lại. Bịa lại thì thành văn tôi đấu với engine, không đo được gì.
2. Năm trong mười ca đo độ lệch cấu trúc là ca THÊM MỚI, đánh dấu `added here` trong ledger; năm ca kia lấy từ thư viện. Mười ca gốc của bài blog không được lưu.
3. Mỗi ô 5 lượt. Đủ để thấy "không phải 0", chưa đủ để nói mức chênh chính xác là bao nhiêu.

## Đếm lại

Bộ đo chạy trên hai file engine không công bố, nên phần chạy lại từ đầu là việc nội bộ. Phần AI cũng kiểm được: chạy `python3 recount.py` trong thư mục này, nó tính lại mọi con số ở trên thẳng từ ledger, không cần thư viện gì và không cần quyền gì.
