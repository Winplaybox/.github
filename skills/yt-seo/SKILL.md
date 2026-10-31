---
name: yt-seo
description: >-
  Write the description, tags and search-facing text for a YouTube video,
  aimed at the query a real person types. Use for "write my description",
  "tags", "SEO", "help this video get found", "nobody is finding this".
---
<!-- Adapted from github.com/Jakeschincariol/youtube-agent-skill, MIT License, Copyright (c) 2026 Jake Schincariol -->

# yt-seo

Search is a smaller lever than packaging and a bigger one than people think for evergreen videos.
For a video aimed at the subscriber feed, say so and spend the effort on `/yt-package` instead.

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

## The description

- **The first two lines are the only ones anyone reads.** They show above "...more" and they are
  the search snippet. Say what the video gives them, in the words they would have typed.
- Then the link or the resource, if there is one, so it is above the fold.
- Then chapters (`/yt-chapters` writes them).
- Then the long version: what is covered, who it is for, what it assumes.

## Tags, honestly

Tags are a weak signal and YouTube has said so. Use them for disambiguation - spellings, the tool
names, the abbreviations people actually type - and stop. Fifteen is plenty. A wall of tags is not
a strategy and stuffing unrelated ones is against the terms.

## The query test

Before handing anything over, write the three search queries this video should win, and check the
title and first two description lines contain the words in those queries. If they do not, the
problem is the title, not the description.

## The gate

Nothing here publishes. This skill writes and you publish. Every output ends in a block the user
copies, and the last line of every run is the question: **ship it, or change it?**
