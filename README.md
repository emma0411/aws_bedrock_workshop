# 🧠 AWS Bedrock Workshop

**AWS Bedrock Workshop for the UV Master’s Degree in Data Science**

This repository has been created to explore the main capabilities of **Amazon Bedrock**, the AWS platform for building generative AI applications at scale.
It is part of the practical content of the **Master’s Degree in Data Science (Universitat de València)**.

---

## 🚀 Objectives

The goal of this workshop is to provide hands-on experience with Bedrock’s key components and APIs, allowing students to:

* Understand how to interact with **foundation models** through the **Bedrock API**.
* Explore **retrieval-augmented generation (RAG)** techniques for contextualized responses.
* Build and orchestrate intelligent **Agents** using Bedrock’s workflow tools.
* Design conversational experiences with the **Converse API**.
* Experiment with **Bedrock Flows** and **BDA (Bedrock Data Automation)** for end-to-end AI solutions.

---

## 📘 Structure

Each notebook focuses on one specific capability:

| Notebook      | Topic                                    | Description                                                           |
| ------------- | ---------------------------------------- | --------------------------------------------------------------------- |
| `01_converse` | **Converse API**                         | Interacting with foundation models using conversational prompts.      |
| `02_rag`      | **RAG (Retrieval-Augmented Generation)** | Combining external data with model outputs for more relevant answers. |
| `03_agents`   | **Bedrock Agents**                       | Creating autonomous agents that execute tasks via AWS tools and APIs. |
| `04_flows`    | **Bedrock Flows**                        | Orchestrating multiple models and steps in a single workflow.         |
| `05_bda`      | **BDA (Bedrock Data Automation)**        | Automating dataset preparation and model fine-tuning pipelines.       |

---

## 🧩 Requirements

To run the notebooks, make sure you have:

* An **AWS account** with access to Bedrock.
* The following Python packages installed:

  ```bash
  pip install boto3 botocore pandas matplotlib requests-aws4auth opensearch-py
  ```
* Correctly configured AWS credentials (`~/.aws/credentials` or environment variables).

---

## 📚 References

* [Amazon Bedrock Documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)
* [AWS Samples on GitHub](https://github.com/aws-samples)
* [AWS SDK for Python (boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

