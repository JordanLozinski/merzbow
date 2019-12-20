# MERZBOW

## Installing

TBD

## Contributing

TBD

## The motivation for this project

I like to listen to philosophy/politics/etc lectures while I'm doing work or wasting time. The material is usually interesting and it's not a big deal if I zone out and miss something. It would be nice to be able to gather material like this automatically so I don't have to go looking for more material so often.

## Crawler

Merzbow comes with a YouTube crawler module by default. If you would like you can write your own crawler that is compatible with Merzbow, to collect from other sources, like RSS feeds, audiobook websites, Patreon feeds, whatever you want.

## Queries

Crawlers are given queries (written as JSON objects) which describe how they decide what video and audio files to collect. 

### YouTube Queries

Here are the fields belonging to YouTube queries:

- **`search_text`:** (Required) The string to search for on YouTube.
- **`audio_only`:** If `audio_only`== 1, only the audio of the selected videos will be outputted.
- **`search_condition`:** The value is interpreted as a Python expression that evaluates to a Boolean value per video. If the value is false the video is excluded from the selection. The expression has some variables you can make use of:
    - VIEWS (The number of views the video has)
    - LIKES (The number of likes the video has)
    - DISLIKES (The number of dislikes the video has)
    - SECONDS (The length of the video in seconds)
    - SEEN (Whether YouTube says you've seen the whole video before)
    - UPLOADER (The name of the uploader)
    - DESCRIPTION (The video description)
    - TAGS (The publicly visible tags as a set of strings)
    
Here is an example YouTube query that searches for videos from the "zizek" search on YouTube that are longer than 20 minutes, have over 1,000 views, and aren't marked as seen on my account:
```
{
    "search_text" : "zizek",
    "search_condition" : "SEEN and SECONDS > (60*20) and VIEWS > 1000"
}
```

## Potential features

Features I would very much like to write:

- A GUI of some kind
- More downloaders

## License

See `LICENSE` in the project root folder.
