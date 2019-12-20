# MERZBOW

## Installing

TBD

### Dependencies:

See `requirements.txt` in the project root folder.

## The motivation for this project

I like to listen to philosophy/politics/etc lectures while I'm doing work or wasting time. The material is usually interesting and it's not a big deal if I zone out and miss something. It would be nice to be able to gather material like this automatically so I don't have to go looking for more material so often.

## Crawler

Merzbow comes with a YouTube crawler module by default. If you would like you can write your own crawler that is compatible with Merzbow, to collect from other sources, like RSS feeds, audiobook websites, Patreon feeds, whatever you want.

## Queries

Crawlers are given queries (written as JSON objects) which describe how they decide what video and audio files to collect. 

All queries must have a `CRAWLER_TYPE` field that specifies what kind of Crawler is expected to ingest this query.

### YouTube Queries 

The `CRAWLER_TYPE` value for a YouTube crawler is `YOUTUBE`.
Here are the fields belonging to YouTube queries:

- **`search_text`:** (Required) The string to search for on YouTube.
- **`audio_only`:** If `audio_only`== 1, only the audio of the selected videos will be outputted.
- **`search_condition`:** The value is interpreted as a Python expression that evaluates to a Boolean value per video. If the value is false the video is excluded from the selection. The expression has some variables you can make use of:
    - `VIEWS` (The number of views the video has)
    - `LIKES` (The number of likes the video has)
    - `DISLIKES` (The number of dislikes the video has)
    - `SECONDS` (The length of the video in seconds)
    - `SEEN` (Whether YouTube says you've seen the whole video before)
    - `UPLOADER` (The name of the uploader)
    - `DESCRIPTION` (The video description)
    - `TAGS` (The publicly visible tags as a set of strings)
    
Here is an example YouTube query that collects videos from the "zizek" search on YouTube that are longer than 20 minutes, have over 1,000 views, and aren't marked as seen on my account:
```
{
    "search_text" : "zizek",
    "search_condition" : "SEEN and SECONDS > (60*20) and VIEWS > 1000"
}
```

## Potential features

- A GUI
- More downloaders
- A standalone player that keeps track of what's been heard/seen
- A small webapp to be used on a media server, or as an internet audio stream, or something

## License

See `LICENSE` in the project root folder.

## Contributing

TBD
