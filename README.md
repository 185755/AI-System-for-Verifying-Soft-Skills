# AI-System-for-Verifying-Soft-Skills
AI System for Verifying Soft Skills Based on Generative Artificial Intelligence for Task Creation in ACDC Sessions." The goal of this project was to develop a program that would generate tasks for AC/DC sessions.

---
## 📌 Project Overview  
This repository contains the implementation of an AI-powered system designed to assess soft skills in candidates using Large Language Models (LLMs). The system evaluates responses recorded by candidates during **Assessment Center/Development Center (AC/DC)** sessions, automating the evaluation process traditionally performed by human assessors.

## 🎯 Project Goal  
The primary goal of this project is to **develop a system that utilizes LLMs to assess soft skills** based on video responses from candidates. The system transcribes, analyzes, and scores the responses to determine if a candidate demonstrates specific competencies.

## 🛠️ Features  
- 📌 **Automated soft skills assessment** using LLMs  
- 📌 **Transcription of video responses** using WhisperAI  
- 📌 **Comparison with human assessors** for evaluation accuracy  
- 📌 **Performance analysis** using precision, recall, F1-score, and accuracy  
- 📌 **Integration with Google Drive API** for file storage and retrieval  

## 📂 Project Workflow  
1. **Candidate Submission**: The candidate records and submits **three short videos** (max 3 minutes each) answering predefined questions:  
   - Describe a difficult problem you managed to solve.  
   - Describe a situation where your suggestions improved a process.  
   - Describe a situation where you collaborated with others to complete a task.  
2. **File Processing**:  
   - The system downloads video files from **Google Drive** via API.  
   - Converts videos to text using **WhisperAI**.  
3. **Soft Skills Evaluation**:  
   - The transcribed text is analyzed using **LLMs (ChatGPT, Hugging Face models, etc.)**.  
   - Models assign scores based on predefined competency indicators.  
4. **Comparison & Reporting**:  
   - The AI-generated scores are compared with **human assessors' evaluations**.  
   - The system calculates **precision, recall, and F1-score** to measure model accuracy.  
   - Results are saved in an **Excel report** for further analysis.  

## 📊 Performance Evaluation  
The system uses key **machine learning metrics** to assess accuracy:  
- **Precision**: Measures how many predicted positives are actually correct.  
- **Recall**: Measures how many actual positives were correctly identified.  
- **F1-Score**: Harmonic mean of precision and recall.  
- **Accuracy**: Overall correctness of the model’s classification.  

### 🔍 Model Comparison (Mean F1-Scores)  
| Model       | F1-Score |
|------------|----------|
| Llama 70B  | 0.7079   |
| GPT-4o     | 0.7076   |
| Qwen       | 0.7028   |
| MistralAI  | 0.7023   |
| GPT-3.5    | 0.6554   |
| HuggingFace | 0.5663   |
| Llama 3B   | 0.4587   |

## 🚀 Technologies Used  
- **Python** (for data processing and automation)  
- **Google Drive API** (for file handling)  
- **WhisperAI** (for video-to-text transcription)  
- **OpenAI & Hugging Face LLMs** (for text analysis)  
- **Pandas, OpenPyXL** (for report generation)  

## ⚠️ Challenges & Solutions  
- **Running large models locally requires high computational resources** → Used **serverless APIs** instead.  
- **Fine-tuning LLMs requires extensive datasets and computing power** → Used **pre-trained models** via API.  

## 📌 Future Improvements  
- Enhance model accuracy with **fine-tuning on domain-specific datasets**.  
- Implement **multi-language support** for broader applicability.  
- Develop a **user-friendly web interface** for easier access and management.  

## 📜 Acknowledgments  
Developed by **Maciej Dziewit & Paweł Sienkiewicz** under the guidance of **Agnieszka Czapiewska**. Special thanks to **Solution Sp. z o.o.** for providing project support.  

---