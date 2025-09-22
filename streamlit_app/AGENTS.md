# AGENTS.md - Guide for AI Coding Assistants

## Build/Run Commands
- **Run app**: `streamlit run app.py`
- **Install dependencies**: `pip install streamlit pandas numpy` (no requirements.txt found)
- **Activate venv**: `source venv/bin/activate` (venv exists in workspace)

## Architecture & Structure
- **Single-file Streamlit app** with dashboard-style layout
- **Main file**: `app.py` - contains entire application logic
- **Dependencies**: streamlit, pandas, numpy for data visualization and UI
- **No database** - uses generated random data via numpy

## Code Style & Conventions
- **Imports**: Standard library first, then third-party (streamlit, pandas, numpy)
- **Comments**: Use `# Comment` for section headers and explanations
- **Streamlit patterns**: Use sidebar for controls, main area for content display
- **Variable naming**: snake_case (e.g., `user_input`, `rows`)
- **String formatting**: Use f-strings for dynamic content (e.g., `f"You typed: {user_input}"`)
- **UI elements**: Use emojis in headers for visual appeal (📊, 🔢, 📈, 🎉)
- **Layout**: Group related functionality with subheaders
- **Data handling**: Use pandas DataFrames for tabular data, numpy for random generation
