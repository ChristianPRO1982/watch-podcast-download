# watch-podcast-download
General watch on AI topics through the podcast medium. This project is used to download audios and store them automatically. In a second step, another project will consume the audios to make transcriptions and finally make a weekly summary of this watch sent by email. It's necessary for me to separate the projects because the computer used for downloading doesn't necessarily have the capacity to make transcriptions. Summaries will be made via the OpenAI API.

Some translations by Deepl.com

## .ENV format

```
DEBUG=0 # 0: off, 1: on, 2: on with debug messages, 3: on with only SQL queries

RSS_FEEDS=my_json_file.json
```

## json file format

```
[
    {"category": "my_category", "name": "my_name", "rss_feed": "URL"}
]
```
