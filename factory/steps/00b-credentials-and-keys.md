# Step 0b — Credentials & API Keys

**Sau brief · Trước hoặc song song OPS Phase 1–2**

→ Hướng dẫn đầy đủ: **[../CREDENTIALS-AND-KEYS.md](../CREDENTIALS-AND-KEYS.md)**

---

## Thứ tự khuyến nghị

```text
1. DeepSeek API key
2. Telegram bot (BotFather) + user ID
3. Railway deploy + volume /data
4. Supabase project + SQL migration
5. Supabase URL + secret key → Railway + /data/.env
6. TinyFish API key → Railway + /data/.env
7. Gateway start + ping test
```

---

## Checklist nhanh

- [ ] Đọc [CREDENTIALS-AND-KEYS.md](../CREDENTIALS-AND-KEYS.md)
- [ ] `.env.example` → `.env` local (không commit)
- [ ] Railway Variables đủ 6 key chính
- [ ] `/data/.env` mirror cùng keys
- [ ] `python scripts/verify_supabase.py` pass

---

## Next

- Chưa xong factory Step 1–3 → tiếp [01-project-kickstart-os.md](01-project-kickstart-os.md)
- Đã xong docs → [04-ops-runtime.md](04-ops-runtime.md)
