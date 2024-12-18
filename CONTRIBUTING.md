# Contribution Guidelines for Zinny Surveys

Zinny-surveys is interested in contributions to expand and refine its survey and weights definitions. Follow these guidelines to create high-quality, reusable contributions.

A newr future addtion will be the ability to extend a survey with additional criteria, thus being able to use an extended survey in analysis with the original survey.

## Customizing and Contributing Surveys

### Creating a New Survey
Surveys define the criteria for evaluating media. To create one:
- Include the following fields:
  - **id**: Unique survey identifier.
  - **name**: Human-readable name.
  - **version**: Use semantic versioning (e.g., `1.0`).
  - **description**: Purpose of the survey.
  - **extends** (optional): ID of the survey this one extends.
  - **defaults**: Default scoring values (e.g., `range`).
  - **criteria**: A list of measurable criteria with:
    - **id**: Unique identifier for each criterion.
    - **name**: Criterion's name.
    - **description**: Explanation of what is being measured.
    - **markers** (optional): Specific value labels.
    - **range** (optional): Overrides the survey default range.

#### Example Template
```json
{
  "id": "example",
  "name": "Example Survey",
  "version": "1.0",
  "description": "An example survey for contributing.",
  "defaults": { "range": [1, 10] },
  "criteria": [
    {
      "id": "example_criterion",
      "name": "Example Criterion",
      "description": "An example measurable factor.",
      "range": [-3, 5],
      "markers": { "-3": "Substandard", "1": "Typical", "5": "Excellent" }
    }
  ]
}
```

### Creating Custom Weights
Weights adjust the importance of each criterion in a survey:
- Include the following fields:
  - **id**: Identifier for the weights file.
  - **name**: Name of the weights.
  - **description**: Purpose of the weighting.
  - **version**: Version of the weights file.
  - **survey_id**: The related survey.
  - **criteria_weights**: Map criterion ids to weight values.

#### Example Template
```json
{
  "id": "example_weights",
  "name": "Custom Weights Example",
  "description": "An example of custom weights for a survey.",
  "version": "1.0",
  "survey_id": "example",
  "criteria_weights": { "example_criterion": 1.5 }
}
```

## Submitting a Contribution
1. **Fork the Repository**: Fork `zinny-surveys`.
2. **Add Files**:
   - Place surveys in `surveys/community/`.
   - Place weights in `weights/community/`.
3. **Validate Your Files**:
   - Use tools like `jsonlint` to ensure valid JSON.
4. **Submit a Pull Request**:
   - Explain your contribution and its purpose.
   - Ensure the files adhere to naming conventions and guidelines.

By following these guidelines, your contributions help ensure high-quality, reusable surveys and weights that benefit the Zinny community.
