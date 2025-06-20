#!/bin/bash
# Set ACCOUNT_NUMBER vairable
export ACCOUNT_NUMBER=$(aws sts get-caller-identity --query 'Account' --output text)
# Create an IAM OIDC (Open ID Connect) provider
echo "Running: eksctl utils associate-iam-oidc-provider --region us-west-2 --cluster eks-lab-cluster --approve"
eksctl utils associate-iam-oidc-provider --region us-east-1 --cluster eks-lab-cluster --approve
# Create a Kubernetes service account named aws-load-balancer-controller in the kube-system namespace for the AWS Load Balancer Controller and annotate the Kubernetes service account with the name of the IAM role.
echo "Running: eksctl create iamserviceaccount --cluster=eks-lab-cluster --namespace=kube-system --name=aws-load-balancer-controller --role-name "AmazonEKSLoadBalancerControllerRole" --attach-policy-arn=arn:aws:iam::$ACCOUNT_NUMBER:policy/AWSLoadBalancerControllerIAMPolicy --approve"
eksctl create iamserviceaccount --cluster=eks-lab-cluster --namespace=kube-system --name=aws-load-balancer-controller --role-name "AmazonEKSLoadBalancerControllerRole" --attach-policy-arn=arn:aws:iam::$ACCOUNT_NUMBER:policy/AWSLoadBalancerControllerIAMPolicy --approve
sleep 5
# Add helm eks-charts repository
echo "Running: helm repo add eks https://aws.github.io/eks-charts"
helm repo add eks https://aws.github.io/eks-charts
# helm update
echo "Running: helm repo update"
helm repo update
# Install the AWS Load Balancer Controller.
## Reference: https://docs.aws.amazon.com/eks/latest/userguide/aws-load-balancer-controller.html
echo "Running: helm install aws-load-balancer-controller eks/aws-load-balancer-controller -n kube-system --set clusterName=eks-lab-cluster --set serviceAccount.create=false --set serviceAccount.name=aws-load-balancer-controller"
helm install aws-load-balancer-controller eks/aws-load-balancer-controller -n kube-system --set clusterName=eks-lab-cluster --set serviceAccount.create=false --set serviceAccount.name=aws-load-balancer-controller
