# Changelog

All notable changes to the Student Grade Predictor project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [3.0.0] - 2025-12-12

### Added

- Added Makefile to act as a driver script to rule them all ([Issue #67](https://github.com/jiroamato/student_grade_predictor/issues/67), [PR #78](https://github.com/jiroamato/student_grade_predictor/pull/78))

### Changed (Peer Review Feedback)

The following changes were made in response to peer review feedback tracked in [Issue #68](https://github.com/jiroamato/student_grade_predictor/issues/68) with the peer review submission here [UBC-MDS/data-analysis-review-2025#13](https://github.com/UBC-MDS/data-analysis-review-2025/issues/13).

- **Clarified feature names in Results & Discussion section** - Specified which variables are used in the analysis to improve clarity for readers. ([Issue #69](https://github.com/jiroamato/student_grade_predictor/issues/69), [Commit 723e18d](https://github.com/jiroamato/student_grade_predictor/commit/723e18d22e10f523c008d603f6a08dff2dc3b491))

- **Improved target distribution histogram visualization** - Extended y-axis to 80 to prevent bars from appearing cut off, and changed bars below threshold to a different color to visually highlight class imbalance. Updated `eda.py` script accordingly. ([Issue #70](https://github.com/jiroamato/student_grade_predictor/issues/70), [PR #86](https://github.com/jiroamato/student_grade_predictor/pull/86), [Commit 9819e9c](https://github.com/jiroamato/student_grade_predictor/commit/9819e9c))

- **Fixed passing threshold inconsistency** - Resolved inconsistency where the introduction defined "passing score > 8" while the Results section used "passing grade >= 10". Reconciled threshold definitions throughout the report. ([Issue #71](https://github.com/jiroamato/student_grade_predictor/issues/71), [Commit df1161b](https://github.com/jiroamato/student_grade_predictor/commit/df1161b))

- **Updated CONTRIBUTING.md for Python project** - Removed R-specific references (roxygen comments, .R file extensions) and added Python style guide references including PEP 8 and black formatter standards. ([Issue #73](https://github.com/jiroamato/student_grade_predictor/issues/73), [Commit 5c1c4d3](https://github.com/jiroamato/student_grade_predictor/commit/5c1c4d309c86fafe5201aa30d8aa1972c9a85ca3))

- **Added caption to Table 2** - Added explanatory caption explaining all variables listed in Table 2, and modified output to display only the top 5 coefficients by absolute value. ([Issue #74](https://github.com/jiroamato/student_grade_predictor/issues/74), [PR #86](https://github.com/jiroamato/student_grade_predictor/pull/86), [Commit 9819e9c](https://github.com/jiroamato/student_grade_predictor/commit/9819e9c))

### Fixed (Peer Review Feedback)

- **Removed duplicate fixture in conftest.py** - Removed duplicate `mock_pipeline` fixture where one incorrectly returned a DataFrame. Only the correct mock object definition was retained. ([Issue #72](https://github.com/jiroamato/student_grade_predictor/issues/72), [PR #79](https://github.com/jiroamato/student_grade_predictor/pull/79), [Commit 25b1162](https://github.com/jiroamato/student_grade_predictor/commit/25b1162))

### Changed (TA Feedback - Milestone 1)

The following changes were made in response to TA feedback tracked in [Issue #88](https://github.com/jiroamato/student_grade_predictor/issues/88).

- **Added package versions to environment.yml** - Added version specifications for all Python packages in the environment file to ensure full reproducibility. ([Issue #89](https://github.com/jiroamato/student_grade_predictor/issues/89), [Commit 29c5906](https://github.com/jiroamato/student_grade_predictor/commit/29c5906abefc6697989d4d0919261cd3fbd94409))

- **Improved GitHub Issues utilization** - Adopted GitHub Issues as the primary method of communication for addressing tasks and dividing work items, starting from Milestone 2. ([Issue #90](https://github.com/jiroamato/student_grade_predictor/issues/90), [Milestone 2](https://github.com/jiroamato/student_grade_predictor/milestone/2), [Milestone 3](https://github.com/jiroamato/student_grade_predictor/milestone/3))

### Changed (Enhancement)

- **Added the most optimal point on the hyperparameter tuning plot in `fit_student_predictor.py`**: - For better readability for users, we've added a red dot indicating the most optimal hyperparameter with it's error [Commit c36900a](https://github.com/jiroamato/student_grade_predictor/commit/c36900ae971f44d0f23fdb4a1f8a0fe8c22f453b) and [PR #87](https://github.com/jiroamato/student_grade_predictor/pull/87).
