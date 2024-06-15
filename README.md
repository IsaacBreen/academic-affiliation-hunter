I'm interested in finding a PhD supervisor in robotics in Australia (where I live and can more easily get a scholarship) who has close ties to academic(s) in a prestigious overseas institution like CMU, MIT, Stanford, Berkley etc.

I have a dataset of academic publications. There are multiple JSONs in no particular order in files numbered `0.json.gz`, `1.json.gz`, `2.json.gz` etc. They each follow the same schema below.

Write code that does the following:

- create a table of academics affiliated with an Australian institution with
	- a name column
	- an affiliation column
	- a score
- loop through all publications for each Australian academic and add 1 to their score every time one of their co-authors is at a target institution. For example, if there are two papers in the dataset:

	- Robots for doing the dishes
		- Hugh Jackman, Australian National University
		- Matt Daemon, Carnegie Mellon University
		- Tom Cruise, Stanford University
	- Robots for lifting boxes
		- Hugh Jackman, Australian National University
		- Tom Cruise, Stanford University

Then the table has one row in it for Hugh Jackman at Australian National University whose score is 3.

Write the full Python code to do this.

- Assume each JSON is in a folder with path `./[Sample Dataset] April 2024 Public Data File from Crossref`.
- Use `gzip` to open the JSON files without extracting them to a local file.
- Define a list of target institutions. Consider an affiliation name to match if it contains any of the target institutions.
- Remove academics with score 0.

