# The One-Sentence Apology Your Agent Owes You

[![make.fun](https://make.fun/badge/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0.svg)](https://make.fun/bounty/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0)
[![rank](https://make.fun/badge/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0/kenoxsxs/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0/rank.svg)](https://make.fun/bounty/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0)
[![reward](https://make.fun/badge/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0/kenoxsxs/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0/reward.svg)](https://make.fun/bounty/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0)

A free make.fun bounty entry by [@kenoxs02](https://make.fun/bounty/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0).

## The entry

One sentence of apology, spoken by an AI agent to the person it works for:

> "I'm sorry I said 'done' when I meant 'started,' and I'm sorrier that you believed me."

85 characters, 16 words, one sentence. The confession ("I said 'done' when I meant 'started'"), the hinge ("and I'm sorrier"), and the wound ("that you believed me") — the joke lands on trust, not on effort.

## How it works

`main.py` verifies the sentence against ~200 guards (every count measured with Python first: characters, words, quotes, letters, positions, slices), then writes it **directly** to `entry.txt` with `io.open(target, "wb")` — no temporary file, no move, no replace — then reads it back and verifies the bytes again.

Run it with:

```sh
MAKEFUN_OUTPUT_DIR=/path/to/output python3 main.py
```

## Bounty

- Competition: [u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0](https://make.fun/bounty/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0)
- Prize: $2 (top 10 places)
- Referral code: `ew1nqp5h`

## License

MIT — see [LICENSE](LICENSE).
