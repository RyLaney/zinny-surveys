with open("/mnt/data/CONTRIBUTING.md", "w") as file:
### Customization and Contribution Guidelines

#### **Making Your Own Survey**
- **Keys and Structure**:
  - Each survey must include:
    - `id`: Unique identifier for the survey.
    - `name`: Human-readable name.
    - `version`: Semantic versioning (e.g., `1.0`).
    - `description`: Brief explanation of the survey's purpose.
    - `defaults`: Default values such as scoring `range` for each criterion.
    - `criteria`: List of measurable criteria with:
      - `id`: Unique identifier for the criterion.
      - `name`: Criterion's human-readable name.
      - `description`: What the criterion evaluates.
      - `keyframes` (optional): Mappings of specific values to descriptions.
- **Example Template**:
```json
{
  "id": "example",
  "name": "Example Survey",
  "version": "1.0",
  "description": "An example survey for contributing.",
  "defaults": {
    "range": [1, 10]
  },
  "criteria": [
    {
      "id": "example_criterion",
      "name": "Example Criterion",
      "description": "An example measurable factor.",
      "keyframes": {
        "1": "Poor",
        "10": "Excellent"
      }
    }
  ]
}
```
#### **Making Your Own Weights**
- Purpose: A weights file adjusts the relative importance of each criterion in a survey.
- File Naming Conventions:
    - Format: `<survey_id>_<descriptive_token>.json`
    - Examples: 
      - `example_default_weights.json`
      - `example_best_perspective.json`
- Keys and Structure:
    - Each weights file must include:
      - `id`: Versioned survey identifier (e.g., example_survey:1.0).
      - `name`: Human-readable name for the weights file.
      - `description`: Brief explanation of the weighting purpose.
      - `version`: Version of the weights file.
      - `survey_id`: Link to the related survey (e.g., example_survey:1.0).
      - `criteria_weights`: Object mapping criterion id to its weight value.
Example Template:
```json
{
  "id": "example_survey:1.0",
  "name": "Custom Weights Example",
  "description": "An example of custom weights for a survey.",
  "version": "1.0",
  "survey_id": "example_survey:1.0",
  "criteria_weights": {
    "example_criterion": 1.5
  }
}
```
#### **Contributing a Survey or Weights**
1. Fork the Repository: Create a fork of the zinny-surveys repository.
1. Add Your File(s):
   - Place new surveys in surveys/community/.
   - Place new weights in weights/community/.
1. Test Your Contribution:
   - Ensure the JSON structure is valid.
   - Use tools like jsonlint to validate.
1. Create a Pull Request (PR):
   - Provide a brief explanation of your contribution.
   - Follow file naming conventions and JSON guidelines.
   - Include examples or notes if needed.
#### **General Guidelines**
- Keep survey id and criteria consistent across related surveys to ensure compatibility.
- Use clear, descriptive names for criteria and weights.
- Consistency is key in survey design, so avoid duplicating values in existing surveys unless improving, consolidating, or extending them for specific purposes.
- Updates to existing surveys should increment the version field using semantic versioning.

#
By following these guidelines, you help ensure high-quality, reusable contributions that benefit all users of the zinny-surveys repository. Thank you for your interest in contributing!