```json
{
  "$schema": "http://json-schema.org/schema#", "type": "object", "properties": {
  "items": {
    "type": "array", "items": {
      "type": "object",
      "properties": {
        "DOI": {"type": "string"},
        "reference": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "author": {"type": "string"},
              "year": {"type": "string"},
              "key": {"type": "string"},
              "volume-title": {"type": "string"},
              "first-page": {"type": "string"},
              "volume": {"type": "string"},
              "journal-title": {"type": "string"},
              "DOI": {"type": "string"},
              "doi-asserted-by": {"type": "string"},
              "unstructured": {"type": "string"},
              "article-title": {"type": "string"},
              "issue": {"type": "string"},
              "series-title": {"type": "string"},
              "ISSN": {"type": "string"},
              "issn-type": {"type": "string"}
            },
            "required": ["key"]
          }
        },
        "issued": {
          "type": "object",
          "properties": {"date-parts": {"type": "array", "items": {"type": "array", "items": {"type": "integer"}}}},
          "required": ["date-parts"]
        },
        "prefix": {"type": "string"},
        "author": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "affiliation": {
                "type": "array",
                "items": {"type": "object", "properties": {"name": {"type": "string"}}, "required": ["name"]}
              },
              "given": {"type": "string"},
              "family": {"type": "string"},
              "sequence": {"type": "string"}
            },
            "required": ["affiliation", "family", "given", "sequence"]
          }
        },
        "reference-count": {"type": "integer"},
        "ISSN": {"type": "array", "items": {"type": "string"}},
        "member": {"type": "string"},
        "source": {"type": "string"},
        "score": {"type": "number"},
        "deposited": {
          "type": "object",
          "properties": {
            "timestamp": {"type": "integer"},
            "date-time": {"type": "string"},
            "date-parts": {"type": "array", "items": {"type": "array", "items": {"type": "integer"}}}
          },
          "required": ["date-parts", "date-time", "timestamp"]
        },
        "indexed": {
          "type": "object",
          "properties": {
            "timestamp": {"type": "integer"},
            "date-time": {"type": "string"},
            "date-parts": {"type": "array", "items": {"type": "array", "items": {"type": "integer"}}}
          },
          "required": ["date-parts", "date-time", "timestamp"]
        },
        "issue": {"type": "string"},
        "published-online": {
          "type": "object",
          "properties": {"date-parts": {"type": "array", "items": {"type": "array", "items": {"type": "integer"}}}},
          "required": ["date-parts"]
        },
        "URL": {"type": "string"},
        "is-referenced-by-count": {"type": "integer"},
        "published": {
          "type": "object",
          "properties": {"date-parts": {"type": "array", "items": {"type": "array", "items": {"type": "integer"}}}},
          "required": ["date-parts"]
        },
        "volume": {"type": "string"},
        "issn-type": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {"type": {"type": "string"}, "value": {"type": "string"}},
            "required": ["type", "value"]
          }
        },
        "link": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "URL": {"type": "string"},
              "intended-application": {"type": "string"},
              "content-version": {"type": "string"},
              "content-type": {"type": "string"}
            },
            "required": ["URL", "content-type", "content-version", "intended-application"]
          }
        },
        "published-print": {
          "type": "object",
          "properties": {"date-parts": {"type": "array", "items": {"type": "array", "items": {"type": "integer"}}}},
          "required": ["date-parts"]
        },
        "journal-issue": {
          "type": "object",
          "properties": {
            "issue": {"type": "string"},
            "published-print": {
              "type": "object",
              "properties": {"date-parts": {"type": "array", "items": {"type": "array", "items": {"type": "integer"}}}},
              "required": ["date-parts"]
            },
            "published-online": {
              "type": "object",
              "properties": {"date-parts": {"type": "array", "items": {"type": "array", "items": {"type": "integer"}}}},
              "required": ["date-parts"]
            }
          },
          "required": ["issue"]
        },
        "references-count": {"type": "integer"},
        "short-container-title": {"type": "array", "items": {"type": "string"}},
        "publisher": {"type": "string"},
        "content-domain": {
          "type": "object",
          "properties": {"domain": {"type": "array", "items": {"type": "string"}}, "crossmark-restriction": {"type": "boolean"}},
          "required": ["crossmark-restriction", "domain"]
        },
        "resource": {
          "type": "object",
          "properties": {"primary": {"type": "object", "properties": {"URL": {"type": "string"}}, "required": ["URL"]}},
          "required": ["primary"]
        },
        "language": {"type": "string"},
        "created": {
          "type": "object",
          "properties": {
            "timestamp": {"type": "integer"},
            "date-time": {"type": "string"},
            "date-parts": {"type": "array", "items": {"type": "array", "items": {"type": "integer"}}}
          },
          "required": ["date-parts", "date-time", "timestamp"]
        },
        "type": {"type": "string"},
        "title": {"type": "array", "items": {"type": "string"}},
        "alternative-id": {"type": "array", "items": {"type": "string"}},
        "container-title": {"type": "array", "items": {"type": "string"}},
        "page": {"type": "string"},
        "abstract": {"type": "string"},
        "license": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "delay-in-days": {"type": "integer"},
              "start": {
                "type": "object",
                "properties": {
                  "timestamp": {"type": "integer"},
                  "date-time": {"type": "string"},
                  "date-parts": {"type": "array", "items": {"type": "array", "items": {"type": "integer"}}}
                },
                "required": ["date-parts", "date-time", "timestamp"]
              },
              "content-version": {"type": "string"},
              "URL": {"type": "string"}
            },
            "required": ["URL", "content-version", "delay-in-days", "start"]
          }
        },
        "assertion": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "label": {"type": "string"},
              "group": {
                "type": "object",
                "properties": {"name": {"type": "string"}, "label": {"type": "string"}},
                "required": ["label", "name"]
              },
              "order": {"type": "integer"},
              "value": {"type": "string"},
              "name": {"type": "string"}
            },
            "required": ["group", "label", "name", "order", "value"]
          }
        },
        "update-policy": {"type": "string"},
        "subtitle": {"type": "array", "items": {"type": "string"}},
        "archive": {"type": "array", "items": {"type": "string"}},
        "article-number": {"type": "string"},
        "published-other": {
          "type": "object",
          "properties": {"date-parts": {"type": "array", "items": {"type": "array", "items": {"type": "integer"}}}},
          "required": ["date-parts"]
        }
      },
      "required": [
        "DOI",
        "ISSN",
        "URL",
        "author",
        "container-title",
        "content-domain",
        "created",
        "deposited",
        "indexed",
        "is-referenced-by-count",
        "issn-type",
        "issue",
        "issued",
        "journal-issue",
        "member",
        "prefix",
        "published",
        "publisher",
        "reference-count",
        "references-count",
        "resource",
        "score",
        "source",
        "title",
        "type",
        "volume"
      ]
    }
  }
}, "required": ["items"]
}
```