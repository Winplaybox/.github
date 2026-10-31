---
name: yt-script
description: >-
  Write a YouTube video script from a raw idea - hook options off 21
  formulas, scored, then the full spoken script with the retention beats
  marked. Use whenever the user wants a video script, a hook, an opening
  line, "what should I say", "write my next video", or is about to record
  and does not have the first fifteen seconds yet.
---
<!-- Adapted from github.com/Jakeschincariol/youtube-agent-skill, MIT License, Copyright (c) 2026 Jake Schincariol -->

# yt-script

The scripts named below sit in this skill's own folder. Run them with `python3` from that folder (plain Python 3, no dependencies).

One idea into a script somebody finishes.

Two tools live in this folder and both actually run. Use them. Do not eyeball the hook.

```bash
python3 hookscore.py hooks.txt              # rank your hook options
python3 hookscore.py --hook "one line"      # score a single one
```

## Before you write

1. Use the channel's voice profile if one is available: in this conversation, the project files,
   memory, or a `voice.md` the user attached. It says how they talk on camera, the words they never
   use, who they are talking to, and what they will not claim. If the user runs several channels,
   confirm which channel this is for. If no profile exists, ask for **three of their own videos**
   (links, transcripts or captions), infer the voice, and hand back a `voice.md` with these
   sections for them to keep: Who I am talking to / How I actually talk / Words I never use /
   Words I do use / What I will not claim / My format. A script in the wrong voice is worse than
   no script, because they have to read it out loud. Match the user's language (Hindi, Hinglish
   or English) in scripts and replies unless told otherwise.
2. Never invent a number, a result or a source. If a figure would strengthen it and you do not have
   one, ask for it or write the line without it.

## The shape

**The first 15 seconds is the whole job.** It does three things or the video leaks: confirm the
click the title promised, open a question the viewer cannot close, and prove the payoff exists.

1. **Hook.** Write FIVE against [the 21 formulas](hooks.json), run them through `hookscore.py`,
   keep the top two, and show the user both with their scores. Never hand over one hook.
2. **The turn** (0:15-0:45). Say what the video is going to do, in one sentence, and start doing it.
   No channel intro, no "before we get started", no subscribe pitch. Those are the single most
   common cause of the 0:30 cliff.
3. **The body.** One idea per beat. Mark each beat with what is ON SCREEN, not just what is said -
   a talking head with nothing to look at is a podcast.
4. **The payoff.** Deliver the thing the hook promised, explicitly, and say that you are delivering
   it: "that is the prompt, it is in the description".
5. **The close.** One ask. Not three.

## What to hand back

- the two best hooks with their scored panels
- the script, beat by beat, with `[ON SCREEN: ...]` on every beat
- the runtime estimate at 150 words per minute
- one line naming which formula the winning hook used and why it fits this idea

## The gate

Nothing here publishes. This skill writes and you publish. Every output ends in a block the user
copies, and the last line of every run is the question: **ship it, or change it?**
