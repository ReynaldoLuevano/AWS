aws ec2 create-launch-template --launch-template-name "launchTemplate" --launch-template-data file://template.json

aws ec2 run-instances --launch-template LaunchTemplateName=launchTemplate