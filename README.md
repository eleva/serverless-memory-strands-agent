# 🧵 Serverless `Memory Strands Agent`
This is a simple serverless agent built with `Strands Agents SDK` using `mem0_memory` tool to persist context across different calls.

## ⚙️ Prerequisites
- [Python](https://www.python.org/downloads/) (v3.12 or later) (for the Python Lambda function)
- [Node.js](https://nodejs.org/en/download/) (v20 or later)
- [Serverless Framework](https://www.serverless.com/framework/docs/getting-started/) (v3 or later)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) (v2 or later)
- [AWS Account](https://aws.amazon.com/free/) (with IAM permissions to deploy Lambda functions)
- [AWS credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html) configured on your machine

## ⚙️ Setup
Run the following commands to set up the project:
```bash
npm install
```

## 🧪 Test the function locally
Use the Serverless Framework to invoke the function locally. You can use the `--data` flag to pass a JSON object with `action`, `user_id` and `content` fields.

Use the following command to store the content for a specific user:
```bash
sls invoke local -f memory --data '{"content": "I like apples and grapefruit, I do not like oranges and bananas","action":"store","user_id":"1"}'
```

Use the following command to list memories for a specific user:
```bash
sls invoke local -f memory --data '{"action":"list","user_id":"1"}'
```

Use the following command to chat with the agent and get a response based on the stored memories for a specific user:
```bash
sls invoke local -f memory --data '{"content":"What fruit do i like?","action":"chat","user_id":"1"}'
```

## 🚀 Deploy on AWS
Make sure you have configured your AWS credentials and have the necessary permissions to deploy Lambda functions.

You can read more about configuring AWS credentials in the [AWS CLI documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)
or use the `aws configure` command to set them up interactively.

You can also use serverless framework to set up your AWS credentials by running:
```bash
sls config credentials --provider aws --key YOUR_AWS_ACCESS_KEY_ID --secret YOUR_AWS_SECRET_ACCESS_KEY
```

Then, run the following command to deploy the function to AWS:
```bash
sls deploy
```

