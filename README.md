# PrivacyBot

## Description

A Discord bot that aims to bring more private communication to your communities.

## Self-Hosting/Setup

PrivacyBot is very easy and quick to get up and running on your server. This guide will help you host PrivacyBot on a Debian or Ubuntu Linux distro.

### Prerequisites

In order to run PrivacyBot you'll need a server with the following:

- Python 3.0 or higher
- The following modules: discord, asyncio, pymongo
- A MongoDB Community Server (For Blackhole, Messages are NEVER logged or stored)
- A Discord bot token
- An IQ of 5 or higher

### Clone

Clone this repository onto your server.

### Config.json

Create a new file in PrivacyBot's directory called "config.json" (case-sensitive). In this file add the following (pseudo-json is marked with <>):

```
{
    "token":"<bot token>",
    "prefix":["<desired prefix>"],
    "mongo_url":"<MongoDB URL>"
}
```

### Run

Go to the PrivacyBot directory and use `python main.py`. 