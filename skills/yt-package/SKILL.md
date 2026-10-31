---
name: yt-package
description: >-
  Write and lint the title and thumbnail for a YouTube video as one pairing,
  checking truncation, duplication and vagueness before publish. Use for
  "title ideas", "what should I call this", "thumbnail text", "my CTR is
  bad", packaging, or any request to rename or repackage an existing video.
---
<!-- Adapted from github.com/Jakeschincariol/youtube-agent-skill, MIT License, Copyright (c) 2026 Jake Schincariol -->

# yt-package

The scripts named below sit in this skill's own folder. Run them with `python3` from that folder (plain Python 3, no dependencies).

The title and the thumbnail are ONE unit. Writing them separately is why most packaging fails: the
thumbnail repeats the title, and half the click surface says the same thing twice.

```bash
python3 title.py --title "..." --thumb "AI RAN IT"
python3 title.py titles.txt            # one per line, ranked
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

## Rules the tool enforces, and why

- **60 characters** is where desktop search truncates, **40** is a mobile home feed. Both are
  reported because they fail differently: a desktop cut loses the tail, a mobile cut can lose the
  subject.
- **The thumbnail must not repeat the title.** Different words, same promise.
- **Three words maximum on the thumbnail.** At feed size a fourth word is a grey smear.
- **A number, a name or a date** beats every adjective available to you.
- **Two all-caps words is the ceiling** before a title reads as spam.

## Write ten, keep two

Generate ten titles, run them all through `title.py`, show the user the top three with their scores
and the specific issue on each. For the winner, write the thumbnail brief: the expression, the
framing, the three words, and what the background has to do to hold contrast at feed size.

## The gate

Nothing here publishes. This skill writes and you publish. Every output ends in a block the user
copies, and the last line of every run is the question: **ship it, or change it?**
