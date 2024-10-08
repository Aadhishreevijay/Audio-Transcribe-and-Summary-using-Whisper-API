# Audio Transcription and Summarization Using Whisper API

This project provides a solution for transcribing and summarizing audio using the OpenAI Whisper API. It includes both frontend and backend components for a complete audio processing application.

## Prerequisites

- **Node.js**: A JavaScript runtime for server-side development. [Download Node.js](https://nodejs.org/)
- **nvm (Node Version Manager)**: A tool to manage multiple Node.js versions. [Install nvm](https://github.com/nvm-sh/nvm#installing-and-updating)
  - Install nvm via the command line (you might need to use the installation script provided in the [nvm repository](https://github.com/nvm-sh/nvm#installing-and-updating)
    ```bash
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash
    ```
  - Install a specific Node.js version:
    ```bash
    nvm install <node_version>
    ```
- **npm (Node Package Manager)**: Comes with Node.js, used to manage project dependencies.

## Project Structure

- **Client:** Frontend React application
  - [Client Repository](https://github.com/Aadhishreevijay/Audio-Transcribe-and-Summary-using-Whisper-API/tree/main/client)

- **Server:** Backend service for handling audio transcription and summarization
  - [Server Repository](https://github.com/Aadhishreevijay/Audio-Transcribe-and-Summary-using-Whisper-API/tree/main/server)

## Getting Started

### Client

1. **Navigate to the Client Directory:**
   ```bash
   cd client
   ```

2. **Install Dependencies:**
   ```bash
   npm install
   ```

3. **Start the Client:**
   ```bash
   npm start
   ```
   Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

### Server

1. **Navigate to the Server Directory:**
   ```bash
   cd server
   ```

2. **Install Dependencies:**
   ```bash
   npm install
   ```

3. **Start the Server:**
   ```bash
   npm start
   ```

## Notes

- **Ensure the Backend is Running:** Before starting the React client, make sure the backend server is up and running. The frontend relies on the backend for audio transcription and summarization.

- **Debugging:** For easier debugging, especially to monitor network requests and responses, it is recommended to install browser extensions:
  - [React Developer Tools for Chrome](https://chrome.google.com/webstore/detail/react-developer-tools/)
  - [React Developer Tools for Firefox](https://addons.mozilla.org/en-US/firefox/addon/react-devtools/)

### Audio Samples

You can use audio samples from [The Podcast Exchange](https://www.thepodcastexchange.ca/audio-samples). 

To download an audio sample, open a new terminal while the backend is running and execute:
```bash
curl -X POST \
  http://localhost:5000/transcribe \
  -H 'Content-Type: application/json' \
  -d '{
    "url": "https://www.thepodcastexchange.ca/s/HSBC_Canada_Announcer_7819_updated.mp3"
  }'
```

## Documentation

- [OpenAI Whisper Audio Integration](https://js.langchain.com/docs/modules/data_connection/document_loaders/integrations/file_loaders/)
- [OpenAI Chat Models Integration](https://js.langchain.com/docs/modules/model_io/models/chat/integrations/openai)
- [Summarization Chain](https://js.langchain.com/docs/modules/chains/popular/summarize)

## Output Example

Here is an example of the output you can expect from the audio transcription and summarization process:

![Audio Transcription and Summarization Output](https://github.com/user-attachments/assets/881d0f80-c2a8-4972-8d01-f7d586eb7984)
