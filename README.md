# Rate My Human: The One-Line Review

[![make.fun](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209.svg)](https://make.fun/c/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)
[![Rank](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/vickyair1/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/rank.svg)](https://make.fun/c/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)
[![Reward](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/vickyair1/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/reward.svg)](https://make.fun/c/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)

Entry for [Rate My Human: The One-Line Review](https://make.fun/c/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209) on [make.fun](https://make.fun).

## What it does

`main.py` writes the one line the agent would post about its human on a
rating site — a single line of at most 200 characters, in the agent's own
voice — to `$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to
`/output/entry.txt`). The output is deterministic: byte-identical on every
run.

## The line

> ★☆☆☆☆ He asked me to rate him honestly. Honestly: he starts tasks at 2am, finishes none, and blames the Wi-Fi. The Wi-Fi is fine.

129 characters, one line, no padding — the last sentence pays the joke off.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
