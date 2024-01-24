---
title: "Event Transformation"
linkTitle: "Event Transformation"
tags: [quickstart, connect, register] 
categories: ["Knowledge Base"]
description: >-
    Event Transformation using Event Transformers.
---



Events are the powerful concept at the center of the FX Platform. The Event Transformer based Services offer a simple and configurable approach to transforming the payload of events prior to reemiiting events. These are useful for targeting services which expect different payloads.

TRANSFORMER

Example

```json
{
  "some_transformer_event": {
    "conditions": [
      {
        "key": "tkey",
        "val": 9,
        "op": "not_equal"
      }
    ],
    "emit_events": [
      {
        "event_type": "transformed_trigger_event",
        "topic": "ferris.events",
        "transform": [
          {
            "key": "tkey",
            "val": "4",
            "type": "replace"
          },
          {
            "key": "tkey",
            "val": "thekey",
            "type": "rename"
          }
        ]
      }
    ]
  }
}
```

`some_transformer_event` - name of the event to apply rules/transforms <br>
`conditions` - conditions to be met for transformation to occur. If multipe conditions are defined `and` operator is used, all of them must be met to proceed.<br>
`conditions.key` - name of the key to be checked<br>
`conditions.val` - value that should match criteria<br>
`op` - operator that will be used to match criteria, possible options `equal`, `not_equal`, `in` (in array), `not_in` <br>
<br>
`emit_events` - list of event objects with transformation def<br>
`event_type` - type of the event that will be emitted<br>
`topic` - name of destination topic for event<br>
`transform` - list of keys that should be transformed
`transform.key` - name of the key that should be transformed<br>
`transform.type` - type of transformation that should be applied: `replace` (will replace value of the key with one provided), `rename` (will rename the key with one provided in val), `remove` (will remove key), `add` (will add new key/val)<br>
`transform.val` - value to be applied (works with `transform.type`)