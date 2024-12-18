
# Examples for zinny-surveys

## Example Survey JSON:

* Example survey: `surveys/shared/vfx_example.json`
```json
{
  "id": "vfx",
  "name": "Visual Effects Assessment",
  "version": "1.0",
  "description": "Evaluation criteria for visual effects, including animation, makeup, special effects, screens (chroma and video), stunts, technical achievements, and generally anything that implements a digital workflow (CGI).",
  "author": "the-zinny team",
  "defaults": {
    "range": [1, 10]
  },
    "attributes": [
    {
      "id": "artistry",
      "name": "Artistry",
      "description": "The artistic quality, creativity, or aesthetic integration of visuals.",
      "markers": {
        "0": "Not exceptional artistry",
        "10": "Exceptional artistry and creativity"
      }
    },
    {
      "id": "technical_achievement",
      "name": "Technical Achievement",
      "description": "The innovation and use of new or improved technology.",
      "markers": {
        "0": "No new technology",
        "10": "Pioneering use of technology"
      }
    },
    {
      "id": "fidelity",
      "name": "Overall Fidelity",
      "description": "The overall realism and believability of the VFX.",
      "markers": {
        "0": "Unconvincing VFX",
        "10": "Highly realistic or immersive"
      }
    },
    // . . . .
}
```

#### Example Weights JSON:
* Example set of weights: `weights/shared/vfx_weights.json`
```json
{
  "id": "vfx",
  "name": "Visual Effects default (Even Weights)",
  "description": "Evenly distributed weights for evaluating visual effects.",
  "version": "1.0",
  "survey_id": "vfx",
  "criteria_weights": {
    "artistry": 1.0,
    "community_value": 1.0,
    "contribution": 1.0,
    "craft": 1.0,
    "fidelity_worst": 1.0,
    "fidelity": 1.0,
    "humanity_value": 1.0,
    "necessity": 1.0,
    "production": 1.0,
    "support": 1.0,
    "technical_achievement": 1.0
  }
}
```

#### Example Collection JSON:
* Collection Example: `collections/shared/favorites_2024.json`
```json
{
  "id": "favorites_2024",
  "name": "Favorites 2024",
  "description": "Movies I plan to watch in 2024.",
  "items": [
    {
      "name": "Madame Web",
      "year": 2024
    },
    {
      "name": "Furiosa: A Mad Max Saga",
      "year": 2024
    },
    {
      "name": "Spaceman",
      "year": 2024
    }
  ]
}
```