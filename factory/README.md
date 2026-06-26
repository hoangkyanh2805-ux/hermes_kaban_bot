# Factory Workflow — Từ ý tưởng video → dự án Hermes Kanban

Quy trình meta dùng để **tái tạo** pipeline kiểu Derek Cheung (hoặc niche khác) từ đầu.

**Instance mẫu:** repo này (`hermes_kaban_bot`) — forex/gold signals.

---

## Bắt đầu ở đâu?

| Bạn đang ở | Đọc |
|------------|-----|
| Có video / idea thô | [WORKFLOW.md](WORKFLOW.md) → Step 0 |
| **Cần lấy API / điền key** | **[../ops/CREDENTIALS-AND-KEYS.md](../ops/CREDENTIALS-AND-KEYS.md)** |
| Sẵn sàng chạy 3 skill | [steps/](steps/) |
| Đã xong Step 1–3, cần deploy | [../ops/OPS-BUNDLER.md](../ops/OPS-BUNDLER.md) |
| Clone sang niche mới | [../ops/clone-checklist.md](../ops/clone-checklist.md) |

---

## Cấu trúc folder

```
factory/
├── README.md                 ← bạn đang đây
├── WORKFLOW.md               ← sơ đồ end-to-end
├── SKILL-MAP.md              ← skill nào khi nào
├── ARTIFACT-MAP.md           ← Step → file trong repo
└── steps/
    ├── 00-idea-to-brief.md
    ├── 00b-credentials-and-keys.md   ← API, Supabase, Railway keys
    ├── 01-project-kickstart-os.md
    ├── 02-agent-os-designer.md
    ├── 03-knowledge-asset-factory.md
    └── 04-ops-runtime.md
```

---

## 3 skill Codex/Cursor

| Skill | Dùng khi |
|-------|----------|
| `project-kickstart-os` | Idea mơ hồ, video YouTube, bắt đầu dự án từ 0 |
| `agent-os-designer` | Thiết kế agent loop, permission, Kanban, DB ownership |
| `knowledge-asset-factory` | Chuyển OS thành skills, SOP, prompts, checklists |

Chi tiết: [SKILL-MAP.md](SKILL-MAP.md)

---

## Nguyên tắc

1. **Docs trước, code sau** — Step 1–3 không implementation
2. **Hermes native Kanban** — không custom orchestrator
3. **OPS sau factory** — Railway, Supabase, cron = phase riêng
4. **Clone được** — OPS Bundler cho dự án thứ 2, 3…
