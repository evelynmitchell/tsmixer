# Product Requirements Document (PRD)

## Project Overview

**Project Name:** TSMixer

**Description:** TSMixer is a PyTorch-based library designed for time series forecasting. It includes various modules and functionalities to handle multivariate time series data, leveraging deep learning techniques for accurate predictions.

**Repository:** [TSMixer GitHub Repository](https://github.com/evelynmitchell/tsmixer)

## Objectives

- Develop a robust and efficient time series forecasting library.
- Ensure the library is easy to use and integrate with existing projects.
- Provide comprehensive documentation and examples to help users get started quickly.
- Implement thorough testing to ensure the reliability and accuracy of the library.

## Features

### Core Features

1. **MixerLayer Module**
   - Implements a mixer layer for time series data.
   - Includes normalization and MLP layers for feature and time mixing.
   - [MixerLayer Class](../tsmixer/tsmixer.py)

2. **TemporalProjection Module**
   - Implements a temporal projection layer.
   - Includes normalization and fully connected layers.
   - [TemporalProjection Class](../tsmixer/tsmixer.py)

3. **Data Loading**
   - Supports loading datasets from various sources.
   - Includes tests to ensure datasets are loaded correctly and contain expected features.
   - [TestDataLoading Class](../tests/test_data_load.py)

### Additional Features

- **Docker Support**
  - Provides a Dockerfile for containerized deployment.
  - [`Dockerfile`](../Dockerfile)

- **Continuous Integration**
  - GitHub Actions workflows for testing and documentation validation.
  - [Documentation Tests Workflow](../.github/workflows/docs_test.yml)
  - [Pull Request Links Workflow](../.github/workflows/pull-request-links.yml)

## Requirements

### Functional Requirements

1. The library should support loading and processing multivariate time series data.
2. The library should provide modules for feature and time mixing.
3. The library should include comprehensive tests to ensure data integrity and module functionality.

### Non-Functional Requirements

1. The library should be easy to install and integrate with existing projects.
2. The library should have clear and comprehensive documentation.
3. The library should be performant and capable of handling large datasets.

## Documentation

- **README.md**
  - Overview of the project.
  - Installation instructions.
  - Basic usage examples.
  - [`README.md`](../README.md)

- **Architecture Documentation**
  - Detailed explanation of the library's architecture and design.
  - architecture.md

- **API Documentation**
  - Detailed documentation of the library's API.
  - index.md

- **Examples and Demos**
  - Practical examples and demos to help users get started.
  - demos.md
  - examples/

## Testing

- Unit tests for all core modules and functionalities.
- Integration tests to ensure the library works as expected in real-world scenarios.
- [`tests`](../tests)

## Timeline

1. **Week 1-2:** Initial setup and core module development.
2. **Week 3-4:** Data loading and processing implementation.
3. **Week 5-6:** Documentation and examples creation.
4. **Week 7-8:** Testing and bug fixing.
5. **Week 9:** Final review and release.

## Contributors

- **Evelyn Mitchell** (Project Lead)
- Additional contributors as listed in the repository.