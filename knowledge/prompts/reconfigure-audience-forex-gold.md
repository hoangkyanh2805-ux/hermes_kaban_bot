# Prompt: Reconfigure audience → Forex / Gold / Signals

Gửi **một lần** qua Telegram sau khi cập nhật skills trên Railway (hoặc kèm nội dung dưới).

---

Cập nhật toàn bộ content pipeline sang niche **forex / gold / trading signals (XAUUSD)**.

**Audience:** `forex-gold-signals` — traders theo dõi vàng, forex, signal actionable.

**Research-agent (TinyFish):**
- Tìm 5 topic trending về XAUUSD / gold / forex mỗi run
- Query gợi ý: gold forecast, XAUUSD technical analysis, macro catalyst, key levels, trading signal
- Nguồn ưu tiên: FXStreet, Investing.com, Forex Factory, X
- **Không** research AI automation / no-code trừ khi liên quan trading tools
- Ghi Supabase `topics.audience` = `forex-gold-signals`

**Script-agent:**
- Format: trading signal script (macro catalyst HOẶC technical setup)
- Có: key levels, trade plan, risk note
- Voice: trader-to-trader, data-backed

**X-optimizer-agent:**
- Thread 4 phần: hook (no URL) → source link reply 1 → analysis/levels → CTA
- Phoenix signals_applied bắt buộc
- Hashtag tuỳ chọn: #XAUUSD #Gold #Forex

**Cron weekly:** giữ thứ Hai 07:00 Asia/Ho_Chi_Minh — research 5, produce top 2 packages.

Xác nhận đã hiểu và áp dụng cho mọi run tiếp theo.

---

## Verify

- [ ] `topics.audience` = `forex-gold-signals` trên run mới
- [ ] Không còn topic AI automation trong run mới
- [ ] `x_posts` thread có link ở reply 1

Spec repo: `content.yaml`
