# Python Project Template

A well-structured Python project template with modern development practices and tools. This template provides a solid foundation for building Python applications with proper configuration management, logging, and environment setup.

## Features

- 🏗️ **Clean Architecture**: Organized project structure with separation of concerns
- ⚙️ **Configuration Management**: Environment-based configuration using Pydantic Settings
- 📝 **Logging**: Integrated logging with Logfire
- 🔄 **Async Support**: Built-in asyncio support for asynchronous operations
- 🌍 **Environment Variables**: Secure configuration through `.env` files
- 📦 **Package Management**: Uses uv for fast package installation
- 🐍 **Virtual Environment**: Automated conda environment setup
- 🔌 **API Ready**: Pre-configured for multiple AI/ML API integrations

## Project Structure

```
python-template/
├── src/
│   ├── app.py              # Main application class
│   ├── main.py             # Application entry point
│   ├── config/             # Configuration management
│   │   ├── __init__.py
│   │   └── Config.py       # Pydantic settings configuration
│   ├── models/             # Data models and schemas
│   │   └── __init__.py
│   └── utils/              # Utility functions and helpers
│       └── __init__.py
├── .env.example            # Environment variables template
├── .gitignore              # Git ignore rules
├── requirements.txt        # Python dependencies
├── venv.sh                 # Environment setup script
└── README.md              # This file
```

## Quick Start

### Prerequisites

- [Conda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/)
- [UV](https://github.com/astral-sh/uv) (for faster package installation)

### Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd python-template
   ```

2. **Create and activate virtual environment:**
   ```bash
   # Make the script executable
   chmod +x venv.sh
   
   # Run the environment setup script
   ./venv.sh
   ```

3. **Configure environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your actual API keys and configuration
   ```

4. **Run the application:**
   ```bash
   python src/main.py
   ```


## Dependencies

The project includes the following main dependencies:

- **pydantic-settings**: Configuration management with validation
- **python-dotenv**: Environment variable loading from `.env` files
- **logfire**: Modern logging and observability


## License

This project is open source and available under the [MIT License](LICENSE).
