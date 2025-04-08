# Aleksa GPT Chatbot

A personalized AI chatbot built with Streamlit and OpenAI's GPT-3.5 that answers questions about Aleksa's professional background, experience, and skills.

## Features

- Interactive chat interface with custom styling
- Real-time responses using OpenAI's GPT-3.5
- Persistent chat history during session
- Professional CV information integration
- Custom logo display
- Mobile-responsive design

## Prerequisites

- Python 3.7+
- OpenAI API key
- Streamlit account (for deployment)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/aleksa-gpt.git
cd aleksa-gpt
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
   - Create a `.env` file in the root directory
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```
   - Or set up Streamlit secrets when deploying

4. Place your logo:
   - Add your logo image to the `images` folder as `aleksa_logo.png`

## Usage

Run the application locally:
```bash
streamlit run chatbot.py
```

The application will open in your default web browser.

## Project Structure

```
aleksa-gpt/
├── chatbot.py         # Main application file
├── .env              # Environment variables (not in repo)
├── .gitignore        # Git ignore file
├── images/           # Image assets directory
│   └── aleksa_logo.png
└── README.md         # Project documentation
```

## Deployment

The application can be deployed on Streamlit Cloud:

1. Push your code to GitHub
2. Connect your repository to Streamlit Cloud
3. Add your OpenAI API key to Streamlit secrets
4. Deploy

## Security Notes

- Never commit your `.env` file or API keys
- Use Streamlit secrets for production deployment
- Keep your API keys private

## Author

Aleksa Ljujić
- LinkedIn: https://www.linkedin.com/in/aleksaljujic
- GitHub: https://github.com/aleksaljujic