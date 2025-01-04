# Setup Instructions for zinny-surveys

Zinny-surveys is a standalone repository containing predefined surveys and weights for structured media evaluations. It serves as a foundational component for other Zinny projects but can also be used independently.

## Installation

To install `zinny-surveys`, you can either clone the repository for development purposes or install it as a package.

### Clone the Repository
1. Clone the repository:
   ```bash
   git clone https://github.com/RyLaney/zinny-surveys.git
   ```

2. Optionally, create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Install as a Package
If you only need the published surveys:
   ```bash
   pip install zinny-surveys
   # or from the repository
   pip install git+https://github.com/RyLaney/zinny-surveys.git
   ```

## Usage

The `zinny-surveys` package allows you to access surveys and weights programmatically:
   ```python
   from zinny_surveys import load_survey, list_files

   surveys = list_files("surveys", "shared")
   print(surveys)
   ```

For detailed usage, see the [Functions.md](docs/Functions.md) file.

Example JSON is in the [Examples.md](docs/Examples.md) file.
