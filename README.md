# A collection of survey definitions for evaluating media

This is zinny's surveys repository, a centralized location for surveys and weights used in evaluating media (e.g., films, TV, streaming series). 

## Motivtion:
Zinny is a tool for rating media, and the structured definitions here provide for a rubric and allow meaningful evaluation of criteria across many titles and users. 

Weights are the scoring patterns used in the evaluations. As separate definitions, they allow for adjusting the importance of criteria for each user or use case.

It provides:
* **Surveys:** Structured definitions of evaluation criteria for rating and analyses.
* **Weights:** Versioned scoring patterns to adjust the importance of criteria.
* **Community Contributions:** A space for sharing user-defined surveys and weights.

For more information about Zinny, see the [Zinny repository](https://github.com/RyLaney/zinny).

## Goals

**Standardization:** Offer officially curated surveys for consistent evaluations.

**Customization:** Allow users to define their own surveys and weights for specific use cases.

**Community Contributions:** Facilitate sharing and improvement of evaluation standards.

## Terms and Definitions
**Survey:** A predefined set of criteria for evaluating a media title. Each survey includes:
* **Metadata:** Describes the survey's purpose, version, author, and related details.
* **Criteria:** Individual measures with attributes such as range and descriptions.

**Criteria:**
* A measurable attribute or factor within a survey.
* Defined by:
  * **ID:** A unique identifier (e.g., "artistry").
  * **Name:** A human-readable name (e.g., "Artistry").
  * **Description:** Explanation of what is being measured.
  * **Range:** Valid scoring range (e.g., [0,10]).
  * **Value Labels:** Descriptions for specific values (e.g., 0: "No quality", 10: "best quality").

**Weights:**
* Define the relative importance of each criterion within a survey.
* Weights refer to a survey
* A survey can be evaluated with numerous weight sets, allowing for different perspectives in different contexts.


## Repository Structure

```plaintext
surveys/
├── official/                     # Institutionally approved surveys
│   ├── feature_vfx.json
│   ├── general_audience.json
│   └── ...
├── community/                    # Community-contributed surveys
└── private/                    # allocated for local surveys

weights/                      # Weighting configurations
├── official/                 # Institutionally approved weights
│   ├── vfx_weights.json
│   └── audience_weights.json
├── community/                # Community-contributed weights
└── private/                    # allocated for local weight configurations
```

## Examples

* Survey Example: `surveys/official/feature_vfx.json`
```json
{
  "id": "vfx",
  "name": "Visual Effects Assessment",
  "version": "1.0",
  "description": "Evaluation criteria for visual effects, including animation .",
  "author": "the-zinny team",
  "defaults": {
    "range": [1, 10]
  },
    "attributes": [
    {
      "id": "artistry",
      "name": "Artistry",
      "description": "The artistic quality, creativity, or aesthetic integration of visuals.",
      "keyframes": {
        "0": "Not exceptional artistry",
        "10": "Exceptional artistry and creativity"
      }
    },
    {
      "id": "technical_achievement",
      "name": "Technical Achievement",
      "description": "The innovation and use of new or improved technology.",
      "keyframes": {
        "0": "No new technology",
        "10": "Pioneering use of technology"
      }
    },
    {
      "id": "fidelity",
      "name": "Overall Fidelity",
      "description": "The overall realism and believability of the VFX.",
      "keyframes": {
        "0": "Unconvincing VFX",
        "10": "Highly realistic or immersive"
      }
    },
    . . . .
```

* Weighting Example: `weights/official/vfx_weights.json`
```json
{
  "id": "vfx",
  "name": "Visual Effects default (Even Weights)",
  "description": "Evenly distributed weights for evaluating visual effects.",
  "version": "1.0",
  "survey_id": "visual_effects:1.0",
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

## Contributing
See the [CONTRIBUTING.md](CONTRIBUTING.md) file for details on how to contribute to this repository.