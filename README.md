# Language Models Chatbot

This repository contains code for a chatbot powered by two language models: OpenAI and Ollama Gemma 2B. The chatbot is designed to engage in conversation on various topics.

## Installation

To install the necessary dependencies, run:

```bash
pip install -r requirements.txt
```

Make sure you have a `.env` file in the project directory containing the required API keys:

```dotenv
LANGCHAIN_API_KEY="lsv2_sk_XXXX"
LANGCHAIN_PROJECT="LLM_Project"
OPENAI_API_KEY="sk-XXXX"
```

Replace `XXXX` with your respective API keys.

## Usage

To run the chatbot using the Ollama Gemma 2B model, execute:

```bash
streamlit run ollama_chat_bot.py
```

And to run the chatbot using the OpenAI model, execute:

```bash
streamlit run open_chat_bot.py
```

The chatbots will then be accessible via a web interface where you can interact with them.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
[![Copy Markdown](https://img.shields.io/badge/Copy-Markdown-blue)](./README.md)
