#  What's the skinny on the ciné

Zinny is a tool for rating media, and the surveys here provide for a rubric, allowing meaningful evaluation of consistent criteria across many titles.

## A collection of survey definitions

This repo is a collection of surveys used in [zinny](https://github.com/RyLaney/zinny).  They are published separately to allow for independent use, and to encourage community contributions.

## Motivtion:
It can be hard to compare movies when they cross genres or styles, or have been watched over a long span of time. The idea of a survey came from experience with structured data, a simple way to make data more meaningful. 

There is so much expertise that goes into a movie which can't be captured in a single rating. The surveys here aspire to combine indepentent component ratings into a more meaningful rating.

Surveys define the criteria to be measured, and Weights are the scoring patterns used in the evaluations.

For more information about Zinny, see the [zinny repository](https://github.com/RyLaney/zinny).

## Goals

**Standardization:** Curated surveys and even weights for consistent evaluations.

**Customization:** Surveys are json and therefore easly crerated for any specific use case that is not already represented.  Weights for any given survey can be copied from the template and modified to suit individual needs.

**Community Contributions:** I'm sure I've missed some important criteria, and I'm sure there are many more surveys that could be useful.  Reach out or send a pull request to contribute.

## Definitions

### Surveys
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

#### Repository Structure

```plaintext
surveys/
├── shared/                     # Institutionally approved surveys
│   ├── vfx.json
│   ├── picture.json
│   └── ...
├── community/                    # Community-contributed surveys
└── local/                        # reserved for local surveys
```

#### Example JSON Representation:

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
    . . . .
```

### Weight Presers
**Weights:**
* Define the relative importance of each criterion within a survey.
* Weights refer to a survey and optionlly a version of that survey.
* A survey can be evaluated with numerous weight sets, allowing for different perspectives in different contexts.

#### Repository Structure

```plaintext
weights/                          # Weighting configurations
├── shared/                     # Institutionally approved weights
│   ├── vfx_even_weights.json
│   ├── picture_even_weights.json
│   ├── picture_storyteller.json
│   └── picture_technologist.json
├── community/                    # Community-contributed weights
└── local/                        # reserved for local weights
```

#### Example JSON Representation:
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
## Collections

**Collection:**
* A curated group of homogeneous items, such as titles or surveys.
* Collections are represented as JSON objects with the following fields:
  * **ID:** A unique identifier for the collection (e.g., "favorites_2024").
  * **Name:** A human-readable name for the collection (e.g., "My Favorites").
  * **Description:** An optional description of the collection (e.g., "Movies I plan to watch this year.").
  * **Items:** A list of objects, where each object represents an item in the collection.
    * For **Title Collections**, each item includes:
      - **Name:** The title of the movie or series.
      - **Year:** The release year of the movie or series.

#### Example JSON Representation:
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


## Installation
If you want to contribute, clone the repository:
```bash
git clone https://github.com/RyLaney/zinny-surveys.git
```

If you just need the published surveys, zinny-surveys can be installed with pip: 
```bash
pip install git+https://github.com/RyLaney/zinny-surveys.git
```

Then you can import pkg_resources and look up the paths:
```python
import pkg_resources
import json

def load_json_file(package, resource_path):
    resource = pkg_resources.resource_string(package, resource_path)
    return json.loads(resource)

# Example usage
data = load_json_file('zinny_surveys', 'surveys/shared/example.json')
print(data)
```

## Contributing
See the [CONTRIBUTING.md](CONTRIBUTING.md) file for more details on how to contribute to this repository.