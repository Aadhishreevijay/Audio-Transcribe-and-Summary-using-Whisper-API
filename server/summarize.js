// import
import { OpenAIWhisperAudio } from "@langchain/community/document_loaders/fs/openai_whisper_audio";
import { OpenAI } from "@langchain/openai";
import { loadSummarizationChain } from "langchain/chains";
import { RecursiveCharacterTextSplitter } from "langchain/text_splitter";

import dotenv from "dotenv";
import { fileURLToPath } from "url";
import path, { dirname } from "path";
import download from "./handler.js";

dotenv.config();

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const filePath = path.join(__dirname, "media", "audio.mp3");

const model = new OpenAI({ temperature: 0 });
// OpenAI  models
const loader = new OpenAIWhisperAudio(filePath);
const textSplitter = new RecursiveCharacterTextSplitter({ chunkSize: 1000 });
const chain = loadSummarizationChain(model, { type: "map_reduce" });

// OpenAI Whisper Audio

export default async (req, res) => {
  await download(req.body.url);
  console.log("Transcribing audio...");
  const transcript = await loader.load();
  const docs = await textSplitter.createDocuments([transcript[0].pageContent]);
  const response = await chain.invoke({
    input_documents: docs,

  });
  return res.status(200).send({
    transcript: transcript[0].pageContent,
    summary: response.text,
  });

};
