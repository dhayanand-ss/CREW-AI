# CrewAI Project

This project demonstrates the use of CrewAI agents for automated content creation and movie Q&A functionality.

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd crew-ai
   ```

2. **Install dependencies**
   ```bash
   pip install crewai crewai-tools python-dotenv
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env file with your actual API keys
   ```

4. **Run the CrewAI agents**
   ```bash
   python CREWAIAGENTS.py
   ```

5. **Run the movie Q&A demo**
   ```bash
   python movie_qa_demo.py
   ```

## 📁 Project Structure

- `CREWAIAGENTS.py` - Main CrewAI script for blog content generation
- `movie_qa_demo.py` - Movie Q&A agent demonstration
- `INSTALLATION_GUIDE.md` - Detailed installation and setup guide
- `.env.example` - Template for environment variables
- `.gitignore` - Git ignore rules for sensitive files

## 🔐 Security

- Never commit your `.env` file to version control
- All API keys and sensitive information are stored in environment variables
- Use `.env.example` as a template for your local configuration

## 📚 Documentation

See `INSTALLATION_GUIDE.md` for detailed setup instructions and troubleshooting.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Ensure no sensitive information is committed
5. Submit a pull request

## 📄 License

This project is for educational and demonstration purposes.
