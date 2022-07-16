# Notes

## Notes on Formatting

### Introduction

These are just work-in-progress notes on how to convey timeline events in a machine-readable way that we can both publish and use to drive the interative timeline viewer (which will eventually allow filtering, display of dates relative to other base dates, and more).

### Prior Art

As we find other examples of modelling timelines, I'll include them here.

### Format

I'm going to design stuff using YAML but we can switch to JSON or XML at any point without these efforts being wasted. We could, for example drive the interative timeline viewer with JSON generated from the easier-to-edit YAML. All this is subject to change.

I propose that multiple files always be supported. This way it's easy to include or exclude different sets of events just by selecting different files to import and serve up to the viewer (which isn't the same as filtering). This also allows competing versions to be handled (e.g. different versions of the Annals of Valinor or Beleriand).

Because the physical files may be used to organize information from difference sources or covering different types of events, it might be worth a file supporting common properties to be shared by all events in that file so redundancy can be reduced. In other words

```yaml
common:
  source: LR B.SA
events:
  -
    date: SA.1
    description: Grey Havens founded
  -
    date: SA.1
    description: Lindon founded
  -
    date: SA.32
    description: The Edain reach Númenor
```

as opposed to

```yaml
events:
  -
    date: SA.1
    description: Grey Havens founded
    source: LR B.SA
  -
    date: SA.1
    description: Lindon founded
    source: LR B.SA
  -
    date: SA.32
    description: The Edain reach Númenor
    source: LR B.SA
```

although the latter would mean exactly the same thing.

So I tentative propose that the top level of a file consists of the properties:

- `common`
- `events`

where `common` is an object (in the JSON sense) of properties to be duplicated on each event and `events` is a list of events.

Each event can then consist of properties:

- `date`
- `description`
- `source`

as well as more to be tentatively proposed below. `description` can just be English text (although we could eventually localize) and `source` can be our citation system.

#### Dates

`date` can just take a single date string (see arda date library)

```yaml
date: SA.32
```

or it can be an object.

Approximate dates are represented as follows:

```yaml
date:
  circa: SA.40
```

and ranges:

```yaml
date:
  start: SA.3262
  end: SA.3310
```

Eventually we can support terminus post quem and terminus ante quem dates.

#### Categories

I think to get started, we should just add a property `categories` to enable basic tag-like filtering. Initially tags could be people, places, types of events.

For example:

```yaml
  -
    date: SA.442
    description: Death of Elros Tar-Minyatur.
    categories:
      - Elros
      - deaths
      - Númenorean rulers
  -
    date: SA.500
    description: Sauron beings to stir again in Middle-earth.
    categories:
      - Sauron
```

Eventually I want to make those categories more richly structured and tied to our authority lists for people and places. But I think we can get started without it.

But looking ahead, I can imagine having event types with type-specific properties:

```yaml
  -
    date: SA.442
    type: death
    person: _ID for Elros_
```

or similar.

If our date format handles ranges, what's the difference between separate birth / death events and an event covering someone's lifespan. Perhaps an even better example would be a ruler's regnal period where the inception would normally be indicated but the end would only be implied by the next ruler's acension unless we used ranges.

**TODO** to discuss the above!
