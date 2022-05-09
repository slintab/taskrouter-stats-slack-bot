# Twilio TaskRouter Statistics for Slack

This repository contains the code for a Slack bot for querying real-time Taskrouter statistics.
The statistics available for querying are listed in the `reports.yml` file.

## Install

Installing the TaskRouter Stats Bot requires a Slack app. You can create one by following the instructions [here](https://api.slack.com/apps). 

***Deploying the bot application***
1. Provide the required configuration variables by editing the `env.list` file. The following variables are required to be set:
   - `SLACK_SIGNING_SECRET=<YOUR_SLACK_APPS_SIGNING_SECRET>` 
   - `SLACK_BOT_TOKEN=<YOUR_SLACK_BOT_TOKEN>`
   - `TWILIO_AUTH_TOKEN=<YOUR_TWILIO_AUTH_TOKEN`
   - `TWILIO_ACCOUNT_SID=<YOUR_TWILIO_ACCOUNT_SID` 
   - `TASKROUTER_WORKSPACE_SID=<YOUR_TWILIO_WORKSPACE_SID` - this is the SID of the workplace from which you want to query statistics from. You can find your Workspace SID by:
     - using the Console, under *TaskRouter -> Workspaces*
     - using the [API](https://www.twilio.com/docs/taskrouter/api/workspace#list-all-workspaces)
2. Run `docker-compose --env-file env.list up` to deploy the application. By default, it will start on port 3000.

***Configuring your Slack app***
1. Add the following [bot token scopes](https://api.slack.com/scopes) to your app:
   - `channels:history`
   - `chat:write`
   - `commands`
2. [Create a Slack command](https://api.slack.com/interactivity/slash-commands#creating_commands) with the following configuration:
   - **Command**: `/tr-stats`
   - **Request URL**: `https://YOUR_DOMAIN.com:3000/slack/events`
   - **Usage hint**:  `workspace [or taskqueue, worker, workflow, help]` 
3. Enable [interactivity](https://api.slack.com/interactivity/handling#setup) for your Slack app.
   - Set the **Request URL** to: https://YOUR_DOMAIN.com:3000/slack/events

## Usage

To start using the bot, add your app to a channel and enter the `/tr-starts` command.

## Demo

![Bot Screenshot Prompt](images/screenshot_1.png?raw=true)

![Bot Screenshot Results](images/screenshot_2.png?raw=true)




## Maintainer
If you have any questions, do not hesitate to reach out at `hello@slintab.dev`