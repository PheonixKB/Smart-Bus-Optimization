# AI Coding Assistant Guidelines

## Code Style Rules

- Follow PEP 8 for Python code formatting
- Use descriptive variable and function names
- Maximum line length: 88 characters (Black formatter default)
- Use type hints for all function signatures
- Import sections: standard library, third-party, local (separated by blank lines)
- Docstrings: Use Google style docstrings for all public functions and classes
- Constants: UPPER_SNAKE_CASE
- Classes: PascalCase
- Functions and variables: snake_case

## Build Commands

- Install dependencies: `pip install -r requirements.txt`
- Run tests: `pytest tests/ -v`
- Run linting: `flake8 src/`
- Format code: `black src/`
- Type checking: `mypy src/`
- Start development server: `uvicorn src.api.main:app --reload`

## Architecture Patterns

- Separation of concerns: Data layer, Service layer, API layer
- Dependency injection for services
- Repository pattern for data access
- Factory pattern for model creation
- Observer pattern for event handling
- MVC-like structure for web components

## Testing Workflows

- Unit tests: Test individual functions and classes
- Integration tests: Test API endpoints and database interactions
- Fixtures: Use pytest fixtures for test data setup
- Mocking: Use unittest.mock for external dependencies
- Coverage: Aim for >80% code coverage
- Test files: Place tests in `tests/` directory mirroring source structure

## Project Structure

```
Smart-Bus-Optimization/
├── data/                 # Data files (raw, cleaned, predictions, etc.)
├── models/               # Trained ML models
├── src/                  # Source code
│   ├── api/              # FastAPI endpoints
│   ├── core/             # Core business logic
│   ├── data/             # Data processing and database models
│   ├── ml/               # Machine learning components
│   ├── optimization/     # Route optimization algorithms
│   └── utils/            # Utility functions
├── tests/                # Test files
├── docs/                 # Documentation
├── requirements.txt      # Python dependencies
├── PLAN.md               # Product roadmap
└── README.md             # Project overview
```

## Development Workflow

1. Create feature branch from `dev`
2. Write code following style guidelines
3. Write tests for new functionality
4. Run local tests and linting
5. Commit changes with descriptive messages
6. Push branch and create pull request
7. Code review by team member
8. Merge to `dev` after approval