import aws_cdk as core
import aws_cdk.assertions as assertions

from application1.application1_stack import Application1Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in application1/application1_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Application1Stack(app, "application1")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
